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

    if self.dcm.Modality in ["SR","PT","CT","SEG","RWV"]:
      self.readTopLevelAttributes(self.dcm.Modality)

  def readTopLevelAttributes(self,tableName):
    self.tables[tableName] = {}
    for a in self.rulesDictionary[tableName]:
      try:
        dataElement = self.dcm.data_element(a)
        if dataElement.VM>1:
          self.tables[tableName][a] = '/'.join([str(i) for i in dataElement.value])
        else:
          self.tables[tableName][a] = str(dataElement.value)
#        else:
#          self.tables[table]
#        self.tables[tableName][a] = self.dcm.data_element(a).value
#        print self.dcm.data_element(a).VM
      except:
        self.tables[tableName][a] = None

      #print self.tables[tableName][a]
