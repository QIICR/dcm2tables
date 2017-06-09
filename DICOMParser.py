import dicom, os, sys

class DICOMParser:
  def __init__(self,fileName,rulesDictionary):
    try:
      self.dcm = dicom.read_file(fileName)
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
          self.tables[modality][a] = getattr(self, "read%s%s" % (modality, a) )()

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
    for item in dataElement.value:
      if item.ConceptNameCodeSequence[0].CodeMeaning == conceptNameMeaning:
        return item.ConceptCodeSequence[0]
    return None

  def getMeasurementUnitsCodeSequence(self):
    dataElement = self.dcm.data_element("ReferencedImageRealWorldValueMappingSequence").value[0]
    dataElement = dataElement.data_element("RealWorldValueMappingSequence").value[0]
    dataElement = dataElement.data_element("MeasurementUnitsCodeSequence").value
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

  # this part is not driven at all by the QDBD schema!
  #  (maybe it should be changed to generalize things better)
  def readReferences(self):
    self.tables["References"] = []
    refSeriesSeq = self.dcm.data_element("ReferencedSeriesSequence")
    for r in refSeriesSeq:
      seriesUID = r.data_element("SeriesInstanceUID").value
      refInstancesSeq = r.data_element("ReferencedInstanceSequence").value
      for i in refInstancesSeq:
        refClassUID = i.ReferencedSOPClassUID
        refInstanceUID = i.ReferencedSOPInstanceUID

        self.tables["References"].append({"SOPInstanceUID": self.dcm.SOPInstanceUID, "ReferencedSOPClassUID": refClassUID, "ReferencedSOPInstanceUID": refInstanceUID, "SeriesInstanceUID": seriesUID})
