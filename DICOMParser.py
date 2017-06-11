import pydicom, os, sys

class DICOMParser:
  def __init__(self,fileName,rulesDictionary):
    try:
      self.dcm = pydicom.read_file(fileName)
    except:
      print "Failed to read input DICOM!"

    self.rulesDictionary = rulesDictionary

    self.tables = {}

  def getTables(self):
    return self.tables

  def parse(self):
    self.readTopLevelAttributes("CompositeContext")
    self.readReferences()

    if self.dcm.Modality in ["SR","PT","CT","SEG","RWV"]:
      self.readTopLevelAttributes(self.dcm.Modality)

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
         if resolvedAttribute is not None:
           print "Successfully resolved",a
         else:
           print "Failed to resolve",a

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
    for item in dataElement:
      if item.ConceptNameCodeSequence[0].CodeMeaning == conceptNameMeaning:
        return item.ConceptCodeSequence[0]
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
