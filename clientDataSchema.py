CDschema = {
    "SocialHistory":(
        ("CODE","TobaccoSmokingBehavior","Tobacco Smoking Behavior"),
        ("CODE","AlcoholConsumption","Alcohol consumption"),
        ("CODE","DetailsOfTobaccoChewing","Details of tobacco chewing")),
    "TumorStaging":(
        ("CODE","PrimaryTumorSite","Primary tumor site"),
        ("CODE","TumorStageFinding","Tumor stage finding"),
        ("CODE","TStage","T Stage"),
        ("CODE","NStage","N Stage"),
        ("CODE","MStage","M Stage")),
    "MedicalHistory":(
        ("CODE","RadiationTherapy","History of radiation therapy"),
        ("CODE","MalignantNeoplasm","History of malignant neoplasm")),
    "DiagnosticProcedure":(),
    "Biopsy":(
        ("DATE","DateOfProcedure","Date of procedure"),
        ("TEXT","Site","Biopsy Site")),
    "Therapeutic Procedure":(),
    "Surgery":(
        ("DATE","DateOfProcedure","Date of procedure"),
        ("TEXT","ProcedureDescription","Procedure Description"),
        ("CODE","ResectionOfPrimaryTumor","Resection of primary tumor"),
        ("CODE","BlockDissectionfCervicalLymphNodes","Block dissection of cervical lymph nodes")),
    "Radiotherapy":(
        ("DATE","DateTreatmentStarted","Date treatment started"),
        ("DATE","DateTreatmentStopped","Date treatment stopped"),
        ("NUM","TotalRadiationDoseDelivered","Total radiation dose delivered"),
        ("NUM","RadiationDosePerFraction","Radiation dose per fraction"),
        ("TEXT","ProcedureDescription","Procedure Description")),
    "Chemotherapy":(
        ("DATE","DateTreatmentStarted","Date treatment started"),
        ("DATE","DateTreatmentStopped","Date treatment stopped"),
        ("CODE","AntineoplasticAgent","Antineoplastic agent")), #Need to support up to 3
    "Pathology of original tumor":(),
    "OriginalPathology":(
        ("CODE","Pathology","Pathology"),
        ("CODE","HistologicalGradeFinding","Histological grade finding"   ),
        ("CODE","MalignancyType","Malignancy Type"),
        ("CODE","TumorMarginStatus","Tumor margin status"),
        ("CODE","PerineuralInvasionFinding","Perineural invasion finding"),
        ("CODE","StatusOfVascularInvasionByTumor","Status of vascular invasion by tumor")),
    "CervicalLymphNodeGroupExcision":(
        ("CODE","CervicalLymphNodeGroup","Cervical lymph node group"),
        ("CODE","Sidedness","Sidedness"),
        ("NUM","NumberOfNodesRemoved","Number of nodes removed"),
        ("NUM","NumberOfNodesPositive","Number of nodes positive"),
        ("CODE","StatusOfExtraCapsularExtensionOfNodalTumor", "Status of extra­capsular extension of nodal tumor"),
        ("TEXT","Comment","Comment")),
    "DiseaseOutcome":(
        ("DATE","FollowupVisitDate","Follow-up visit date"),
        ("CODE","FollowupStatus","Followup status"),
        ("DATE","Date of death"),
        ("CODE","Cause of death"),
        ("CODE","Post-radiotherapy treatment"),
        ("DATE","Date of cancer recurrence"),
        ("CODE","Location of first recurrence")),
    "RecurrentPathology":(
        ("CODE", "Pathology", "Pathology"),
        ("CODE", "HistologicalGradeFinding", "Histological grade finding"),
        ("CODE", "MalignancyType", "Malignancy Type"),
        ("CODE", "TumorMarginStatus", "Tumor margin status"),
        ("CODE", "PerineuralInvasionFinding", "Perineural invasion finding"),
        ("CODE", "StatusOfVascularInvasionByTumor", "Status of vascular invasion by tumor"))
}
