from DICOMParser import DICOMParser
import pydicom
import copy

class SRCDParser(DICOMParser):
    def parse(self):
        modality = self.dcm.Modality
        if modality == "SR":
          self.readTopLevelAttributes("CD")
          if hasattr(self.dcm, "ContentTemplateSequence"):
            if self.dcm.ContentTemplateSequence[0].TemplateIdentifier == "QIICR_2000":
              self.ClinicalDataParser("CD")
            else:
              super(SRCDParser,self).parse()
        else:
          super(SRCDParser, self).parse()

    def ClinicalDataParser(self, modality):
        completedContainers = []
        self.tables['CD']=[self.tables['CD']]
        for container in ('ProblemList','SocialHistory','TumorStaging','MedicalHistory','Biopsy','Surgery','Radiotherapy',
                  'Chemotherapy','OriginalPathology','CervicalLymphNodeGroupExcision','DiseaseOutcome'):
            str(getattr(self, "readCD%s" % (container))(container))
            completedContainers.append(container)

    def readCDProblemList(self, container):
        dataElement = getattr(self, "getCD%sContainer" % (container))()
        if not dataElement is None:
            dataElement=dataElement[0].ContentSequence
            self.readCDValue(container, 'Code', 'Problem', 'Problem', dataElement[0])
            srcTables=self.tables['CD']
            self.tables['CD']=[]
            for i in range(1,len(dataElement)):
                destTables=copy.deepcopy(srcTables)
                self.readCDValueMulti(container, 'Code', 'Therapy', 'Therapy', dataElement[i], destTables)
                self.tables['CD'] += destTables

    def readCDSocialHistory(self, container):
        dataElement = getattr(self, "getCD%sContainer" % (container))()
        if not dataElement is None:
            self.readCDValue(container, 'Code', 'TobaccoSmokingBehavior', 'Tobacco Smoking Behavior', dataElement)
            self.readCDValue(container, 'Code', 'AlcoholConsumption', 'Alcohol consumption', dataElement)
            self.readCDValue(container, 'Code', 'DetailsOfTobaccoChewing', 'Details of tobacco chewing', dataElement)

    def readCDTumorStaging(self, container):
        dataElement = getattr(self, "getCD%sContainer" % (container))()
        if not dataElement is None:
            self.readCDValue(container, 'Code', "PrimaryTumorSite", "Primary tumor site", dataElement)
            self.readCDValue(container, "Code", "TumorStageFinding", "Tumor stage finding", dataElement)
            dataElement = self.getContainerByConceptNameMeaning(dataElement, "TNM Category")
            if not dataElement is None:
                self.readCDValue(container, "Code", "TStage", "T Stage", dataElement)
                self.readCDValue(container, "Code", "NStage", "N Stage", dataElement)
                self.readCDValue(container, "Code", "MStage", "M Stage", dataElement)

    def readCDMedicalHistory(self, container):
        dataElement = getattr(self, "getCD%sContainer" % (container))()
        if not dataElement is None:
            self.readCDValue(container, "Code", "RadiationTherapy", "History of radiation therapy", dataElement)
            self.readCDValue(container, "Code", "MalignantNeoplasm", "History of malignant neoplasm", dataElement)

    def readCDBiopsy(self, container):
        dataElements = getattr(self, "getCD%sContainer" % (container))()
        if not dataElements is None and dataElements.VM>0:
            srcTables=self.tables['CD']
            self.tables['CD']=[]
            for dataElement in dataElements:
                destTables=copy.deepcopy(srcTables)
                dataElement = dataElement.ContentSequence
                self.readCDValueMulti(container, "Date", "DateOfProcedure", "Date of procedure", dataElement,
                    destTables)
                self.readCDValueMulti(container, "TextValue", "Site", "Biopsy Site", dataElement,
                    destTables)
                self.tables['CD'] += destTables

    def readCDSurgery(self, container):
        dataElements = getattr(self, "getCD%sContainer" % (container))()
        if not dataElements is None and len(dataElements)>0:
            srcTables=self.tables['CD']
            self.tables['CD']=[]
            for dataElement in dataElements:
                destTables=copy.deepcopy(srcTables)
                self.readCDValueMulti(container, "Date", "DateOfProcedure", "Date of procedure", dataElement,
                    destTables)
                self.readCDValueMulti(container, "TextValue", "ProcedureDescription", "Procedure Description",
                    dataElement, destTables)
                self.readCDValueMulti(container, "Code", "ResectionOfPrimaryTumor", "Resection of primary tumor",
                    dataElement, destTables)
                self.readCDValueMulti(container, "Code", "BlockDissectionOfCervicalLymphNodes",
                    "Block dissection of cervical lymph nodes", dataElement, destTables)
                self.tables['CD'] += destTables

    def readCDRadiotherapy(self, container):
        dataElements = getattr(self, "getCD%sContainer" % (container))()
        if not dataElements is None and len(dataElements)>0:
            srcTables=self.tables['CD']
            self.tables['CD']=[]
            for dataElement in dataElements:
                destTables=copy.deepcopy(srcTables)
                self.readCDValueMulti(container, "Date", "DateTreatmentStarted", "Date treatment started", dataElement,
                    destTables)
                self.readCDValueMulti(container, "Date", "DateTreatmentStopped", "Date treatment stopped", dataElement,
                    destTables)
                self.readCDValueMulti(container, "NumericValue", "TotalRadiationDoseDelivered",
                    "Total radiation dose delivered", dataElement, destTables)
                self.readCDValueMulti(container, "NumericValue", "RadiationDosePerFraction", "Radiation dose per fraction",
                    dataElement, destTables)
                self.readCDValueMulti(container, "TextValue", "ProcedureDescription", "Procedure Description", dataElement,
                    destTables)
                self.tables['CD'] += destTables

    def readCDChemotherapy(self, container):
        dataElements = getattr(self, "getCD%sContainer" % (container))()
        if not dataElements is None and len(dataElements)>0:
            srcTables = self.tables['CD']
            self.tables['CD'] = []
            for dataElement in dataElements:
                destTables=copy.deepcopy(srcTables)
                self.readCDValueMulti(container, "Date", "DateTreatmentStarted", "Date treatment started", dataElement,
                    destTables)
                self.readCDValueMulti(container, "Date", "DateTreatmentStopped", "Date treatment stopped", dataElement,
                    destTables)
                self.readCDValueMulti(container, "Code", "AntineoplasticAgent", "Antineoplastic agent",
                    dataElement, destTables)  # Need to support up to 3
                self.tables['CD'] += destTables

    def readCDOriginalPathology(self, container):
        dataElement = getattr(self, "getCD%sContainer" % (container))()
        if not dataElement is None:
            self.readCDValue(container, "Code", "Pathology", "Pathology", dataElement)
            dataElement = dataElement[0].data_element('ContentSequence')
            if not dataElement is None:
                self.readCDValue(container, "Code", "HistologicalGradeFinding", "Histological grade finding",
                                 dataElement)
                self.readCDValue(container, "Code", "MalignancyType", "Malignancy Type", dataElement)
                self.readCDValue(container, "Code", "TumorMarginStatus", "Tumor margin status", dataElement)
                self.readCDValue(container, "Code", "PerineuralInvasionFinding", "Perineural invasion finding",
                                 dataElement)
                self.readCDValue(container, "Code", "StatusOfVascularInvasionByTumor",
                                 "Status of vascular invasion by tumor", dataElement)

    def readCDCervicalLymphNodeGroupExcision(self, container):
        dataElements = getattr(self, "getCD%sContainer" % (container))()
        if not dataElements is None:
            lymphNodeGroup = [dataElement for dataElement in dataElements if
                self.readCDValue(container, "Code", "StatusOfExtraCapsularExtensionOfNodalTumor",
                   "Status of extra-capsular extension of nodal tumor", dataElement) +
                self.readCDValue(container, "TextValue", "Comment", "Comment", dataElement) == 0]
            if len(lymphNodeGroup)>0:
                srcTables=self.tables['CD']
                self.tables['CD']=[]
                for dataElement in lymphNodeGroup:
                    destTables=copy.deepcopy(srcTables)
                    self.readCDValueMulti(container,"Code","CervicalLymphNodeGroup","Cervical lymph node group",dataElement,
                        destTables)
                    try:
                        dataElement = dataElement.data_element('ContentSequence')
                        self.readCDValueMulti(container, "Code", "Sidedness", "Sidedness", dataElement, destTables)
                        self.readCDValueMulti(container, "NumericValue", "NumberOfNodesRemoved", "Number of nodes removed",
                             dataElement, destTables)
                        self.readCDValueMulti(container, "NumericValue", "NumberOfNodesPositive", "Number of nodes positive",
                             dataElement, destTables)
                    except:
                        pass
                    self.tables['CD'] += destTables

    def readCDDiseaseOutcome(self, container):
        dataElement = getattr(self, "getCD%sContainer" % (container))()
        if not dataElement is None:
            self.readCDValue(container, "Date", "FollowupVisitDate", "Follow-up visit date", dataElement)
            self.readCDValue(container, "Code", "FollowupStatus", "Followup status", dataElement)
            self.readCDValue(container, "Date", "DateOfDeath", "Date of death", dataElement)
            self.readCDValue(container, "Code", "CauseOfDeath", "Cause of death", dataElement)
            self.readCDValue(container, "Code", "PostRadiotherapyTreatment", "Post-radiotherapy treatment", dataElement)
            self.readCDValue(container, "Date", "DateOfCancerRecurrence", "Date of cancer recurrence", dataElement)
            self.readCDValue(container, "Code", "LocationOfFirstRecurrence", "Location of first recurrence",
                             dataElement)
            dataElement = self.getContainerByConceptNameMeaning(dataElement, "Pathology of recurrent tumor")
            if not dataElement is None:
                dataElement = dataElement[0].data_element('ContentSequence')
                self.readCDValue(container, "Code", "Pathology", "Pathology", dataElement)
                dataElement = dataElement[0].data_element('ContentSequence')
                self.readCDValue(container, "Code", "HistologicalGradeFinding", "Histological grade finding",
                                 dataElement)
                self.readCDValue(container, "Code", "MalignancyType", "Malignancy Type", dataElement)
                self.readCDValue(container, "Code", "TumorMarginStatus", "Tumor margin status", dataElement)
                self.readCDValue(container, "Code", "PerineuralInvasionFinding", "Perineural invasion finding",
                                 dataElement)
                self.readCDValue(container, "Code", "StatusOfVascularInvasionByTumor",
                                 "Status of vascular invasion by tumor", dataElement)

    def readCDValueMulti(self, container, valueType, field, codeMeaning, dataElement,destTables):
        value = None
        if type(dataElement) == pydicom.dataset.Dataset:
            if dataElement.ConceptNameCodeSequence[0].CodeMeaning == codeMeaning:
                if valueType == "Date" or valueType == "TextValue":
                    value = dataElement.data_element(valueType).value
                elif valueType == "NumericValue":
                    value = dataElement.MeasuredValueSequence[0].NumericValue
                elif valueType == "Code":
                    value = dataElement.ConceptCodeSequence[0]
        else:
            for item in dataElement:
                if item.ConceptNameCodeSequence[0].CodeMeaning == codeMeaning:
                    if valueType == "Date" or valueType == "TextValue":
                        value = item.data_element(valueType).value
                    elif valueType == "NumericValue":
                        value = item.MeasuredValueSequence[0].NumericValue
                    elif valueType == "Code":
                        value = item.ConceptCodeSequence[0]
                    break
        if not value is None:
            for table in destTables:
                if valueType == "Code":
                    table["%s_%s_CodeValue" % (container, field)] = value.CodeValue
                    table["%s_%s_CodingSchemeDesignator" % (container, field)] = value.CodingSchemeDesignator
                    table["%s_%s_CodeMeaning" % (container, field)] = value.CodeMeaning
                else:
                    table["%s_%s" % (container, field)] = value
        return not value is None

    def readCDValue(self, container, valueType, field, codeMeaning, dataElement):
        value = None
        if type(dataElement) == pydicom.dataset.Dataset:
            if dataElement.ConceptNameCodeSequence[0].CodeMeaning == codeMeaning:
                if valueType == "Date" or valueType == "TextValue":
                    value = dataElement.data_element(valueType).value
                elif valueType == "NumericValue":
                    value = dataElement.MeasuredValueSequence[0].NumericValue
                elif valueType == "Code":
                    value = dataElement.ConceptCodeSequence[0]
        else:
            for item in dataElement:
                if item.ConceptNameCodeSequence[0].CodeMeaning == codeMeaning:
                    if valueType == "Date" or valueType == "TextValue":
                        value = item.data_element(valueType).value
                    elif valueType == "NumericValue":
                        value = item.MeasuredValueSequence[0].NumericValue
                    elif valueType == "Code":
                        value = item.ConceptCodeSequence[0]
                    break
        if not value is None:
            for table in self.tables['CD']:
                if valueType == "Code":
                    table["%s_%s_CodeValue" % (container, field)] = value.CodeValue
                    table["%s_%s_CodingSchemeDesignator" % (container, field)] = value.CodingSchemeDesignator
                    table["%s_%s_CodeMeaning" % (container, field)] = value.CodeMeaning
                else:
                    table["%s_%s" % (container, field)] = value
        return not value is None

    def getCDProblemListContainer(self):
        container = self.getCDSummaryClinicalDocumentContainer()[2]
        try:
            return container.data_element('ContentSequence')
        except:
            return None

    def getCDSocialHistoryContainer(self):
        return self.getCDSummaryClinicalDocumentContainer()[3].data_element('ContentSequence')

    def getCDTumorStagingContainer(self):
        return self.getCDSummaryClinicalDocumentContainer()[4].data_element('ContentSequence')

    def getCDTNMCategoryContainer(self):
        dataElement = self.getCDTumorStagingContainer()
        return self.getContainerByConceptNameMeaning(dataElement, "TNM Category")

    def getCDMedicalHistoryContainer(self):
        return self.getCDSummaryClinicalDocumentContainer()[5].data_element('ContentSequence')

    def getCDDiagnosticProcedureContainer(self):
        try:
            return self.getCDSummaryClinicalDocumentContainer()[6].data_element('ContentSequence')
        except:
            return None

    def getCDBiopsyContainer(self):
        return self.getCDDiagnosticProcedureContainer()

    def getCDTherapeuticProcedureContainer(self):
        return self.getCDSummaryClinicalDocumentContainer()[7].data_element('ContentSequence')

    def getCDSurgeryContainer(self):
        containers = self.getCDTherapeuticProcedureContainer()
        surgeryContainers = []
        for container in containers:
            if container.ConceptNameCodeSequence[0].CodeMeaning == "Surgical Procedure":
                surgeryContainers.append(container.ContentSequence)
        return surgeryContainers

    def getCDRadiotherapyContainer(self):
        containers = self.getCDTherapeuticProcedureContainer()
        surgeryContainers = []
        for container in containers:
            if container.ConceptNameCodeSequence[0].CodeMeaning == "Radiotherapy Procedure":
                surgeryContainers.append(container.ContentSequence)
        return surgeryContainers

    def getCDChemotherapyContainer(self):
        containers = self.getCDTherapeuticProcedureContainer()
        surgeryContainers = []
        for container in containers:
            if container.ConceptNameCodeSequence[0].CodeMeaning == "Chemotherapy":
                surgeryContainers.append(container.ContentSequence)
        return surgeryContainers

    def getCDPathologyOfOriginalTumorContainer(self):
        return self.getCDSummaryClinicalDocumentContainer()[8].data_element('ContentSequence')

    def getCDOriginalPathologyContainer(self):
        dataElement = self.getCDPathologyOfOriginalTumorContainer()
        return self.getContainerByConceptNameMeaning(dataElement, "Pathology Results")

    def getCDCervicalLymphNodeGroupExcisionContainer(self):
        dataElement = self.getCDPathologyOfOriginalTumorContainer()
        return self.getContainerByConceptNameMeaning(dataElement, "Excision of cervical lymph nodes group")

    def getCDDiseaseOutcomeContainer(self):
        return self.getCDSummaryClinicalDocumentContainer()[9].data_element('ContentSequence')

    def getCDSummaryClinicalDocumentContainer(self):
        return self.dcm.data_element("ContentSequence")

    def getContainerByConceptNameMeaning(self, dataElement, conceptNameMeaning):
        if not dataElement is None:
            for item in dataElement:
                if item.ConceptNameCodeSequence[0].CodeMeaning == conceptNameMeaning:
                    try:
                        return item.data_element('ContentSequence')
                    except:
                        return None
        return None
