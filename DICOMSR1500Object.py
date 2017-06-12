class DICOMSRObject(DICOMObject):
  def __init__(self,fileName):
    super(DICOMObject,self).__init__(fileName)

    self.readTemplateInfo()

  def readTemplateInfo(self):
    self.templateID = self.dcm.ContentTemplateSequence.value[0].TemplateIdentifier
