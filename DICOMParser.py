import pydicom, os, sys

class DICOMParser:
  def __init__(self,fileName,rulesDictionary):
    try:
      self.dcm = pydicom.read_file(fileName)
    except:
      raise

    self.rulesDictionary = rulesDictionary

    self.tables = {}

  def getTables(self):
    return self.tables

  def parse(self):
    self.readTopLevelAttributes("CompositeContext")
    self.readReferences()

    modality = self.dcm.Modality
    if modality=="SR" and self.dcm.StudyDescription=="Clinical Data":
      modality = self.dcm.Modality = "CD"

    if modality in ["CD","SR","PT","CT","SEG","RWV"]:
      self.readTopLevelAttributes(self.dcm.Modality)

    if modality == "SEG":
      self.readSegments()
      self.readSegmentFrames()

    if modality == "CD":
      self.ClinicalDataParser(modality)

  def readTopLevelAttributes(self,modality):
    self.tables[modality] = {}
    unresolvedAttributes = []
    for a in self.rulesDictionary[modality]:
      try:
        dataElement = self.dcm.data_element(a)
        if dataElement.VM>1:
          self.tables[modality][a] = '/'.join([str(i) for i in dataElement.value])
        else:
          self.tables[modality][a] = str(dataElement.value)
#        else:
#          self.tables[table]
#        self.tables[tableName][a] = self.dcm.data_element(a).value
#        print self.dcm.data_element(a).VM
      except:
        unresolvedAttributes.append(a)
        self.tables[modality][a] = None

    for a in unresolvedAttributes:
      if hasattr(self,"read"+modality+a):
         resolvedAttribute = str(getattr(self, "read%s%s" % (modality, a) )())
         self.tables[modality][a] = resolvedAttribute
         '''
         if resolvedAttribute is not None:
           print "Successfully resolved",a
         else:
           print "Failed to resolve",a
         '''

      #print self.tables[tableName][a]

  # functions to read specific attributes that are not top-level or that are SR #   tree elements
  #def readReferencedImageRealWorldValueMappingSequence(self):
  #  de = self.dcm.data_element("ReferencedImageRealWorldValueMappingSequence")
  #  if de:
  #    de = de.data_element("RealWorldValueMappingSequence")
  #    if de:

  # given the input data element, which must be a SQ, and must have the structure
  #  of items that follow the pattern ConceptNameCodeSequence/ConceptCodeSequence, find the sequence item that has
  #  ConceptNameCodeSequence > CodeMeaning, and return the data element corresponding
  #  to the ConceptCodeSequnce matching the requested ConceptNameCodeSequence meaning
  def getConceptCodeByConceptNameMeaning(self,dataElement,conceptNameMeaning):
    if not dataElement is None:
      for item in dataElement:
        if item.ConceptNameCodeSequence[0].CodeMeaning == conceptNameMeaning:
          return item.ConceptCodeSequence[0]
    return None

  def getDateByConceptNameMeaning(self,dataElement,conceptNameMeaning):
    if not dataElement is None:
      for item in dataElement:
        if item.ConceptNameCodeSequence[0].CodeMeaning == conceptNameMeaning:
          return item.Date
    return None

  def getTextByConceptNameMeaning(self,dataElement,conceptNameMeaning):
    if not dataElement is None:
      for item in dataElement:
        if item.ConceptNameCodeSequence[0].CodeMeaning == conceptNameMeaning:
          return item.TextValue
    return None

  def getNumberByConceptNameMeaning(self,dataElement,conceptNameMeaning):
    if not dataElement is None:
      for item in dataElement:
        if item.ConceptNameCodeSequence[0].CodeMeaning == conceptNameMeaning:
          return item.MeasuredValueSequence[0].NumericValue
    return None

  def getContainerByConceptNameMeaning(self,dataElement,conceptNameMeaning):
    if not dataElement is None:
      for item in dataElement:
        if item.ConceptNameCodeSequence[0].CodeMeaning == conceptNameMeaning:
          try:
            return item.data_element('ContentSequence')
          except:
            return None
    return None


  def getMeasurementUnitsCodeSequence(self):
    dataElement = self.dcm.data_element("ReferencedImageRealWorldValueMappingSequence").value[0]
    dataElement = dataElement.data_element("RealWorldValueMappingSequence").value[0]
    dataElement = dataElement.data_element("MeasurementUnitsCodeSequence").value
    return dataElement

  def getQuantityDefinitionSequence(self):
    dataElement = self.dcm.data_element("ReferencedImageRealWorldValueMappingSequence").value[0]
    dataElement = dataElement.data_element("RealWorldValueMappingSequence").value[0]
    dataElement = dataElement.data_element("QuantityDefinitionSequence").value
    return dataElement

  def readRWVUnits_CodeValue(self):
    dataElement = self.getMeasurementUnitsCodeSequence()[0]
    return dataElement.CodeValue

  def readRWVUnits_CodingSchemeDesignator(self):
    dataElement = self.getMeasurementUnitsCodeSequence()[0]
    return dataElement.CodingSchemeDesignator

  def readRWVUnits_CodeMeaning(self):
    dataElement = self.getMeasurementUnitsCodeSequence()[0]
    return dataElement.CodeMeaning

  def readRWVQuantity_CodeValue(self):
    dataElement = self.getQuantityDefinitionSequence()
    dataElement = self.getConceptCodeByConceptNameMeaning(dataElement, "Quantity")
    return dataElement.CodeValue

  def readRWVQuantity_CodingSchemeDesignator(self):
    dataElement = self.getQuantityDefinitionSequence()
    dataElement = self.getConceptCodeByConceptNameMeaning(dataElement, "Quantity")
    return dataElement.CodingSchemeDesignator

  def readRWVQuantity_CodeMeaning(self):
    dataElement = self.getQuantityDefinitionSequence()
    dataElement = self.getConceptCodeByConceptNameMeaning(dataElement, "Quantity")
    return dataElement.CodeMeaning

  def readRWVMeasurementMethod_CodeValue(self):
    dataElement = self.getQuantityDefinitionSequence()
    dataElement = self.getConceptCodeByConceptNameMeaning(dataElement, "Measurement Method")
    return dataElement.CodeValue

  def readRWVMeasurementMethod_CodingSchemeDesignator(self):
    dataElement = self.getQuantityDefinitionSequence()
    dataElement = self.getConceptCodeByConceptNameMeaning(dataElement, "Measurement Method")
    return dataElement.CodingSchemeDesignator

  def readRWVMeasurementMethod_CodeMeaning(self):
    dataElement = self.getQuantityDefinitionSequence()
    dataElement = self.getConceptCodeByConceptNameMeaning(dataElement, "Measurement Method")
    return dataElement.CodeMeaning

  def readRWVRealWorldValueIntercept(self):
    dataElement = self.dcm.data_element("ReferencedImageRealWorldValueMappingSequence").value[0]
    dataElement = dataElement.data_element("RealWorldValueMappingSequence").value[0]
    return dataElement.RealWorldValueIntercept

  def readRWVRealWorldValueSlope(self):
    dataElement = self.dcm.data_element("ReferencedImageRealWorldValueMappingSequence").value[0]
    dataElement = dataElement.data_element("RealWorldValueMappingSequence").value[0]
    return dataElement.RealWorldValueSlope



  def ClinicalDataParser(self,modality):
#    self.tables[modality] = {}
    unresolvedAttributes = []
    completedContainers = []
    for a in self.rulesDictionary[modality]:
      if self.tables[modality][a] is not None:
        continue
      container = a.split('_',1)[0]
      if container in completedContainers:
        continue
      #Process by container
      if container in ('SocialHistory','TumorStaging','TNMCategory','MedicalHistory','Biopsy','Surgery','Radiotherapy','Chemotherapy','OriginalPathology','CervicalLymphNodeGroupExcision',
               'DiseaseOutcome','RecurrentPathology'):
        str(getattr(self, "readCD%s" % (container))(container))
        completedContainers.append(container)
      else:
        unresolvedAttributes.append(a)
        self.tables[modality][a] = None

  def readCDSocialHistory(self,container):
    dataElement = getattr(self,"getCD%sContainer"%(container))()
    self.readCDCode(container,'TobaccoSmokingBehavior','Tobacco Smoking Behavior',dataElement)
    self.readCDCode(container,'AlcoholConsumption','Alcohol consumption',dataElement)
    self.readCDCode(container,'DetailsOfTobaccoChewing','Details of tobacco chewing',dataElement)

  def readCDTumorStaging(self,container):
    dataElement = getattr(self,"getCD%sContainer"%(container))()
    self.readCDCode(container,"PrimaryTumorSite","Primary tumor site",dataElement)
    self.readCDCode(container,"TumorStageFinding","Tumor stage finding",dataElement)

  def readCDTNMCategory(self,container):
    dataElement = getattr(self,"getCD%sContainer"%(container))()
    self.readCDCode(container,"TStage","T Stage",dataElement)
    self.readCDCode(container,"NStage","N Stage",dataElement)
    self.readCDCode(container,"MStage","M Stage",dataElement)

  def readCDMedicalHistory(self,container):
    dataElement = getattr(self,"getCD%sContainer"%(container))()
    self.readCDCode(container,"RadiationTherapy","History of radiation therapy",dataElement)
    self.readCDCode(container,"MalignantNeoplasm","History of malignant neoplasm",dataElement)

  def readCDBiopsy(self,container):
    dataElement = getattr(self,"getCD%sContainer"%(container))()
    self.readCDDate(container,"DateOfProcedure","Date of procedure",dataElement)
    self.readCDText(container,"Site","Biopsy Site",dataElement)

  def readCDSurgery(self, container):
    dataElement = getattr(self, "getCD%sContainer" % (container))()
    self.readCDDate(container,"DateOfProcedure", "Date of procedure",dataElement)
    self.readCDText(container,"ProcedureDescription", "Procedure Description",dataElement)
    self.readCDCode(container,"ResectionOfPrimaryTumor", "Resection of primary tumor",dataElement),
    self.readCDCode(container,"BlockDissectionfCervicalLymphNodes", "Block dissection of cervical lymph nodes",dataElement),

  def readCDRadiotherapy(self,container):
    dataElement = getattr(self,"getCD%sContainer"%(container))()
    self.readCDDate(container,"DateTreatmentStarted", "Date treatment started",dataElement)
    self.readCDDate(container,"DateTreatmentStopped", "Date treatment stopped",dataElement)
    self.readCDNum(container,"TotalRadiationDoseDelivered", "Total radiation dose delivered",dataElement)
    self.readCDNum(container,"RadiationDosePerFraction", "Radiation dose per fraction",dataElement)
    self.readCDText(container,"ProcedureDescription","Procedure Description",dataElement)

  def readCDChemotherapy(self,container):
    dataElement = getattr(self,"getCD%sContainer"%(container))()
    self.readCDDate(container,"DateTreatmentStarted", "Date treatment started",dataElement)
    self.readCDDate(container,"DateTreatmentStopped", "Date treatment stopped",dataElement)
    self.readCDCode(container,"AntineoplasticAgent", "Antineoplastic agent",dataElement)  # Need to support up to 3

  def readCDOriginalPathology(self, container):
    dataElement = getattr(self, "getCD%sContainer" % (container))()
    self.readCDCode(container,"Pathology","Pathology",dataElement)
    if not dataElement is None:
      dataElement=dataElement[0].data_element('ContentSequence')
    self.readCDCode(container,"HistologicalGradeFinding","Histological grade finding"   ,dataElement)
    self.readCDCode(container,"MalignancyType","Malignancy Type",dataElement)
    self.readCDCode(container,"TumorMarginStatus","Tumor margin status",dataElement)
    self.readCDCode(container,"PerineuralInvasionFinding","Perineural invasion finding",dataElement)
    self.readCDCode(container,"StatusOfVascularInvasionByTumor","Status of vascular invasion by tumor",dataElement)

  def readCDCervicalLymphNodeGroupExcision(self, container):
    dataElement = getattr(self, "getCD%sContainer" % (container))()
    self.readCDCode(container,"CervicalLymphNodeGroup","Cervical lymph node group",dataElement)
    self.readCDCode(container,"Sidedness","Sidedness",dataElement)
    self.readCDNum(container,"NumberOfNodesRemoved","Number of nodes removed",dataElement)
    self.readCDNum(container,"NumberOfNodesPositive","Number of nodes positive",dataElement)
    self.readCDText(container,"Comment","Comment",dataElement)

  def readCDDiseaseOutcome(self, container):
    dataElement = getattr(self, "getCD%sContainer" % (container))()
    self.readCDDate(container,"FollowupVisitDate","Follow-up visit date",dataElement)
    self.readCDCode(container,"FollowupStatus","Follow-up status",dataElement)
    self.readCDDate(container,"DateOfDeath","Date of death",dataElement)
    self.readCDCode(container,"CauseOfDeath","Cause of death",dataElement)
    self.readCDCode(container,"PostRadiotherapyTreatment","Post-radiotherapy treatment",dataElement)
    self.readCDDate(container,"DateOf2ndPrimary","Date of cancer recurrence",dataElement)
    self.readCDCode(container,"LocationOfFirstRecurrence","Location of first recurrence",dataElement)

  def readCDRecurrentPathology(self, container):
    dataElement = getattr(self, "getCD%sContainer" % (container))()
    self.readCDCode(container, "Pathology", "Pathology",dataElement)
    if not dataElement is None:
      dataElement = dataElement[0].data_element('ContentSequence')
    self.readCDCode(container, "HistologicalGradeFinding", "Histological grade finding",dataElement)
    self.readCDCode(container, "MalignancyType", "Malignancy Type",dataElement)
    self.readCDCode(container, "TumorMarginStatus", "Tumor margin status",dataElement)
    self.readCDCode(container, "PerineuralInvasionFinding", "Perineural invasion finding",dataElement)
    self.readCDCode(container, "StatusOfVascularInvasionByTumor", "Status of vascular invasion by tumor",dataElement)

  def readCDCode(self,container,field,codeMeaning,dataElement):
    dataElement = self.getConceptCodeByConceptNameMeaning(dataElement,codeMeaning)
    if dataElement is None:
      self.tables['CD']["%s_%s_CodeValue"%(container,field)] = None
      self.tables['CD']["%s_%s_CodingSchemeDesignator"%(container,field)] = None
      self.tables['CD']["%s_%s_CodeMeaning"%(container,field)] = None
    else:
      self.tables['CD']["%s_%s_CodeValue" % (container, field)] = dataElement.CodeValue
      self.tables['CD']["%s_%s_CodingSchemeDesignator" % (container, field)] = dataElement.CodingSchemeDesignator
      self.tables['CD']["%s_%s_CodeMeaning" % (container, field)] = dataElement.CodeMeaning

  def readCDDate(self,container,field,codeMeaning,dataElement):
    date = self.getDateByConceptNameMeaning(dataElement,codeMeaning)
    self.tables['CD']["%s_%s" % (container, field)] = date

  def readCDText(self,container,field,codeMeaning,dataElement):
    text = self.getTextByConceptNameMeaning(dataElement,codeMeaning)
    self.tables['CD']["%s_%s"%(container, field)] = text

  def readCDNum(self,container,field,codeMeaning,dataElement):
    number = self.getNumberByConceptNameMeaning(dataElement,codeMeaning)
    self.tables['CD']["%s_%s"%(container, field)] = number

  def getCDSocialHistoryContainer(self):
    return self.getCDSummaryClinicalDocumentContainer()[3].data_element('ContentSequence')

  def getCDTumorStagingContainer(self):
    return self.getCDSummaryClinicalDocumentContainer()[4].data_element('ContentSequence')

  def getCDTNMCategoryContainer(self):
    dataElement = self.getCDTumorStagingContainer()
    return self.getContainerByConceptNameMeaning(dataElement,"TNM Category")

  def getCDMedicalHistoryContainer(self):
    return self.getCDSummaryClinicalDocumentContainer()[5].data_element('ContentSequence')

  def getCDDiagnosticProcedureContainer(self):
    try:
      return self.getCDSummaryClinicalDocumentContainer()[6].data_element('ContentSequence')
    except:
      return None

  def getCDBiopsyContainer(self):
    dataElement =  self.getCDDiagnosticProcedureContainer()
    return self.getContainerByConceptNameMeaning(dataElement,"Biopsy")

  def getCDTherapeuticProcedureContainer(self):
    return self.getCDSummaryClinicalDocumentContainer()[7].data_element('ContentSequence')

  def getCDSurgeryContainer(self):
    dataElement = self.getCDTherapeuticProcedureContainer()
    return self.getContainerByConceptNameMeaning(dataElement,"Surgical Procedure")

  def getCDRadiotherapyContainer(self):
    dataElement = self.getCDTherapeuticProcedureContainer()
    return self.getContainerByConceptNameMeaning(dataElement,"Radiotherapy Procedure")

  def getCDChemotherapyContainer(self):
    dataElement =  self.getCDTherapeuticProcedureContainer()
    return self.getContainerByConceptNameMeaning(dataElement,"Chemotherapy")

  def getCDPathologyOfOriginalTumorContainer(self):
    return self.getCDSummaryClinicalDocumentContainer()[8].data_element('ContentSequence')

  def getCDOriginalPathologyContainer(self):
    dataElement =  self.getCDPathologyOfOriginalTumorContainer()
    return self.getContainerByConceptNameMeaning(dataElement,"Pathology Results")

  def getCDCervicalLymphNodeGroupExcisionContainer(self):
    dataElement =  self.getCDPathologyOfOriginalTumorContainer()
    return self.getContainerByConceptNameMeaning(dataElement,"Excision of cervical lymph nodes group")

  def getCDDiseaseOutcomeContainer(self):
    return self.getCDSummaryClinicalDocumentContainer()[9].data_element('ContentSequence')

  def getCDRecurrentPathologyContainer(self):
    dataElement =  self.getCDDiseaseOutcomeContainer()
    return self.getContainerByConceptNameMeaning(dataElement,"Pathology of recurrent tumor")

  def getCDSummaryClinicalDocumentContainer(self):
    return self.dcm.data_element("ContentSequence")

  # this part is not driven at all by the QDBD schema!
  #  (maybe it should be changed to generalize things better)
  def readReferences(self):
    self.tables["References"] = []
    try:
      refSeriesSeq = self.dcm.data_element("ReferencedSeriesSequence")
    except:
      refSeriesSeq = None
    try:
      evidenceSeq = self.dcm.data_element("CurrentRequestedProcedureEvidenceSequence")
    except:
      evidenceSeq = None

    if refSeriesSeq:
      self.readReferencedSeriesSequence(refSeriesSeq)
    if evidenceSeq:
      self.readEvidenceSequence(evidenceSeq)

  def readReferencedSeriesSequence(self, seq):
    for r in seq:
      seriesUID = r.data_element("SeriesInstanceUID").value
      refInstancesSeq = r.data_element("ReferencedInstanceSequence").value
      for i in refInstancesSeq:
        refClassUID = i.ReferencedSOPClassUID
        refInstanceUID = i.ReferencedSOPInstanceUID

        self.tables["References"].append({"SOPInstanceUID": self.dcm.SOPInstanceUID, "ReferencedSOPClassUID": refClassUID, "ReferencedSOPInstanceUID": refInstanceUID, "SeriesInstanceUID": seriesUID})

  def readEvidenceSequence(self, seq):
    for l1item in seq:
      seriesSeq = l1item.data_element("ReferencedSeriesSequence").value
      for l2item in seriesSeq:
        sopSeq = l2item.data_element("ReferencedSOPSequence").value
        seriesUID = l2item.SeriesInstanceUID
        for l3item in sopSeq:
          refClassUID = l3item.ReferencedSOPClassUID
          refInstanceUID = l3item.ReferencedSOPInstanceUID

          self.tables["References"].append({"SOPInstanceUID": self.dcm.SOPInstanceUID, "ReferencedSOPClassUID": refClassUID, "ReferencedSOPInstanceUID": refInstanceUID, "SeriesInstanceUID": seriesUID})

  def readSegments(self):
    seq = self.dcm.data_element("SegmentSequence")
    self.tables["SEG_Segments"] = []

    for segment in seq:
      sAttr = {}

      # Attrubute should be either in a sub-sequence, at the
      #  top level of the sequence, or at the top level of the dataset
      #  Try all those options
      for attr in self.rulesDictionary["SEG_Segments"]:
        if attr.find("_")>0:
          # it is (supposed to be!) a code tuple in a sequence
          seqName,attrName = attr.split("_")
          sAttr[attr] = segment.data_element(seqName)[0].data_element(attrName).value
        else:
          try:
            sAttr[attr] = segment.data_element(attr).value
          except:
            try:
              sAttr[attr] = self.dcm.data_element(attr).value
            except:
              sAttr[attr] = None

      self.tables["SEG_Segments"].append(sAttr)

  def readSegmentFrames(self):
    pfFG = self.dcm.data_element("PerFrameFunctionalGroupsSequence")
    sFG = self.dcm.data_element("SharedFunctionalGroupsSequence")

    self.tables["SEG_SegmentFrames"] = []

    # Attrubute should be either in a sub-sequence, in the shared FG,
    #  or at the top level of the dataset
    #  Try all those options
    for frame in pfFG:
      fAttr = {}
      for attr in self.rulesDictionary["SEG_SegmentFrames"]:
        # print "Looking for",attr
        # recursively search in the per-frame FG item
        value = self.recursiveFindInDataset(frame,attr)
        if value is None:
          # recursively search in the shared FG
          value = self.recursiveFindInDataElement(sFG,attr)
        # if those fail, look it up top-level
        if value is None:
          value = self.dcm.data_element(attr).value
        fAttr[attr] = value
      self.tables["SEG_SegmentFrames"].append(fAttr)

  # idea from https://github.com/pieper/Chronicle/blob/master/bin/record.py#L58
  def recursiveFindInDataElement(self,de,attr):
    if de.keyword == attr:
      return de.value
    elif de.VR == "SQ":
      for item in de:
        return self.recursiveFindInDataset(item,attr)
    return None

  def recursiveFindInDataset(self,ds,attr):
    for key in ds.keys():
      de = ds[key]
      value = self.recursiveFindInDataElement(de,attr)
      if value is not None:
        return value
    return None
