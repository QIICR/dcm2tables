import pydicom

class DICOMObject:
  def __init__(self,fileName):
    self.dcm = pydicom.read_file(fileName)
