from DICOMParser import DICOMParser
import pydicom

class SRCDParser(DICOMParser):
    def __init__(self,fileName,rulesDictionary):
        super(SRCDParser,self).__init__(fileName,rulesDictionary)
        #DICOMParser.__init__(self,fileName,rulesDictionary)

    def parse(self):
        modality = self.dcm.Modality
        if modality == "SR" and self.dcm.StudyDescription == "Clinical Data":
            self.readTopLevelAttributes("CD")
            self.ClinicalDataParser("CD")
        else:
            super(SRCDParser,self).parse()

    def ClinicalDataParser(self, modality):
        #    self.tables[modality] = {}
        unresolvedAttributes = []
        completedContainers = []
        for a in self.rulesDictionary[modality]:
            if self.tables[modality][a] is not None:
                continue
            container = a.split('_', 1)[0]
            if container in completedContainers:
                continue
            # Process by container
            str(getattr(self, "readCD%s" % (container))(container))
            completedContainers.append(container)

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
        if not dataElements is None:
            for dataElement in dataElements:
                dataElement = dataElement.ContentSequence
                self.readCDValue(container, "Date", "DateOfProcedure", "Date of procedure", dataElement)
                self.readCDValue(container, "TextValue", "Site", "Biopsy Site", dataElement)

    def readCDSurgery(self, container):
        dataElements = getattr(self, "getCD%sContainer" % (container))()
        if not dataElements is None:
            for dataElement in dataElements:
                self.readCDValue(container, "Date", "DateOfProcedure", "Date of procedure", dataElement)
                self.readCDValue(container, "TextValue", "ProcedureDescription", "Procedure Description", dataElement)
                self.readCDValue(container, "Code", "ResectionOfPrimaryTumor", "Resection of primary tumor",
                                 dataElement),
                self.readCDValue(container, "Code", "BlockDissectionOfCervicalLymphNodes",
                                 "Block dissection of cervical lymph nodes", dataElement),

    def readCDRadiotherapy(self, container):
        dataElements = getattr(self, "getCD%sContainer" % (container))()
        if not dataElements is None:
            for dataElement in dataElements:
                self.readCDValue(container, "Date", "DateTreatmentStarted", "Date treatment started", dataElement)
                self.readCDValue(container, "Date", "DateTreatmentStopped", "Date treatment stopped", dataElement)
                self.readCDValue(container, "NumericValue", "TotalRadiationDoseDelivered",
                                 "Total radiation dose delivered", dataElement)
                self.readCDValue(container, "NumericValue", "RadiationDosePerFraction", "Radiation dose per fraction",
                                 dataElement)
                self.readCDValue(container, "TextValue", "ProcedureDescription", "Procedure Description", dataElement)

    def readCDChemotherapy(self, container):
        dataElements = getattr(self, "getCD%sContainer" % (container))()
        if not dataElements is None:
            for dataElement in dataElements:
                self.readCDValue(container, "Date", "DateTreatmentStarted", "Date treatment started", dataElement)
                self.readCDValue(container, "Date", "DateTreatmentStopped", "Date treatment stopped", dataElement)
                self.readCDValue(container, "Code", "AntineoplasticAgent", "Antineoplastic agent",
                                 dataElement)  # Need to support up to 3

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

    def readCD"Cervical lymph node group"(self, container):
        dataElements = getattr(self, "getCD%sContainer" % (container))()
        if not dataElements is None:
            lymphNodeGroup = [dataElement for dataElement in dataElements if
                self.readCDValue(container, "Code", "StatusOfExtraCapsularExtensionOfNodalTumor",
                   "Status of extra-capsular extension of nodal tumor", dataElement) +
                self.readCDValue(container, "TextValue", "Comment", "Comment", dataElement) == 0]
            for dataElement in lymphNodeGroup:
                self.readCDValue(container,"Code","CervicalLymphNodeGroup","Cervical lymph node group",dataElement)
                try:
                    dataElement = dataElement.data_element('ContentSequence')
                    self.readCDValue(container, "Code", "Sidedness", "Sidedness", dataElement)
                    self.readCDValue(container, "NumericValue", "NumberOfNodesRemoved", "Number of nodes removed",
                                     dataElement)
                    self.readCDValue(container, "NumericValue", "NumberOfNodesPositive", "Number of nodes positive",
                                     dataElement)
                except:
                    return

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
            if valueType == "Code":
                self.tables['CD']["%s_%s_CodeValue" % (container, field)] = value.CodeValue
                self.tables['CD']["%s_%s_CodingSchemeDesignator" % (container, field)] = value.CodingSchemeDesignator
                self.tables['CD']["%s_%s_CodeMeaning" % (container, field)] = value.CodeMeaning
            else:
                self.tables['CD']["%s_%s" % (container, field)] = value
        return not value is None

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
