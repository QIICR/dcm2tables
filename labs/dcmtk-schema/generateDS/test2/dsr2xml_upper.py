#!/usr/bin/env python

#
# Generated Wed Jul 17 14:30:35 2019 by generateDS.py version 2.33.1.
# Python 3.6.3 (default, Jan  8 2019, 21:58:05)  [GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)]
#
# Command line options:
#   ('-f', '')
#   ('-o', 'dsr2xml_api.py')
#   ('-s', 'dsr2xml_upper.py')
#   ('--super', 'dsr2xml_api')
#   ('--member-specs', 'list')
#
# Command line arguments:
#   ../../dsr2xml.xsd
#
# Command line:
#   /Users/fedorov/.pyenv/versions/3.6.3/bin/generateDS -f -o "dsr2xml_api.py" -s "dsr2xml_upper.py" --super="dsr2xml_api" --member-specs="list" ../../dsr2xml.xsd
#
# Current working directory (os.getcwd()):
#   attempt2
#

import os
import sys
from lxml import etree as etree_

import dsr2xml_api as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = ''

#
# Data representation classes
#


class ReportSub(supermod.Report):
    def __init__(self, type_=None, sopclass=None, charset=None, timezone=None, modality=None, manufacturer=None, device=None, synchronization=None, referringphysician=None, patient=None, study=None, series=None, instance=None, coding=None, evidence=None, reference=None, document=None, **kwargs_):
        super(ReportSub, self).__init__(type_, sopclass, charset, timezone, modality, manufacturer, device, synchronization, referringphysician, patient, study, series, instance, coding, evidence, reference, document,  **kwargs_)
supermod.Report.subclass = ReportSub
# end class ReportSub


class SOPClassSub(supermod.SOPClass):
    def __init__(self, uid=None, valueOf_=None, **kwargs_):
        super(SOPClassSub, self).__init__(uid, valueOf_,  **kwargs_)
supermod.SOPClass.subclass = SOPClassSub
# end class SOPClassSub


class DeviceSub(supermod.Device):
    def __init__(self, manufacturer=None, model=None, serial=None, version=None, **kwargs_):
        super(DeviceSub, self).__init__(manufacturer, model, serial, version,  **kwargs_)
supermod.Device.subclass = DeviceSub
# end class DeviceSub


class SynchronizationSub(supermod.Synchronization):
    def __init__(self, uid=None, trigger=None, acquisitiontime=None, **kwargs_):
        super(SynchronizationSub, self).__init__(uid, trigger, acquisitiontime,  **kwargs_)
supermod.Synchronization.subclass = SynchronizationSub
# end class SynchronizationSub


class ReferringPhysicianSub(supermod.ReferringPhysician):
    def __init__(self, name=None, **kwargs_):
        super(ReferringPhysicianSub, self).__init__(name,  **kwargs_)
supermod.ReferringPhysician.subclass = ReferringPhysicianSub
# end class ReferringPhysicianSub


class PatientSub(supermod.Patient):
    def __init__(self, id=None, issuer=None, name=None, birthday=None, sex=None, **kwargs_):
        super(PatientSub, self).__init__(id, issuer, name, birthday, sex,  **kwargs_)
supermod.Patient.subclass = PatientSub
# end class PatientSub


class StudySub(supermod.Study):
    def __init__(self, uid=None, id=None, date=None, time=None, accession=None, description=None, **kwargs_):
        super(StudySub, self).__init__(uid, id, date, time, accession, description,  **kwargs_)
supermod.Study.subclass = StudySub
# end class StudySub


class SeriesSub(supermod.Series):
    def __init__(self, uid=None, number=None, date=None, time=None, protocol=None, description=None, **kwargs_):
        super(SeriesSub, self).__init__(uid, number, date, time, protocol, description,  **kwargs_)
supermod.Series.subclass = SeriesSub
# end class SeriesSub


class InstanceSub(supermod.Instance):
    def __init__(self, uid=None, number=None, creation=None, **kwargs_):
        super(InstanceSub, self).__init__(uid, number, creation,  **kwargs_)
supermod.Instance.subclass = InstanceSub
# end class InstanceSub


class CodingSub(supermod.Coding):
    def __init__(self, scheme=None, **kwargs_):
        super(CodingSub, self).__init__(scheme,  **kwargs_)
supermod.Coding.subclass = CodingSub
# end class CodingSub


class EvidenceSub(supermod.Evidence):
    def __init__(self, type_=None, study=None, **kwargs_):
        super(EvidenceSub, self).__init__(type_, study,  **kwargs_)
supermod.Evidence.subclass = EvidenceSub
# end class EvidenceSub


class ReferenceSub(supermod.Reference):
    def __init__(self, value=None, **kwargs_):
        super(ReferenceSub, self).__init__(value,  **kwargs_)
supermod.Reference.subclass = ReferenceSub
# end class ReferenceSub


class DocumentSub(supermod.Document):
    def __init__(self, preliminary=None, completion=None, verification=None, predecessor=None, identical=None, content=None, **kwargs_):
        super(DocumentSub, self).__init__(preliminary, completion, verification, predecessor, identical, content,  **kwargs_)
supermod.Document.subclass = DocumentSub
# end class DocumentSub


class ContentSub(supermod.Content):
    def __init__(self, date=None, time=None, container=None, **kwargs_):
        super(ContentSub, self).__init__(date, time, container,  **kwargs_)
supermod.Content.subclass = ContentSub
# end class ContentSub


class ReferencedSOPInstancesSub(supermod.ReferencedSOPInstances):
    def __init__(self, study=None, **kwargs_):
        super(ReferencedSOPInstancesSub, self).__init__(study,  **kwargs_)
supermod.ReferencedSOPInstances.subclass = ReferencedSOPInstancesSub
# end class ReferencedSOPInstancesSub


class CodeSub(supermod.Code):
    def __init__(self, value=None, scheme=None, meaning=None, **kwargs_):
        super(CodeSub, self).__init__(value, scheme, meaning,  **kwargs_)
supermod.Code.subclass = CodeSub
# end class CodeSub


class TemplateSub(supermod.Template):
    def __init__(self, resource=None, id=None, **kwargs_):
        super(TemplateSub, self).__init__(resource, id,  **kwargs_)
supermod.Template.subclass = TemplateSub
# end class TemplateSub


class ObservationSub(supermod.Observation):
    def __init__(self, uid=None, datetime=None, **kwargs_):
        super(ObservationSub, self).__init__(uid, datetime,  **kwargs_)
supermod.Observation.subclass = ObservationSub
# end class ObservationSub


class ReferencedSOPSub(supermod.ReferencedSOP):
    def __init__(self, sopclass=None, instance=None, extensiontype_=None, **kwargs_):
        super(ReferencedSOPSub, self).__init__(sopclass, instance, extensiontype_,  **kwargs_)
supermod.ReferencedSOP.subclass = ReferencedSOPSub
# end class ReferencedSOPSub


class MappingResourceSub(supermod.MappingResource):
    def __init__(self, uid=None, valueOf_=None, **kwargs_):
        super(MappingResourceSub, self).__init__(uid, valueOf_,  **kwargs_)
supermod.MappingResource.subclass = MappingResourceSub
# end class MappingResourceSub


class PersonNameSub(supermod.PersonName):
    def __init__(self, prefix=None, first=None, middle=None, last=None, suffix=None, **kwargs_):
        super(PersonNameSub, self).__init__(prefix, first, middle, last, suffix,  **kwargs_)
supermod.PersonName.subclass = PersonNameSub
# end class PersonNameSub


class birthdayTypeSub(supermod.birthdayType):
    def __init__(self, date=None, **kwargs_):
        super(birthdayTypeSub, self).__init__(date,  **kwargs_)
supermod.birthdayType.subclass = birthdayTypeSub
# end class birthdayTypeSub


class accessionTypeSub(supermod.accessionType):
    def __init__(self, number=None, **kwargs_):
        super(accessionTypeSub, self).__init__(number,  **kwargs_)
supermod.accessionType.subclass = accessionTypeSub
# end class accessionTypeSub


class creationTypeSub(supermod.creationType):
    def __init__(self, uid=None, date=None, time=None, **kwargs_):
        super(creationTypeSub, self).__init__(uid, date, time,  **kwargs_)
supermod.creationType.subclass = creationTypeSub
# end class creationTypeSub


class schemeTypeSub(supermod.schemeType):
    def __init__(self, designator=None, registry=None, uid=None, id=None, name=None, version=None, organization=None, **kwargs_):
        super(schemeTypeSub, self).__init__(designator, registry, uid, id, name, version, organization,  **kwargs_)
supermod.schemeType.subclass = schemeTypeSub
# end class schemeTypeSub


class studyTypeSub(supermod.studyType):
    def __init__(self, uid=None, series=None, **kwargs_):
        super(studyTypeSub, self).__init__(uid, series,  **kwargs_)
supermod.studyType.subclass = studyTypeSub
# end class studyTypeSub


class seriesTypeSub(supermod.seriesType):
    def __init__(self, uid=None, aetitle=None, location=None, fileset=None, value=None, **kwargs_):
        super(seriesTypeSub, self).__init__(uid, aetitle, location, fileset, value,  **kwargs_)
supermod.seriesType.subclass = seriesTypeSub
# end class seriesTypeSub


class locationTypeSub(supermod.locationType):
    def __init__(self, uid=None, **kwargs_):
        super(locationTypeSub, self).__init__(uid,  **kwargs_)
supermod.locationType.subclass = locationTypeSub
# end class locationTypeSub


class filesetTypeSub(supermod.filesetType):
    def __init__(self, uid=None, valueOf_=None, **kwargs_):
        super(filesetTypeSub, self).__init__(uid, valueOf_,  **kwargs_)
supermod.filesetType.subclass = filesetTypeSub
# end class filesetTypeSub


class valueTypeSub(supermod.valueType):
    def __init__(self, sopclass=None, instance=None, purpose=None, **kwargs_):
        super(valueTypeSub, self).__init__(sopclass, instance, purpose,  **kwargs_)
supermod.valueType.subclass = valueTypeSub
# end class valueTypeSub


class valueType1Sub(supermod.valueType1):
    def __init__(self, sopclass=None, instance=None, purpose=None, **kwargs_):
        super(valueType1Sub, self).__init__(sopclass, instance, purpose,  **kwargs_)
supermod.valueType1.subclass = valueType1Sub
# end class valueType1Sub


class preliminaryTypeSub(supermod.preliminaryType):
    def __init__(self, flag=None, **kwargs_):
        super(preliminaryTypeSub, self).__init__(flag,  **kwargs_)
supermod.preliminaryType.subclass = preliminaryTypeSub
# end class preliminaryTypeSub


class completionTypeSub(supermod.completionType):
    def __init__(self, flag=None, description=None, **kwargs_):
        super(completionTypeSub, self).__init__(flag, description,  **kwargs_)
supermod.completionType.subclass = completionTypeSub
# end class completionTypeSub


class verificationTypeSub(supermod.verificationType):
    def __init__(self, flag=None, observer=None, **kwargs_):
        super(verificationTypeSub, self).__init__(flag, observer,  **kwargs_)
supermod.verificationType.subclass = verificationTypeSub
# end class verificationTypeSub


class observerTypeSub(supermod.observerType):
    def __init__(self, pos=None, datetime=None, name=None, code=None, organization=None, **kwargs_):
        super(observerTypeSub, self).__init__(pos, datetime, name, code, organization,  **kwargs_)
supermod.observerType.subclass = observerTypeSub
# end class observerTypeSub


class containerTypeSub(supermod.containerType):
    def __init__(self, id=None, flag=None, template=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, **kwargs_):
        super(containerTypeSub, self).__init__(id, flag, template, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference,  **kwargs_)
supermod.containerType.subclass = containerTypeSub
# end class containerTypeSub


class studyType2Sub(supermod.studyType2):
    def __init__(self, uid=None, series=None, **kwargs_):
        super(studyType2Sub, self).__init__(uid, series,  **kwargs_)
supermod.studyType2.subclass = studyType2Sub
# end class studyType2Sub


class seriesType3Sub(supermod.seriesType3):
    def __init__(self, uid=None, aetitle=None, location=None, fileset=None, value=None, **kwargs_):
        super(seriesType3Sub, self).__init__(uid, aetitle, location, fileset, value,  **kwargs_)
supermod.seriesType3.subclass = seriesType3Sub
# end class seriesType3Sub


class locationType4Sub(supermod.locationType4):
    def __init__(self, uid=None, **kwargs_):
        super(locationType4Sub, self).__init__(uid,  **kwargs_)
supermod.locationType4.subclass = locationType4Sub
# end class locationType4Sub


class filesetType5Sub(supermod.filesetType5):
    def __init__(self, uid=None, valueOf_=None, **kwargs_):
        super(filesetType5Sub, self).__init__(uid, valueOf_,  **kwargs_)
supermod.filesetType5.subclass = filesetType5Sub
# end class filesetType5Sub


class valueType6Sub(supermod.valueType6):
    def __init__(self, sopclass=None, instance=None, purpose=None, **kwargs_):
        super(valueType6Sub, self).__init__(sopclass, instance, purpose,  **kwargs_)
supermod.valueType6.subclass = valueType6Sub
# end class valueType6Sub


class schemeType7Sub(supermod.schemeType7):
    def __init__(self, designator=None, version=None, **kwargs_):
        super(schemeType7Sub, self).__init__(designator, version,  **kwargs_)
supermod.schemeType7.subclass = schemeType7Sub
# end class schemeType7Sub


class instanceTypeSub(supermod.instanceType):
    def __init__(self, uid=None, **kwargs_):
        super(instanceTypeSub, self).__init__(uid,  **kwargs_)
supermod.instanceType.subclass = instanceTypeSub
# end class instanceTypeSub


class schemeType8Sub(supermod.schemeType8):
    def __init__(self, designator=None, version=None, **kwargs_):
        super(schemeType8Sub, self).__init__(designator, version,  **kwargs_)
supermod.schemeType8.subclass = schemeType8Sub
# end class schemeType8Sub


class rationalTypeSub(supermod.rationalType):
    def __init__(self, numerator=None, denominator=None, **kwargs_):
        super(rationalTypeSub, self).__init__(numerator, denominator,  **kwargs_)
supermod.rationalType.subclass = rationalTypeSub
# end class rationalTypeSub


class studyType9Sub(supermod.studyType9):
    def __init__(self, uid=None, series=None, **kwargs_):
        super(studyType9Sub, self).__init__(uid, series,  **kwargs_)
supermod.studyType9.subclass = studyType9Sub
# end class studyType9Sub


class seriesType10Sub(supermod.seriesType10):
    def __init__(self, uid=None, aetitle=None, location=None, fileset=None, value=None, **kwargs_):
        super(seriesType10Sub, self).__init__(uid, aetitle, location, fileset, value,  **kwargs_)
supermod.seriesType10.subclass = seriesType10Sub
# end class seriesType10Sub


class locationType11Sub(supermod.locationType11):
    def __init__(self, uid=None, **kwargs_):
        super(locationType11Sub, self).__init__(uid,  **kwargs_)
supermod.locationType11.subclass = locationType11Sub
# end class locationType11Sub


class filesetType12Sub(supermod.filesetType12):
    def __init__(self, uid=None, valueOf_=None, **kwargs_):
        super(filesetType12Sub, self).__init__(uid, valueOf_,  **kwargs_)
supermod.filesetType12.subclass = filesetType12Sub
# end class filesetType12Sub


class valueType13Sub(supermod.valueType13):
    def __init__(self, sopclass=None, instance=None, purpose=None, **kwargs_):
        super(valueType13Sub, self).__init__(sopclass, instance, purpose,  **kwargs_)
supermod.valueType13.subclass = valueType13Sub
# end class valueType13Sub


class textTypeSub(supermod.textType):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(textTypeSub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.textType.subclass = textTypeSub
# end class textTypeSub


class codeTypeSub(supermod.codeType):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, scheme=None, meaning=None, **kwargs_):
        super(codeTypeSub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, scheme, meaning,  **kwargs_)
supermod.codeType.subclass = codeTypeSub
# end class codeTypeSub


class numTypeSub(supermod.numType):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, float_=None, rational=None, unit=None, qualifier=None, **kwargs_):
        super(numTypeSub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, float_, rational, unit, qualifier,  **kwargs_)
supermod.numType.subclass = numTypeSub
# end class numTypeSub


class datetimeTypeSub(supermod.datetimeType):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(datetimeTypeSub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.datetimeType.subclass = datetimeTypeSub
# end class datetimeTypeSub


class dateTypeSub(supermod.dateType):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(dateTypeSub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.dateType.subclass = dateTypeSub
# end class dateTypeSub


class timeTypeSub(supermod.timeType):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(timeTypeSub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.timeType.subclass = timeTypeSub
# end class timeTypeSub


class uidrefTypeSub(supermod.uidrefType):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(uidrefTypeSub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.uidrefType.subclass = uidrefTypeSub
# end class uidrefTypeSub


class pnameTypeSub(supermod.pnameType):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(pnameTypeSub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.pnameType.subclass = pnameTypeSub
# end class pnameTypeSub


class scoordTypeSub(supermod.scoordType):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoordTypeSub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoordType.subclass = scoordTypeSub
# end class scoordTypeSub


class fiducialTypeSub(supermod.fiducialType):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialTypeSub, self).__init__(uid,  **kwargs_)
supermod.fiducialType.subclass = fiducialTypeSub
# end class fiducialTypeSub


class scoord3dTypeSub(supermod.scoord3dType):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoord3dTypeSub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoord3dType.subclass = scoord3dTypeSub
# end class scoord3dTypeSub


class dataTypeSub(supermod.dataType):
    def __init__(self, uid=None, valueOf_=None, **kwargs_):
        super(dataTypeSub, self).__init__(uid, valueOf_,  **kwargs_)
supermod.dataType.subclass = dataTypeSub
# end class dataTypeSub


class fiducialType14Sub(supermod.fiducialType14):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType14Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType14.subclass = fiducialType14Sub
# end class fiducialType14Sub


class tcoordTypeSub(supermod.tcoordType):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, **kwargs_):
        super(tcoordTypeSub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data,  **kwargs_)
supermod.tcoordType.subclass = tcoordTypeSub
# end class tcoordTypeSub


class dataType15Sub(supermod.dataType15):
    def __init__(self, type_=None, valueOf_=None, **kwargs_):
        super(dataType15Sub, self).__init__(type_, valueOf_,  **kwargs_)
supermod.dataType15.subclass = dataType15Sub
# end class dataType15Sub


class compositeTypeSub(supermod.compositeType):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(compositeTypeSub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.compositeType.subclass = compositeTypeSub
# end class compositeTypeSub


class imageTypeSub(supermod.imageType):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(imageTypeSub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.imageType.subclass = imageTypeSub
# end class imageTypeSub


class valueType16Sub(supermod.valueType16):
    def __init__(self, sopclass=None, instance=None, frames=None, segments=None, pstate=None, mapping=None, **kwargs_):
        super(valueType16Sub, self).__init__(sopclass, instance, frames, segments, pstate, mapping,  **kwargs_)
supermod.valueType16.subclass = valueType16Sub
# end class valueType16Sub


class waveformTypeSub(supermod.waveformType):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(waveformTypeSub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.waveformType.subclass = waveformTypeSub
# end class waveformTypeSub


class valueType17Sub(supermod.valueType17):
    def __init__(self, sopclass=None, instance=None, channels=None, **kwargs_):
        super(valueType17Sub, self).__init__(sopclass, instance, channels,  **kwargs_)
supermod.valueType17.subclass = valueType17Sub
# end class valueType17Sub


class containerType18Sub(supermod.containerType18):
    def __init__(self, flag=None, id=None, template=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, **kwargs_):
        super(containerType18Sub, self).__init__(flag, id, template, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference,  **kwargs_)
supermod.containerType18.subclass = containerType18Sub
# end class containerType18Sub


class referenceTypeSub(supermod.referenceType):
    def __init__(self, id=None, ref=None, relationship=None, **kwargs_):
        super(referenceTypeSub, self).__init__(id, ref, relationship,  **kwargs_)
supermod.referenceType.subclass = referenceTypeSub
# end class referenceTypeSub


class textType19Sub(supermod.textType19):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(textType19Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.textType19.subclass = textType19Sub
# end class textType19Sub


class textType20Sub(supermod.textType20):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(textType20Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.textType20.subclass = textType20Sub
# end class textType20Sub


class codeType21Sub(supermod.codeType21):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, scheme=None, meaning=None, **kwargs_):
        super(codeType21Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, scheme, meaning,  **kwargs_)
supermod.codeType21.subclass = codeType21Sub
# end class codeType21Sub


class numType22Sub(supermod.numType22):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, float_=None, rational=None, unit=None, qualifier=None, **kwargs_):
        super(numType22Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, float_, rational, unit, qualifier,  **kwargs_)
supermod.numType22.subclass = numType22Sub
# end class numType22Sub


class datetimeType23Sub(supermod.datetimeType23):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(datetimeType23Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.datetimeType23.subclass = datetimeType23Sub
# end class datetimeType23Sub


class dateType24Sub(supermod.dateType24):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(dateType24Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.dateType24.subclass = dateType24Sub
# end class dateType24Sub


class timeType25Sub(supermod.timeType25):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(timeType25Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.timeType25.subclass = timeType25Sub
# end class timeType25Sub


class uidrefType26Sub(supermod.uidrefType26):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(uidrefType26Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.uidrefType26.subclass = uidrefType26Sub
# end class uidrefType26Sub


class pnameType27Sub(supermod.pnameType27):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(pnameType27Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.pnameType27.subclass = pnameType27Sub
# end class pnameType27Sub


class scoordType28Sub(supermod.scoordType28):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoordType28Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoordType28.subclass = scoordType28Sub
# end class scoordType28Sub


class fiducialType29Sub(supermod.fiducialType29):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType29Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType29.subclass = fiducialType29Sub
# end class fiducialType29Sub


class scoord3dType30Sub(supermod.scoord3dType30):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoord3dType30Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoord3dType30.subclass = scoord3dType30Sub
# end class scoord3dType30Sub


class dataType31Sub(supermod.dataType31):
    def __init__(self, uid=None, valueOf_=None, **kwargs_):
        super(dataType31Sub, self).__init__(uid, valueOf_,  **kwargs_)
supermod.dataType31.subclass = dataType31Sub
# end class dataType31Sub


class fiducialType32Sub(supermod.fiducialType32):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType32Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType32.subclass = fiducialType32Sub
# end class fiducialType32Sub


class tcoordType33Sub(supermod.tcoordType33):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, **kwargs_):
        super(tcoordType33Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data,  **kwargs_)
supermod.tcoordType33.subclass = tcoordType33Sub
# end class tcoordType33Sub


class dataType34Sub(supermod.dataType34):
    def __init__(self, type_=None, valueOf_=None, **kwargs_):
        super(dataType34Sub, self).__init__(type_, valueOf_,  **kwargs_)
supermod.dataType34.subclass = dataType34Sub
# end class dataType34Sub


class compositeType35Sub(supermod.compositeType35):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(compositeType35Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.compositeType35.subclass = compositeType35Sub
# end class compositeType35Sub


class imageType36Sub(supermod.imageType36):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(imageType36Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.imageType36.subclass = imageType36Sub
# end class imageType36Sub


class valueType37Sub(supermod.valueType37):
    def __init__(self, sopclass=None, instance=None, frames=None, segments=None, pstate=None, mapping=None, **kwargs_):
        super(valueType37Sub, self).__init__(sopclass, instance, frames, segments, pstate, mapping,  **kwargs_)
supermod.valueType37.subclass = valueType37Sub
# end class valueType37Sub


class waveformType38Sub(supermod.waveformType38):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(waveformType38Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.waveformType38.subclass = waveformType38Sub
# end class waveformType38Sub


class valueType39Sub(supermod.valueType39):
    def __init__(self, sopclass=None, instance=None, channels=None, **kwargs_):
        super(valueType39Sub, self).__init__(sopclass, instance, channels,  **kwargs_)
supermod.valueType39.subclass = valueType39Sub
# end class valueType39Sub


class containerType40Sub(supermod.containerType40):
    def __init__(self, flag=None, id=None, template=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, **kwargs_):
        super(containerType40Sub, self).__init__(flag, id, template, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference,  **kwargs_)
supermod.containerType40.subclass = containerType40Sub
# end class containerType40Sub


class referenceType41Sub(supermod.referenceType41):
    def __init__(self, id=None, ref=None, relationship=None, **kwargs_):
        super(referenceType41Sub, self).__init__(id, ref, relationship,  **kwargs_)
supermod.referenceType41.subclass = referenceType41Sub
# end class referenceType41Sub


class codeType42Sub(supermod.codeType42):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, scheme=None, meaning=None, **kwargs_):
        super(codeType42Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, scheme, meaning,  **kwargs_)
supermod.codeType42.subclass = codeType42Sub
# end class codeType42Sub


class textType43Sub(supermod.textType43):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(textType43Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.textType43.subclass = textType43Sub
# end class textType43Sub


class codeType44Sub(supermod.codeType44):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, scheme=None, meaning=None, **kwargs_):
        super(codeType44Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, scheme, meaning,  **kwargs_)
supermod.codeType44.subclass = codeType44Sub
# end class codeType44Sub


class numType45Sub(supermod.numType45):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, float_=None, rational=None, unit=None, qualifier=None, **kwargs_):
        super(numType45Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, float_, rational, unit, qualifier,  **kwargs_)
supermod.numType45.subclass = numType45Sub
# end class numType45Sub


class datetimeType46Sub(supermod.datetimeType46):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(datetimeType46Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.datetimeType46.subclass = datetimeType46Sub
# end class datetimeType46Sub


class dateType47Sub(supermod.dateType47):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(dateType47Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.dateType47.subclass = dateType47Sub
# end class dateType47Sub


class timeType48Sub(supermod.timeType48):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(timeType48Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.timeType48.subclass = timeType48Sub
# end class timeType48Sub


class uidrefType49Sub(supermod.uidrefType49):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(uidrefType49Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.uidrefType49.subclass = uidrefType49Sub
# end class uidrefType49Sub


class pnameType50Sub(supermod.pnameType50):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(pnameType50Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.pnameType50.subclass = pnameType50Sub
# end class pnameType50Sub


class scoordType51Sub(supermod.scoordType51):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoordType51Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoordType51.subclass = scoordType51Sub
# end class scoordType51Sub


class fiducialType52Sub(supermod.fiducialType52):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType52Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType52.subclass = fiducialType52Sub
# end class fiducialType52Sub


class scoord3dType53Sub(supermod.scoord3dType53):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoord3dType53Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoord3dType53.subclass = scoord3dType53Sub
# end class scoord3dType53Sub


class dataType54Sub(supermod.dataType54):
    def __init__(self, uid=None, valueOf_=None, **kwargs_):
        super(dataType54Sub, self).__init__(uid, valueOf_,  **kwargs_)
supermod.dataType54.subclass = dataType54Sub
# end class dataType54Sub


class fiducialType55Sub(supermod.fiducialType55):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType55Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType55.subclass = fiducialType55Sub
# end class fiducialType55Sub


class tcoordType56Sub(supermod.tcoordType56):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, **kwargs_):
        super(tcoordType56Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data,  **kwargs_)
supermod.tcoordType56.subclass = tcoordType56Sub
# end class tcoordType56Sub


class dataType57Sub(supermod.dataType57):
    def __init__(self, type_=None, valueOf_=None, **kwargs_):
        super(dataType57Sub, self).__init__(type_, valueOf_,  **kwargs_)
supermod.dataType57.subclass = dataType57Sub
# end class dataType57Sub


class compositeType58Sub(supermod.compositeType58):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(compositeType58Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.compositeType58.subclass = compositeType58Sub
# end class compositeType58Sub


class imageType59Sub(supermod.imageType59):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(imageType59Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.imageType59.subclass = imageType59Sub
# end class imageType59Sub


class valueType60Sub(supermod.valueType60):
    def __init__(self, sopclass=None, instance=None, frames=None, segments=None, pstate=None, mapping=None, **kwargs_):
        super(valueType60Sub, self).__init__(sopclass, instance, frames, segments, pstate, mapping,  **kwargs_)
supermod.valueType60.subclass = valueType60Sub
# end class valueType60Sub


class waveformType61Sub(supermod.waveformType61):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(waveformType61Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.waveformType61.subclass = waveformType61Sub
# end class waveformType61Sub


class valueType62Sub(supermod.valueType62):
    def __init__(self, sopclass=None, instance=None, channels=None, **kwargs_):
        super(valueType62Sub, self).__init__(sopclass, instance, channels,  **kwargs_)
supermod.valueType62.subclass = valueType62Sub
# end class valueType62Sub


class containerType63Sub(supermod.containerType63):
    def __init__(self, flag=None, id=None, template=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, **kwargs_):
        super(containerType63Sub, self).__init__(flag, id, template, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference,  **kwargs_)
supermod.containerType63.subclass = containerType63Sub
# end class containerType63Sub


class referenceType64Sub(supermod.referenceType64):
    def __init__(self, id=None, ref=None, relationship=None, **kwargs_):
        super(referenceType64Sub, self).__init__(id, ref, relationship,  **kwargs_)
supermod.referenceType64.subclass = referenceType64Sub
# end class referenceType64Sub


class schemeType65Sub(supermod.schemeType65):
    def __init__(self, designator=None, version=None, **kwargs_):
        super(schemeType65Sub, self).__init__(designator, version,  **kwargs_)
supermod.schemeType65.subclass = schemeType65Sub
# end class schemeType65Sub


class numType66Sub(supermod.numType66):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, float_=None, rational=None, unit=None, qualifier=None, **kwargs_):
        super(numType66Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, float_, rational, unit, qualifier,  **kwargs_)
supermod.numType66.subclass = numType66Sub
# end class numType66Sub


class textType67Sub(supermod.textType67):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(textType67Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.textType67.subclass = textType67Sub
# end class textType67Sub


class codeType68Sub(supermod.codeType68):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, scheme=None, meaning=None, **kwargs_):
        super(codeType68Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, scheme, meaning,  **kwargs_)
supermod.codeType68.subclass = codeType68Sub
# end class codeType68Sub


class numType69Sub(supermod.numType69):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, float_=None, rational=None, unit=None, qualifier=None, **kwargs_):
        super(numType69Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, float_, rational, unit, qualifier,  **kwargs_)
supermod.numType69.subclass = numType69Sub
# end class numType69Sub


class datetimeType70Sub(supermod.datetimeType70):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(datetimeType70Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.datetimeType70.subclass = datetimeType70Sub
# end class datetimeType70Sub


class dateType71Sub(supermod.dateType71):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(dateType71Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.dateType71.subclass = dateType71Sub
# end class dateType71Sub


class timeType72Sub(supermod.timeType72):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(timeType72Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.timeType72.subclass = timeType72Sub
# end class timeType72Sub


class uidrefType73Sub(supermod.uidrefType73):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(uidrefType73Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.uidrefType73.subclass = uidrefType73Sub
# end class uidrefType73Sub


class pnameType74Sub(supermod.pnameType74):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(pnameType74Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.pnameType74.subclass = pnameType74Sub
# end class pnameType74Sub


class scoordType75Sub(supermod.scoordType75):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoordType75Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoordType75.subclass = scoordType75Sub
# end class scoordType75Sub


class fiducialType76Sub(supermod.fiducialType76):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType76Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType76.subclass = fiducialType76Sub
# end class fiducialType76Sub


class scoord3dType77Sub(supermod.scoord3dType77):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoord3dType77Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoord3dType77.subclass = scoord3dType77Sub
# end class scoord3dType77Sub


class dataType78Sub(supermod.dataType78):
    def __init__(self, uid=None, valueOf_=None, **kwargs_):
        super(dataType78Sub, self).__init__(uid, valueOf_,  **kwargs_)
supermod.dataType78.subclass = dataType78Sub
# end class dataType78Sub


class fiducialType79Sub(supermod.fiducialType79):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType79Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType79.subclass = fiducialType79Sub
# end class fiducialType79Sub


class tcoordType80Sub(supermod.tcoordType80):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, **kwargs_):
        super(tcoordType80Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data,  **kwargs_)
supermod.tcoordType80.subclass = tcoordType80Sub
# end class tcoordType80Sub


class dataType81Sub(supermod.dataType81):
    def __init__(self, type_=None, valueOf_=None, **kwargs_):
        super(dataType81Sub, self).__init__(type_, valueOf_,  **kwargs_)
supermod.dataType81.subclass = dataType81Sub
# end class dataType81Sub


class compositeType82Sub(supermod.compositeType82):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(compositeType82Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.compositeType82.subclass = compositeType82Sub
# end class compositeType82Sub


class imageType83Sub(supermod.imageType83):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(imageType83Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.imageType83.subclass = imageType83Sub
# end class imageType83Sub


class valueType84Sub(supermod.valueType84):
    def __init__(self, sopclass=None, instance=None, frames=None, segments=None, pstate=None, mapping=None, **kwargs_):
        super(valueType84Sub, self).__init__(sopclass, instance, frames, segments, pstate, mapping,  **kwargs_)
supermod.valueType84.subclass = valueType84Sub
# end class valueType84Sub


class waveformType85Sub(supermod.waveformType85):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(waveformType85Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.waveformType85.subclass = waveformType85Sub
# end class waveformType85Sub


class valueType86Sub(supermod.valueType86):
    def __init__(self, sopclass=None, instance=None, channels=None, **kwargs_):
        super(valueType86Sub, self).__init__(sopclass, instance, channels,  **kwargs_)
supermod.valueType86.subclass = valueType86Sub
# end class valueType86Sub


class containerType87Sub(supermod.containerType87):
    def __init__(self, flag=None, id=None, template=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, **kwargs_):
        super(containerType87Sub, self).__init__(flag, id, template, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference,  **kwargs_)
supermod.containerType87.subclass = containerType87Sub
# end class containerType87Sub


class referenceType88Sub(supermod.referenceType88):
    def __init__(self, id=None, ref=None, relationship=None, **kwargs_):
        super(referenceType88Sub, self).__init__(id, ref, relationship,  **kwargs_)
supermod.referenceType88.subclass = referenceType88Sub
# end class referenceType88Sub


class rationalType89Sub(supermod.rationalType89):
    def __init__(self, numerator=None, denominator=None, **kwargs_):
        super(rationalType89Sub, self).__init__(numerator, denominator,  **kwargs_)
supermod.rationalType89.subclass = rationalType89Sub
# end class rationalType89Sub


class datetimeType90Sub(supermod.datetimeType90):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(datetimeType90Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.datetimeType90.subclass = datetimeType90Sub
# end class datetimeType90Sub


class textType91Sub(supermod.textType91):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(textType91Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.textType91.subclass = textType91Sub
# end class textType91Sub


class codeType92Sub(supermod.codeType92):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, scheme=None, meaning=None, **kwargs_):
        super(codeType92Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, scheme, meaning,  **kwargs_)
supermod.codeType92.subclass = codeType92Sub
# end class codeType92Sub


class numType93Sub(supermod.numType93):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, float_=None, rational=None, unit=None, qualifier=None, **kwargs_):
        super(numType93Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, float_, rational, unit, qualifier,  **kwargs_)
supermod.numType93.subclass = numType93Sub
# end class numType93Sub


class datetimeType94Sub(supermod.datetimeType94):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(datetimeType94Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.datetimeType94.subclass = datetimeType94Sub
# end class datetimeType94Sub


class dateType95Sub(supermod.dateType95):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(dateType95Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.dateType95.subclass = dateType95Sub
# end class dateType95Sub


class timeType96Sub(supermod.timeType96):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(timeType96Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.timeType96.subclass = timeType96Sub
# end class timeType96Sub


class uidrefType97Sub(supermod.uidrefType97):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(uidrefType97Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.uidrefType97.subclass = uidrefType97Sub
# end class uidrefType97Sub


class pnameType98Sub(supermod.pnameType98):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(pnameType98Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.pnameType98.subclass = pnameType98Sub
# end class pnameType98Sub


class scoordType99Sub(supermod.scoordType99):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoordType99Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoordType99.subclass = scoordType99Sub
# end class scoordType99Sub


class fiducialType100Sub(supermod.fiducialType100):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType100Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType100.subclass = fiducialType100Sub
# end class fiducialType100Sub


class scoord3dType101Sub(supermod.scoord3dType101):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoord3dType101Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoord3dType101.subclass = scoord3dType101Sub
# end class scoord3dType101Sub


class dataType102Sub(supermod.dataType102):
    def __init__(self, uid=None, valueOf_=None, **kwargs_):
        super(dataType102Sub, self).__init__(uid, valueOf_,  **kwargs_)
supermod.dataType102.subclass = dataType102Sub
# end class dataType102Sub


class fiducialType103Sub(supermod.fiducialType103):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType103Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType103.subclass = fiducialType103Sub
# end class fiducialType103Sub


class tcoordType104Sub(supermod.tcoordType104):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, **kwargs_):
        super(tcoordType104Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data,  **kwargs_)
supermod.tcoordType104.subclass = tcoordType104Sub
# end class tcoordType104Sub


class dataType105Sub(supermod.dataType105):
    def __init__(self, type_=None, valueOf_=None, **kwargs_):
        super(dataType105Sub, self).__init__(type_, valueOf_,  **kwargs_)
supermod.dataType105.subclass = dataType105Sub
# end class dataType105Sub


class compositeType106Sub(supermod.compositeType106):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(compositeType106Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.compositeType106.subclass = compositeType106Sub
# end class compositeType106Sub


class imageType107Sub(supermod.imageType107):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(imageType107Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.imageType107.subclass = imageType107Sub
# end class imageType107Sub


class valueType108Sub(supermod.valueType108):
    def __init__(self, sopclass=None, instance=None, frames=None, segments=None, pstate=None, mapping=None, **kwargs_):
        super(valueType108Sub, self).__init__(sopclass, instance, frames, segments, pstate, mapping,  **kwargs_)
supermod.valueType108.subclass = valueType108Sub
# end class valueType108Sub


class waveformType109Sub(supermod.waveformType109):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(waveformType109Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.waveformType109.subclass = waveformType109Sub
# end class waveformType109Sub


class valueType110Sub(supermod.valueType110):
    def __init__(self, sopclass=None, instance=None, channels=None, **kwargs_):
        super(valueType110Sub, self).__init__(sopclass, instance, channels,  **kwargs_)
supermod.valueType110.subclass = valueType110Sub
# end class valueType110Sub


class containerType111Sub(supermod.containerType111):
    def __init__(self, flag=None, id=None, template=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, **kwargs_):
        super(containerType111Sub, self).__init__(flag, id, template, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference,  **kwargs_)
supermod.containerType111.subclass = containerType111Sub
# end class containerType111Sub


class referenceType112Sub(supermod.referenceType112):
    def __init__(self, id=None, ref=None, relationship=None, **kwargs_):
        super(referenceType112Sub, self).__init__(id, ref, relationship,  **kwargs_)
supermod.referenceType112.subclass = referenceType112Sub
# end class referenceType112Sub


class dateType113Sub(supermod.dateType113):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(dateType113Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.dateType113.subclass = dateType113Sub
# end class dateType113Sub


class textType114Sub(supermod.textType114):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(textType114Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.textType114.subclass = textType114Sub
# end class textType114Sub


class codeType115Sub(supermod.codeType115):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, scheme=None, meaning=None, **kwargs_):
        super(codeType115Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, scheme, meaning,  **kwargs_)
supermod.codeType115.subclass = codeType115Sub
# end class codeType115Sub


class numType116Sub(supermod.numType116):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, float_=None, rational=None, unit=None, qualifier=None, **kwargs_):
        super(numType116Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, float_, rational, unit, qualifier,  **kwargs_)
supermod.numType116.subclass = numType116Sub
# end class numType116Sub


class datetimeType117Sub(supermod.datetimeType117):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(datetimeType117Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.datetimeType117.subclass = datetimeType117Sub
# end class datetimeType117Sub


class dateType118Sub(supermod.dateType118):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(dateType118Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.dateType118.subclass = dateType118Sub
# end class dateType118Sub


class timeType119Sub(supermod.timeType119):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(timeType119Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.timeType119.subclass = timeType119Sub
# end class timeType119Sub


class uidrefType120Sub(supermod.uidrefType120):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(uidrefType120Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.uidrefType120.subclass = uidrefType120Sub
# end class uidrefType120Sub


class pnameType121Sub(supermod.pnameType121):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(pnameType121Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.pnameType121.subclass = pnameType121Sub
# end class pnameType121Sub


class scoordType122Sub(supermod.scoordType122):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoordType122Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoordType122.subclass = scoordType122Sub
# end class scoordType122Sub


class fiducialType123Sub(supermod.fiducialType123):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType123Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType123.subclass = fiducialType123Sub
# end class fiducialType123Sub


class scoord3dType124Sub(supermod.scoord3dType124):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoord3dType124Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoord3dType124.subclass = scoord3dType124Sub
# end class scoord3dType124Sub


class dataType125Sub(supermod.dataType125):
    def __init__(self, uid=None, valueOf_=None, **kwargs_):
        super(dataType125Sub, self).__init__(uid, valueOf_,  **kwargs_)
supermod.dataType125.subclass = dataType125Sub
# end class dataType125Sub


class fiducialType126Sub(supermod.fiducialType126):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType126Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType126.subclass = fiducialType126Sub
# end class fiducialType126Sub


class tcoordType127Sub(supermod.tcoordType127):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, **kwargs_):
        super(tcoordType127Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data,  **kwargs_)
supermod.tcoordType127.subclass = tcoordType127Sub
# end class tcoordType127Sub


class dataType128Sub(supermod.dataType128):
    def __init__(self, type_=None, valueOf_=None, **kwargs_):
        super(dataType128Sub, self).__init__(type_, valueOf_,  **kwargs_)
supermod.dataType128.subclass = dataType128Sub
# end class dataType128Sub


class compositeType129Sub(supermod.compositeType129):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(compositeType129Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.compositeType129.subclass = compositeType129Sub
# end class compositeType129Sub


class imageType130Sub(supermod.imageType130):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(imageType130Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.imageType130.subclass = imageType130Sub
# end class imageType130Sub


class valueType131Sub(supermod.valueType131):
    def __init__(self, sopclass=None, instance=None, frames=None, segments=None, pstate=None, mapping=None, **kwargs_):
        super(valueType131Sub, self).__init__(sopclass, instance, frames, segments, pstate, mapping,  **kwargs_)
supermod.valueType131.subclass = valueType131Sub
# end class valueType131Sub


class waveformType132Sub(supermod.waveformType132):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(waveformType132Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.waveformType132.subclass = waveformType132Sub
# end class waveformType132Sub


class valueType133Sub(supermod.valueType133):
    def __init__(self, sopclass=None, instance=None, channels=None, **kwargs_):
        super(valueType133Sub, self).__init__(sopclass, instance, channels,  **kwargs_)
supermod.valueType133.subclass = valueType133Sub
# end class valueType133Sub


class containerType134Sub(supermod.containerType134):
    def __init__(self, flag=None, id=None, template=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, **kwargs_):
        super(containerType134Sub, self).__init__(flag, id, template, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference,  **kwargs_)
supermod.containerType134.subclass = containerType134Sub
# end class containerType134Sub


class referenceType135Sub(supermod.referenceType135):
    def __init__(self, id=None, ref=None, relationship=None, **kwargs_):
        super(referenceType135Sub, self).__init__(id, ref, relationship,  **kwargs_)
supermod.referenceType135.subclass = referenceType135Sub
# end class referenceType135Sub


class timeType136Sub(supermod.timeType136):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(timeType136Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.timeType136.subclass = timeType136Sub
# end class timeType136Sub


class textType137Sub(supermod.textType137):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(textType137Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.textType137.subclass = textType137Sub
# end class textType137Sub


class codeType138Sub(supermod.codeType138):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, scheme=None, meaning=None, **kwargs_):
        super(codeType138Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, scheme, meaning,  **kwargs_)
supermod.codeType138.subclass = codeType138Sub
# end class codeType138Sub


class numType139Sub(supermod.numType139):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, float_=None, rational=None, unit=None, qualifier=None, **kwargs_):
        super(numType139Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, float_, rational, unit, qualifier,  **kwargs_)
supermod.numType139.subclass = numType139Sub
# end class numType139Sub


class datetimeType140Sub(supermod.datetimeType140):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(datetimeType140Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.datetimeType140.subclass = datetimeType140Sub
# end class datetimeType140Sub


class dateType141Sub(supermod.dateType141):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(dateType141Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.dateType141.subclass = dateType141Sub
# end class dateType141Sub


class timeType142Sub(supermod.timeType142):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(timeType142Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.timeType142.subclass = timeType142Sub
# end class timeType142Sub


class uidrefType143Sub(supermod.uidrefType143):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(uidrefType143Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.uidrefType143.subclass = uidrefType143Sub
# end class uidrefType143Sub


class pnameType144Sub(supermod.pnameType144):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(pnameType144Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.pnameType144.subclass = pnameType144Sub
# end class pnameType144Sub


class scoordType145Sub(supermod.scoordType145):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoordType145Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoordType145.subclass = scoordType145Sub
# end class scoordType145Sub


class fiducialType146Sub(supermod.fiducialType146):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType146Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType146.subclass = fiducialType146Sub
# end class fiducialType146Sub


class scoord3dType147Sub(supermod.scoord3dType147):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoord3dType147Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoord3dType147.subclass = scoord3dType147Sub
# end class scoord3dType147Sub


class dataType148Sub(supermod.dataType148):
    def __init__(self, uid=None, valueOf_=None, **kwargs_):
        super(dataType148Sub, self).__init__(uid, valueOf_,  **kwargs_)
supermod.dataType148.subclass = dataType148Sub
# end class dataType148Sub


class fiducialType149Sub(supermod.fiducialType149):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType149Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType149.subclass = fiducialType149Sub
# end class fiducialType149Sub


class tcoordType150Sub(supermod.tcoordType150):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, **kwargs_):
        super(tcoordType150Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data,  **kwargs_)
supermod.tcoordType150.subclass = tcoordType150Sub
# end class tcoordType150Sub


class dataType151Sub(supermod.dataType151):
    def __init__(self, type_=None, valueOf_=None, **kwargs_):
        super(dataType151Sub, self).__init__(type_, valueOf_,  **kwargs_)
supermod.dataType151.subclass = dataType151Sub
# end class dataType151Sub


class compositeType152Sub(supermod.compositeType152):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(compositeType152Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.compositeType152.subclass = compositeType152Sub
# end class compositeType152Sub


class imageType153Sub(supermod.imageType153):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(imageType153Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.imageType153.subclass = imageType153Sub
# end class imageType153Sub


class valueType154Sub(supermod.valueType154):
    def __init__(self, sopclass=None, instance=None, frames=None, segments=None, pstate=None, mapping=None, **kwargs_):
        super(valueType154Sub, self).__init__(sopclass, instance, frames, segments, pstate, mapping,  **kwargs_)
supermod.valueType154.subclass = valueType154Sub
# end class valueType154Sub


class waveformType155Sub(supermod.waveformType155):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(waveformType155Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.waveformType155.subclass = waveformType155Sub
# end class waveformType155Sub


class valueType156Sub(supermod.valueType156):
    def __init__(self, sopclass=None, instance=None, channels=None, **kwargs_):
        super(valueType156Sub, self).__init__(sopclass, instance, channels,  **kwargs_)
supermod.valueType156.subclass = valueType156Sub
# end class valueType156Sub


class containerType157Sub(supermod.containerType157):
    def __init__(self, flag=None, id=None, template=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, **kwargs_):
        super(containerType157Sub, self).__init__(flag, id, template, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference,  **kwargs_)
supermod.containerType157.subclass = containerType157Sub
# end class containerType157Sub


class referenceType158Sub(supermod.referenceType158):
    def __init__(self, id=None, ref=None, relationship=None, **kwargs_):
        super(referenceType158Sub, self).__init__(id, ref, relationship,  **kwargs_)
supermod.referenceType158.subclass = referenceType158Sub
# end class referenceType158Sub


class uidrefType159Sub(supermod.uidrefType159):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(uidrefType159Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.uidrefType159.subclass = uidrefType159Sub
# end class uidrefType159Sub


class textType160Sub(supermod.textType160):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(textType160Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.textType160.subclass = textType160Sub
# end class textType160Sub


class codeType161Sub(supermod.codeType161):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, scheme=None, meaning=None, **kwargs_):
        super(codeType161Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, scheme, meaning,  **kwargs_)
supermod.codeType161.subclass = codeType161Sub
# end class codeType161Sub


class numType162Sub(supermod.numType162):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, float_=None, rational=None, unit=None, qualifier=None, **kwargs_):
        super(numType162Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, float_, rational, unit, qualifier,  **kwargs_)
supermod.numType162.subclass = numType162Sub
# end class numType162Sub


class datetimeType163Sub(supermod.datetimeType163):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(datetimeType163Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.datetimeType163.subclass = datetimeType163Sub
# end class datetimeType163Sub


class dateType164Sub(supermod.dateType164):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(dateType164Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.dateType164.subclass = dateType164Sub
# end class dateType164Sub


class timeType165Sub(supermod.timeType165):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(timeType165Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.timeType165.subclass = timeType165Sub
# end class timeType165Sub


class uidrefType166Sub(supermod.uidrefType166):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(uidrefType166Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.uidrefType166.subclass = uidrefType166Sub
# end class uidrefType166Sub


class pnameType167Sub(supermod.pnameType167):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(pnameType167Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.pnameType167.subclass = pnameType167Sub
# end class pnameType167Sub


class scoordType168Sub(supermod.scoordType168):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoordType168Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoordType168.subclass = scoordType168Sub
# end class scoordType168Sub


class fiducialType169Sub(supermod.fiducialType169):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType169Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType169.subclass = fiducialType169Sub
# end class fiducialType169Sub


class scoord3dType170Sub(supermod.scoord3dType170):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoord3dType170Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoord3dType170.subclass = scoord3dType170Sub
# end class scoord3dType170Sub


class dataType171Sub(supermod.dataType171):
    def __init__(self, uid=None, valueOf_=None, **kwargs_):
        super(dataType171Sub, self).__init__(uid, valueOf_,  **kwargs_)
supermod.dataType171.subclass = dataType171Sub
# end class dataType171Sub


class fiducialType172Sub(supermod.fiducialType172):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType172Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType172.subclass = fiducialType172Sub
# end class fiducialType172Sub


class tcoordType173Sub(supermod.tcoordType173):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, **kwargs_):
        super(tcoordType173Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data,  **kwargs_)
supermod.tcoordType173.subclass = tcoordType173Sub
# end class tcoordType173Sub


class dataType174Sub(supermod.dataType174):
    def __init__(self, type_=None, valueOf_=None, **kwargs_):
        super(dataType174Sub, self).__init__(type_, valueOf_,  **kwargs_)
supermod.dataType174.subclass = dataType174Sub
# end class dataType174Sub


class compositeType175Sub(supermod.compositeType175):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(compositeType175Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.compositeType175.subclass = compositeType175Sub
# end class compositeType175Sub


class imageType176Sub(supermod.imageType176):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(imageType176Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.imageType176.subclass = imageType176Sub
# end class imageType176Sub


class valueType177Sub(supermod.valueType177):
    def __init__(self, sopclass=None, instance=None, frames=None, segments=None, pstate=None, mapping=None, **kwargs_):
        super(valueType177Sub, self).__init__(sopclass, instance, frames, segments, pstate, mapping,  **kwargs_)
supermod.valueType177.subclass = valueType177Sub
# end class valueType177Sub


class waveformType178Sub(supermod.waveformType178):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(waveformType178Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.waveformType178.subclass = waveformType178Sub
# end class waveformType178Sub


class valueType179Sub(supermod.valueType179):
    def __init__(self, sopclass=None, instance=None, channels=None, **kwargs_):
        super(valueType179Sub, self).__init__(sopclass, instance, channels,  **kwargs_)
supermod.valueType179.subclass = valueType179Sub
# end class valueType179Sub


class containerType180Sub(supermod.containerType180):
    def __init__(self, flag=None, id=None, template=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, **kwargs_):
        super(containerType180Sub, self).__init__(flag, id, template, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference,  **kwargs_)
supermod.containerType180.subclass = containerType180Sub
# end class containerType180Sub


class referenceType181Sub(supermod.referenceType181):
    def __init__(self, id=None, ref=None, relationship=None, **kwargs_):
        super(referenceType181Sub, self).__init__(id, ref, relationship,  **kwargs_)
supermod.referenceType181.subclass = referenceType181Sub
# end class referenceType181Sub


class pnameType182Sub(supermod.pnameType182):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(pnameType182Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.pnameType182.subclass = pnameType182Sub
# end class pnameType182Sub


class textType183Sub(supermod.textType183):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(textType183Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.textType183.subclass = textType183Sub
# end class textType183Sub


class codeType184Sub(supermod.codeType184):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, scheme=None, meaning=None, **kwargs_):
        super(codeType184Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, scheme, meaning,  **kwargs_)
supermod.codeType184.subclass = codeType184Sub
# end class codeType184Sub


class numType185Sub(supermod.numType185):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, float_=None, rational=None, unit=None, qualifier=None, **kwargs_):
        super(numType185Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, float_, rational, unit, qualifier,  **kwargs_)
supermod.numType185.subclass = numType185Sub
# end class numType185Sub


class datetimeType186Sub(supermod.datetimeType186):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(datetimeType186Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.datetimeType186.subclass = datetimeType186Sub
# end class datetimeType186Sub


class dateType187Sub(supermod.dateType187):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(dateType187Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.dateType187.subclass = dateType187Sub
# end class dateType187Sub


class timeType188Sub(supermod.timeType188):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(timeType188Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.timeType188.subclass = timeType188Sub
# end class timeType188Sub


class uidrefType189Sub(supermod.uidrefType189):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(uidrefType189Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.uidrefType189.subclass = uidrefType189Sub
# end class uidrefType189Sub


class pnameType190Sub(supermod.pnameType190):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(pnameType190Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.pnameType190.subclass = pnameType190Sub
# end class pnameType190Sub


class scoordType191Sub(supermod.scoordType191):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoordType191Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoordType191.subclass = scoordType191Sub
# end class scoordType191Sub


class fiducialType192Sub(supermod.fiducialType192):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType192Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType192.subclass = fiducialType192Sub
# end class fiducialType192Sub


class scoord3dType193Sub(supermod.scoord3dType193):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoord3dType193Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoord3dType193.subclass = scoord3dType193Sub
# end class scoord3dType193Sub


class dataType194Sub(supermod.dataType194):
    def __init__(self, uid=None, valueOf_=None, **kwargs_):
        super(dataType194Sub, self).__init__(uid, valueOf_,  **kwargs_)
supermod.dataType194.subclass = dataType194Sub
# end class dataType194Sub


class fiducialType195Sub(supermod.fiducialType195):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType195Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType195.subclass = fiducialType195Sub
# end class fiducialType195Sub


class tcoordType196Sub(supermod.tcoordType196):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, **kwargs_):
        super(tcoordType196Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data,  **kwargs_)
supermod.tcoordType196.subclass = tcoordType196Sub
# end class tcoordType196Sub


class dataType197Sub(supermod.dataType197):
    def __init__(self, type_=None, valueOf_=None, **kwargs_):
        super(dataType197Sub, self).__init__(type_, valueOf_,  **kwargs_)
supermod.dataType197.subclass = dataType197Sub
# end class dataType197Sub


class compositeType198Sub(supermod.compositeType198):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(compositeType198Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.compositeType198.subclass = compositeType198Sub
# end class compositeType198Sub


class imageType199Sub(supermod.imageType199):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(imageType199Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.imageType199.subclass = imageType199Sub
# end class imageType199Sub


class valueType200Sub(supermod.valueType200):
    def __init__(self, sopclass=None, instance=None, frames=None, segments=None, pstate=None, mapping=None, **kwargs_):
        super(valueType200Sub, self).__init__(sopclass, instance, frames, segments, pstate, mapping,  **kwargs_)
supermod.valueType200.subclass = valueType200Sub
# end class valueType200Sub


class waveformType201Sub(supermod.waveformType201):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(waveformType201Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.waveformType201.subclass = waveformType201Sub
# end class waveformType201Sub


class valueType202Sub(supermod.valueType202):
    def __init__(self, sopclass=None, instance=None, channels=None, **kwargs_):
        super(valueType202Sub, self).__init__(sopclass, instance, channels,  **kwargs_)
supermod.valueType202.subclass = valueType202Sub
# end class valueType202Sub


class containerType203Sub(supermod.containerType203):
    def __init__(self, flag=None, id=None, template=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, **kwargs_):
        super(containerType203Sub, self).__init__(flag, id, template, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference,  **kwargs_)
supermod.containerType203.subclass = containerType203Sub
# end class containerType203Sub


class referenceType204Sub(supermod.referenceType204):
    def __init__(self, id=None, ref=None, relationship=None, **kwargs_):
        super(referenceType204Sub, self).__init__(id, ref, relationship,  **kwargs_)
supermod.referenceType204.subclass = referenceType204Sub
# end class referenceType204Sub


class scoordType205Sub(supermod.scoordType205):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoordType205Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoordType205.subclass = scoordType205Sub
# end class scoordType205Sub


class textType206Sub(supermod.textType206):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(textType206Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.textType206.subclass = textType206Sub
# end class textType206Sub


class codeType207Sub(supermod.codeType207):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, scheme=None, meaning=None, **kwargs_):
        super(codeType207Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, scheme, meaning,  **kwargs_)
supermod.codeType207.subclass = codeType207Sub
# end class codeType207Sub


class numType208Sub(supermod.numType208):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, float_=None, rational=None, unit=None, qualifier=None, **kwargs_):
        super(numType208Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, float_, rational, unit, qualifier,  **kwargs_)
supermod.numType208.subclass = numType208Sub
# end class numType208Sub


class datetimeType209Sub(supermod.datetimeType209):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(datetimeType209Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.datetimeType209.subclass = datetimeType209Sub
# end class datetimeType209Sub


class dateType210Sub(supermod.dateType210):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(dateType210Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.dateType210.subclass = dateType210Sub
# end class dateType210Sub


class timeType211Sub(supermod.timeType211):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(timeType211Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.timeType211.subclass = timeType211Sub
# end class timeType211Sub


class uidrefType212Sub(supermod.uidrefType212):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(uidrefType212Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.uidrefType212.subclass = uidrefType212Sub
# end class uidrefType212Sub


class pnameType213Sub(supermod.pnameType213):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(pnameType213Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.pnameType213.subclass = pnameType213Sub
# end class pnameType213Sub


class scoordType214Sub(supermod.scoordType214):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoordType214Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoordType214.subclass = scoordType214Sub
# end class scoordType214Sub


class fiducialType215Sub(supermod.fiducialType215):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType215Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType215.subclass = fiducialType215Sub
# end class fiducialType215Sub


class scoord3dType216Sub(supermod.scoord3dType216):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoord3dType216Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoord3dType216.subclass = scoord3dType216Sub
# end class scoord3dType216Sub


class dataType217Sub(supermod.dataType217):
    def __init__(self, uid=None, valueOf_=None, **kwargs_):
        super(dataType217Sub, self).__init__(uid, valueOf_,  **kwargs_)
supermod.dataType217.subclass = dataType217Sub
# end class dataType217Sub


class fiducialType218Sub(supermod.fiducialType218):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType218Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType218.subclass = fiducialType218Sub
# end class fiducialType218Sub


class tcoordType219Sub(supermod.tcoordType219):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, **kwargs_):
        super(tcoordType219Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data,  **kwargs_)
supermod.tcoordType219.subclass = tcoordType219Sub
# end class tcoordType219Sub


class dataType220Sub(supermod.dataType220):
    def __init__(self, type_=None, valueOf_=None, **kwargs_):
        super(dataType220Sub, self).__init__(type_, valueOf_,  **kwargs_)
supermod.dataType220.subclass = dataType220Sub
# end class dataType220Sub


class compositeType221Sub(supermod.compositeType221):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(compositeType221Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.compositeType221.subclass = compositeType221Sub
# end class compositeType221Sub


class imageType222Sub(supermod.imageType222):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(imageType222Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.imageType222.subclass = imageType222Sub
# end class imageType222Sub


class valueType223Sub(supermod.valueType223):
    def __init__(self, sopclass=None, instance=None, frames=None, segments=None, pstate=None, mapping=None, **kwargs_):
        super(valueType223Sub, self).__init__(sopclass, instance, frames, segments, pstate, mapping,  **kwargs_)
supermod.valueType223.subclass = valueType223Sub
# end class valueType223Sub


class waveformType224Sub(supermod.waveformType224):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(waveformType224Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.waveformType224.subclass = waveformType224Sub
# end class waveformType224Sub


class valueType225Sub(supermod.valueType225):
    def __init__(self, sopclass=None, instance=None, channels=None, **kwargs_):
        super(valueType225Sub, self).__init__(sopclass, instance, channels,  **kwargs_)
supermod.valueType225.subclass = valueType225Sub
# end class valueType225Sub


class containerType226Sub(supermod.containerType226):
    def __init__(self, flag=None, id=None, template=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, **kwargs_):
        super(containerType226Sub, self).__init__(flag, id, template, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference,  **kwargs_)
supermod.containerType226.subclass = containerType226Sub
# end class containerType226Sub


class referenceType227Sub(supermod.referenceType227):
    def __init__(self, id=None, ref=None, relationship=None, **kwargs_):
        super(referenceType227Sub, self).__init__(id, ref, relationship,  **kwargs_)
supermod.referenceType227.subclass = referenceType227Sub
# end class referenceType227Sub


class fiducialType228Sub(supermod.fiducialType228):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType228Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType228.subclass = fiducialType228Sub
# end class fiducialType228Sub


class scoord3dType229Sub(supermod.scoord3dType229):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoord3dType229Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoord3dType229.subclass = scoord3dType229Sub
# end class scoord3dType229Sub


class textType230Sub(supermod.textType230):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(textType230Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.textType230.subclass = textType230Sub
# end class textType230Sub


class codeType231Sub(supermod.codeType231):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, scheme=None, meaning=None, **kwargs_):
        super(codeType231Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, scheme, meaning,  **kwargs_)
supermod.codeType231.subclass = codeType231Sub
# end class codeType231Sub


class numType232Sub(supermod.numType232):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, float_=None, rational=None, unit=None, qualifier=None, **kwargs_):
        super(numType232Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, float_, rational, unit, qualifier,  **kwargs_)
supermod.numType232.subclass = numType232Sub
# end class numType232Sub


class datetimeType233Sub(supermod.datetimeType233):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(datetimeType233Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.datetimeType233.subclass = datetimeType233Sub
# end class datetimeType233Sub


class dateType234Sub(supermod.dateType234):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(dateType234Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.dateType234.subclass = dateType234Sub
# end class dateType234Sub


class timeType235Sub(supermod.timeType235):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(timeType235Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.timeType235.subclass = timeType235Sub
# end class timeType235Sub


class uidrefType236Sub(supermod.uidrefType236):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(uidrefType236Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.uidrefType236.subclass = uidrefType236Sub
# end class uidrefType236Sub


class pnameType237Sub(supermod.pnameType237):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(pnameType237Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.pnameType237.subclass = pnameType237Sub
# end class pnameType237Sub


class scoordType238Sub(supermod.scoordType238):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoordType238Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoordType238.subclass = scoordType238Sub
# end class scoordType238Sub


class fiducialType239Sub(supermod.fiducialType239):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType239Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType239.subclass = fiducialType239Sub
# end class fiducialType239Sub


class scoord3dType240Sub(supermod.scoord3dType240):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoord3dType240Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoord3dType240.subclass = scoord3dType240Sub
# end class scoord3dType240Sub


class dataType241Sub(supermod.dataType241):
    def __init__(self, uid=None, valueOf_=None, **kwargs_):
        super(dataType241Sub, self).__init__(uid, valueOf_,  **kwargs_)
supermod.dataType241.subclass = dataType241Sub
# end class dataType241Sub


class fiducialType242Sub(supermod.fiducialType242):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType242Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType242.subclass = fiducialType242Sub
# end class fiducialType242Sub


class tcoordType243Sub(supermod.tcoordType243):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, **kwargs_):
        super(tcoordType243Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data,  **kwargs_)
supermod.tcoordType243.subclass = tcoordType243Sub
# end class tcoordType243Sub


class dataType244Sub(supermod.dataType244):
    def __init__(self, type_=None, valueOf_=None, **kwargs_):
        super(dataType244Sub, self).__init__(type_, valueOf_,  **kwargs_)
supermod.dataType244.subclass = dataType244Sub
# end class dataType244Sub


class compositeType245Sub(supermod.compositeType245):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(compositeType245Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.compositeType245.subclass = compositeType245Sub
# end class compositeType245Sub


class imageType246Sub(supermod.imageType246):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(imageType246Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.imageType246.subclass = imageType246Sub
# end class imageType246Sub


class valueType247Sub(supermod.valueType247):
    def __init__(self, sopclass=None, instance=None, frames=None, segments=None, pstate=None, mapping=None, **kwargs_):
        super(valueType247Sub, self).__init__(sopclass, instance, frames, segments, pstate, mapping,  **kwargs_)
supermod.valueType247.subclass = valueType247Sub
# end class valueType247Sub


class waveformType248Sub(supermod.waveformType248):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(waveformType248Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.waveformType248.subclass = waveformType248Sub
# end class waveformType248Sub


class valueType249Sub(supermod.valueType249):
    def __init__(self, sopclass=None, instance=None, channels=None, **kwargs_):
        super(valueType249Sub, self).__init__(sopclass, instance, channels,  **kwargs_)
supermod.valueType249.subclass = valueType249Sub
# end class valueType249Sub


class containerType250Sub(supermod.containerType250):
    def __init__(self, flag=None, id=None, template=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, **kwargs_):
        super(containerType250Sub, self).__init__(flag, id, template, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference,  **kwargs_)
supermod.containerType250.subclass = containerType250Sub
# end class containerType250Sub


class referenceType251Sub(supermod.referenceType251):
    def __init__(self, id=None, ref=None, relationship=None, **kwargs_):
        super(referenceType251Sub, self).__init__(id, ref, relationship,  **kwargs_)
supermod.referenceType251.subclass = referenceType251Sub
# end class referenceType251Sub


class dataType252Sub(supermod.dataType252):
    def __init__(self, uid=None, valueOf_=None, **kwargs_):
        super(dataType252Sub, self).__init__(uid, valueOf_,  **kwargs_)
supermod.dataType252.subclass = dataType252Sub
# end class dataType252Sub


class fiducialType253Sub(supermod.fiducialType253):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType253Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType253.subclass = fiducialType253Sub
# end class fiducialType253Sub


class tcoordType254Sub(supermod.tcoordType254):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, **kwargs_):
        super(tcoordType254Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data,  **kwargs_)
supermod.tcoordType254.subclass = tcoordType254Sub
# end class tcoordType254Sub


class textType255Sub(supermod.textType255):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(textType255Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.textType255.subclass = textType255Sub
# end class textType255Sub


class codeType256Sub(supermod.codeType256):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, scheme=None, meaning=None, **kwargs_):
        super(codeType256Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, scheme, meaning,  **kwargs_)
supermod.codeType256.subclass = codeType256Sub
# end class codeType256Sub


class numType257Sub(supermod.numType257):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, float_=None, rational=None, unit=None, qualifier=None, **kwargs_):
        super(numType257Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, float_, rational, unit, qualifier,  **kwargs_)
supermod.numType257.subclass = numType257Sub
# end class numType257Sub


class datetimeType258Sub(supermod.datetimeType258):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(datetimeType258Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.datetimeType258.subclass = datetimeType258Sub
# end class datetimeType258Sub


class dateType259Sub(supermod.dateType259):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(dateType259Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.dateType259.subclass = dateType259Sub
# end class dateType259Sub


class timeType260Sub(supermod.timeType260):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(timeType260Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.timeType260.subclass = timeType260Sub
# end class timeType260Sub


class uidrefType261Sub(supermod.uidrefType261):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(uidrefType261Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.uidrefType261.subclass = uidrefType261Sub
# end class uidrefType261Sub


class pnameType262Sub(supermod.pnameType262):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(pnameType262Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.pnameType262.subclass = pnameType262Sub
# end class pnameType262Sub


class scoordType263Sub(supermod.scoordType263):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoordType263Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoordType263.subclass = scoordType263Sub
# end class scoordType263Sub


class fiducialType264Sub(supermod.fiducialType264):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType264Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType264.subclass = fiducialType264Sub
# end class fiducialType264Sub


class scoord3dType265Sub(supermod.scoord3dType265):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoord3dType265Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoord3dType265.subclass = scoord3dType265Sub
# end class scoord3dType265Sub


class dataType266Sub(supermod.dataType266):
    def __init__(self, uid=None, valueOf_=None, **kwargs_):
        super(dataType266Sub, self).__init__(uid, valueOf_,  **kwargs_)
supermod.dataType266.subclass = dataType266Sub
# end class dataType266Sub


class fiducialType267Sub(supermod.fiducialType267):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType267Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType267.subclass = fiducialType267Sub
# end class fiducialType267Sub


class tcoordType268Sub(supermod.tcoordType268):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, **kwargs_):
        super(tcoordType268Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data,  **kwargs_)
supermod.tcoordType268.subclass = tcoordType268Sub
# end class tcoordType268Sub


class dataType269Sub(supermod.dataType269):
    def __init__(self, type_=None, valueOf_=None, **kwargs_):
        super(dataType269Sub, self).__init__(type_, valueOf_,  **kwargs_)
supermod.dataType269.subclass = dataType269Sub
# end class dataType269Sub


class compositeType270Sub(supermod.compositeType270):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(compositeType270Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.compositeType270.subclass = compositeType270Sub
# end class compositeType270Sub


class imageType271Sub(supermod.imageType271):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(imageType271Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.imageType271.subclass = imageType271Sub
# end class imageType271Sub


class valueType272Sub(supermod.valueType272):
    def __init__(self, sopclass=None, instance=None, frames=None, segments=None, pstate=None, mapping=None, **kwargs_):
        super(valueType272Sub, self).__init__(sopclass, instance, frames, segments, pstate, mapping,  **kwargs_)
supermod.valueType272.subclass = valueType272Sub
# end class valueType272Sub


class waveformType273Sub(supermod.waveformType273):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(waveformType273Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.waveformType273.subclass = waveformType273Sub
# end class waveformType273Sub


class valueType274Sub(supermod.valueType274):
    def __init__(self, sopclass=None, instance=None, channels=None, **kwargs_):
        super(valueType274Sub, self).__init__(sopclass, instance, channels,  **kwargs_)
supermod.valueType274.subclass = valueType274Sub
# end class valueType274Sub


class containerType275Sub(supermod.containerType275):
    def __init__(self, flag=None, id=None, template=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, **kwargs_):
        super(containerType275Sub, self).__init__(flag, id, template, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference,  **kwargs_)
supermod.containerType275.subclass = containerType275Sub
# end class containerType275Sub


class referenceType276Sub(supermod.referenceType276):
    def __init__(self, id=None, ref=None, relationship=None, **kwargs_):
        super(referenceType276Sub, self).__init__(id, ref, relationship,  **kwargs_)
supermod.referenceType276.subclass = referenceType276Sub
# end class referenceType276Sub


class dataType277Sub(supermod.dataType277):
    def __init__(self, type_=None, valueOf_=None, **kwargs_):
        super(dataType277Sub, self).__init__(type_, valueOf_,  **kwargs_)
supermod.dataType277.subclass = dataType277Sub
# end class dataType277Sub


class compositeType278Sub(supermod.compositeType278):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(compositeType278Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.compositeType278.subclass = compositeType278Sub
# end class compositeType278Sub


class textType279Sub(supermod.textType279):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(textType279Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.textType279.subclass = textType279Sub
# end class textType279Sub


class codeType280Sub(supermod.codeType280):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, scheme=None, meaning=None, **kwargs_):
        super(codeType280Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, scheme, meaning,  **kwargs_)
supermod.codeType280.subclass = codeType280Sub
# end class codeType280Sub


class numType281Sub(supermod.numType281):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, float_=None, rational=None, unit=None, qualifier=None, **kwargs_):
        super(numType281Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, float_, rational, unit, qualifier,  **kwargs_)
supermod.numType281.subclass = numType281Sub
# end class numType281Sub


class datetimeType282Sub(supermod.datetimeType282):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(datetimeType282Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.datetimeType282.subclass = datetimeType282Sub
# end class datetimeType282Sub


class dateType283Sub(supermod.dateType283):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(dateType283Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.dateType283.subclass = dateType283Sub
# end class dateType283Sub


class timeType284Sub(supermod.timeType284):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(timeType284Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.timeType284.subclass = timeType284Sub
# end class timeType284Sub


class uidrefType285Sub(supermod.uidrefType285):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(uidrefType285Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.uidrefType285.subclass = uidrefType285Sub
# end class uidrefType285Sub


class pnameType286Sub(supermod.pnameType286):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(pnameType286Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.pnameType286.subclass = pnameType286Sub
# end class pnameType286Sub


class scoordType287Sub(supermod.scoordType287):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoordType287Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoordType287.subclass = scoordType287Sub
# end class scoordType287Sub


class fiducialType288Sub(supermod.fiducialType288):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType288Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType288.subclass = fiducialType288Sub
# end class fiducialType288Sub


class scoord3dType289Sub(supermod.scoord3dType289):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoord3dType289Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoord3dType289.subclass = scoord3dType289Sub
# end class scoord3dType289Sub


class dataType290Sub(supermod.dataType290):
    def __init__(self, uid=None, valueOf_=None, **kwargs_):
        super(dataType290Sub, self).__init__(uid, valueOf_,  **kwargs_)
supermod.dataType290.subclass = dataType290Sub
# end class dataType290Sub


class fiducialType291Sub(supermod.fiducialType291):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType291Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType291.subclass = fiducialType291Sub
# end class fiducialType291Sub


class tcoordType292Sub(supermod.tcoordType292):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, **kwargs_):
        super(tcoordType292Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data,  **kwargs_)
supermod.tcoordType292.subclass = tcoordType292Sub
# end class tcoordType292Sub


class dataType293Sub(supermod.dataType293):
    def __init__(self, type_=None, valueOf_=None, **kwargs_):
        super(dataType293Sub, self).__init__(type_, valueOf_,  **kwargs_)
supermod.dataType293.subclass = dataType293Sub
# end class dataType293Sub


class compositeType294Sub(supermod.compositeType294):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(compositeType294Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.compositeType294.subclass = compositeType294Sub
# end class compositeType294Sub


class imageType295Sub(supermod.imageType295):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(imageType295Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.imageType295.subclass = imageType295Sub
# end class imageType295Sub


class valueType296Sub(supermod.valueType296):
    def __init__(self, sopclass=None, instance=None, frames=None, segments=None, pstate=None, mapping=None, **kwargs_):
        super(valueType296Sub, self).__init__(sopclass, instance, frames, segments, pstate, mapping,  **kwargs_)
supermod.valueType296.subclass = valueType296Sub
# end class valueType296Sub


class waveformType297Sub(supermod.waveformType297):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(waveformType297Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.waveformType297.subclass = waveformType297Sub
# end class waveformType297Sub


class valueType298Sub(supermod.valueType298):
    def __init__(self, sopclass=None, instance=None, channels=None, **kwargs_):
        super(valueType298Sub, self).__init__(sopclass, instance, channels,  **kwargs_)
supermod.valueType298.subclass = valueType298Sub
# end class valueType298Sub


class containerType299Sub(supermod.containerType299):
    def __init__(self, flag=None, id=None, template=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, **kwargs_):
        super(containerType299Sub, self).__init__(flag, id, template, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference,  **kwargs_)
supermod.containerType299.subclass = containerType299Sub
# end class containerType299Sub


class referenceType300Sub(supermod.referenceType300):
    def __init__(self, id=None, ref=None, relationship=None, **kwargs_):
        super(referenceType300Sub, self).__init__(id, ref, relationship,  **kwargs_)
supermod.referenceType300.subclass = referenceType300Sub
# end class referenceType300Sub


class imageType301Sub(supermod.imageType301):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(imageType301Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.imageType301.subclass = imageType301Sub
# end class imageType301Sub


class textType302Sub(supermod.textType302):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(textType302Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.textType302.subclass = textType302Sub
# end class textType302Sub


class codeType303Sub(supermod.codeType303):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, scheme=None, meaning=None, **kwargs_):
        super(codeType303Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, scheme, meaning,  **kwargs_)
supermod.codeType303.subclass = codeType303Sub
# end class codeType303Sub


class numType304Sub(supermod.numType304):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, float_=None, rational=None, unit=None, qualifier=None, **kwargs_):
        super(numType304Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, float_, rational, unit, qualifier,  **kwargs_)
supermod.numType304.subclass = numType304Sub
# end class numType304Sub


class datetimeType305Sub(supermod.datetimeType305):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(datetimeType305Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.datetimeType305.subclass = datetimeType305Sub
# end class datetimeType305Sub


class dateType306Sub(supermod.dateType306):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(dateType306Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.dateType306.subclass = dateType306Sub
# end class dateType306Sub


class timeType307Sub(supermod.timeType307):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(timeType307Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.timeType307.subclass = timeType307Sub
# end class timeType307Sub


class uidrefType308Sub(supermod.uidrefType308):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(uidrefType308Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.uidrefType308.subclass = uidrefType308Sub
# end class uidrefType308Sub


class pnameType309Sub(supermod.pnameType309):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(pnameType309Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.pnameType309.subclass = pnameType309Sub
# end class pnameType309Sub


class scoordType310Sub(supermod.scoordType310):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoordType310Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoordType310.subclass = scoordType310Sub
# end class scoordType310Sub


class fiducialType311Sub(supermod.fiducialType311):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType311Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType311.subclass = fiducialType311Sub
# end class fiducialType311Sub


class scoord3dType312Sub(supermod.scoord3dType312):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoord3dType312Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoord3dType312.subclass = scoord3dType312Sub
# end class scoord3dType312Sub


class dataType313Sub(supermod.dataType313):
    def __init__(self, uid=None, valueOf_=None, **kwargs_):
        super(dataType313Sub, self).__init__(uid, valueOf_,  **kwargs_)
supermod.dataType313.subclass = dataType313Sub
# end class dataType313Sub


class fiducialType314Sub(supermod.fiducialType314):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType314Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType314.subclass = fiducialType314Sub
# end class fiducialType314Sub


class tcoordType315Sub(supermod.tcoordType315):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, **kwargs_):
        super(tcoordType315Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data,  **kwargs_)
supermod.tcoordType315.subclass = tcoordType315Sub
# end class tcoordType315Sub


class dataType316Sub(supermod.dataType316):
    def __init__(self, type_=None, valueOf_=None, **kwargs_):
        super(dataType316Sub, self).__init__(type_, valueOf_,  **kwargs_)
supermod.dataType316.subclass = dataType316Sub
# end class dataType316Sub


class compositeType317Sub(supermod.compositeType317):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(compositeType317Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.compositeType317.subclass = compositeType317Sub
# end class compositeType317Sub


class imageType318Sub(supermod.imageType318):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(imageType318Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.imageType318.subclass = imageType318Sub
# end class imageType318Sub


class valueType319Sub(supermod.valueType319):
    def __init__(self, sopclass=None, instance=None, frames=None, segments=None, pstate=None, mapping=None, **kwargs_):
        super(valueType319Sub, self).__init__(sopclass, instance, frames, segments, pstate, mapping,  **kwargs_)
supermod.valueType319.subclass = valueType319Sub
# end class valueType319Sub


class waveformType320Sub(supermod.waveformType320):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(waveformType320Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.waveformType320.subclass = waveformType320Sub
# end class waveformType320Sub


class valueType321Sub(supermod.valueType321):
    def __init__(self, sopclass=None, instance=None, channels=None, **kwargs_):
        super(valueType321Sub, self).__init__(sopclass, instance, channels,  **kwargs_)
supermod.valueType321.subclass = valueType321Sub
# end class valueType321Sub


class containerType322Sub(supermod.containerType322):
    def __init__(self, flag=None, id=None, template=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, **kwargs_):
        super(containerType322Sub, self).__init__(flag, id, template, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference,  **kwargs_)
supermod.containerType322.subclass = containerType322Sub
# end class containerType322Sub


class referenceType323Sub(supermod.referenceType323):
    def __init__(self, id=None, ref=None, relationship=None, **kwargs_):
        super(referenceType323Sub, self).__init__(id, ref, relationship,  **kwargs_)
supermod.referenceType323.subclass = referenceType323Sub
# end class referenceType323Sub


class valueType324Sub(supermod.valueType324):
    def __init__(self, sopclass=None, instance=None, frames=None, segments=None, pstate=None, mapping=None, **kwargs_):
        super(valueType324Sub, self).__init__(sopclass, instance, frames, segments, pstate, mapping,  **kwargs_)
supermod.valueType324.subclass = valueType324Sub
# end class valueType324Sub


class waveformType325Sub(supermod.waveformType325):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(waveformType325Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.waveformType325.subclass = waveformType325Sub
# end class waveformType325Sub


class textType326Sub(supermod.textType326):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(textType326Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.textType326.subclass = textType326Sub
# end class textType326Sub


class codeType327Sub(supermod.codeType327):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, scheme=None, meaning=None, **kwargs_):
        super(codeType327Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, scheme, meaning,  **kwargs_)
supermod.codeType327.subclass = codeType327Sub
# end class codeType327Sub


class numType328Sub(supermod.numType328):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, float_=None, rational=None, unit=None, qualifier=None, **kwargs_):
        super(numType328Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, float_, rational, unit, qualifier,  **kwargs_)
supermod.numType328.subclass = numType328Sub
# end class numType328Sub


class datetimeType329Sub(supermod.datetimeType329):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(datetimeType329Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.datetimeType329.subclass = datetimeType329Sub
# end class datetimeType329Sub


class dateType330Sub(supermod.dateType330):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(dateType330Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.dateType330.subclass = dateType330Sub
# end class dateType330Sub


class timeType331Sub(supermod.timeType331):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(timeType331Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.timeType331.subclass = timeType331Sub
# end class timeType331Sub


class uidrefType332Sub(supermod.uidrefType332):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(uidrefType332Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.uidrefType332.subclass = uidrefType332Sub
# end class uidrefType332Sub


class pnameType333Sub(supermod.pnameType333):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(pnameType333Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.pnameType333.subclass = pnameType333Sub
# end class pnameType333Sub


class scoordType334Sub(supermod.scoordType334):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoordType334Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoordType334.subclass = scoordType334Sub
# end class scoordType334Sub


class fiducialType335Sub(supermod.fiducialType335):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType335Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType335.subclass = fiducialType335Sub
# end class fiducialType335Sub


class scoord3dType336Sub(supermod.scoord3dType336):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoord3dType336Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoord3dType336.subclass = scoord3dType336Sub
# end class scoord3dType336Sub


class dataType337Sub(supermod.dataType337):
    def __init__(self, uid=None, valueOf_=None, **kwargs_):
        super(dataType337Sub, self).__init__(uid, valueOf_,  **kwargs_)
supermod.dataType337.subclass = dataType337Sub
# end class dataType337Sub


class fiducialType338Sub(supermod.fiducialType338):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType338Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType338.subclass = fiducialType338Sub
# end class fiducialType338Sub


class tcoordType339Sub(supermod.tcoordType339):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, **kwargs_):
        super(tcoordType339Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data,  **kwargs_)
supermod.tcoordType339.subclass = tcoordType339Sub
# end class tcoordType339Sub


class dataType340Sub(supermod.dataType340):
    def __init__(self, type_=None, valueOf_=None, **kwargs_):
        super(dataType340Sub, self).__init__(type_, valueOf_,  **kwargs_)
supermod.dataType340.subclass = dataType340Sub
# end class dataType340Sub


class compositeType341Sub(supermod.compositeType341):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(compositeType341Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.compositeType341.subclass = compositeType341Sub
# end class compositeType341Sub


class imageType342Sub(supermod.imageType342):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(imageType342Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.imageType342.subclass = imageType342Sub
# end class imageType342Sub


class valueType343Sub(supermod.valueType343):
    def __init__(self, sopclass=None, instance=None, frames=None, segments=None, pstate=None, mapping=None, **kwargs_):
        super(valueType343Sub, self).__init__(sopclass, instance, frames, segments, pstate, mapping,  **kwargs_)
supermod.valueType343.subclass = valueType343Sub
# end class valueType343Sub


class waveformType344Sub(supermod.waveformType344):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(waveformType344Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.waveformType344.subclass = waveformType344Sub
# end class waveformType344Sub


class valueType345Sub(supermod.valueType345):
    def __init__(self, sopclass=None, instance=None, channels=None, **kwargs_):
        super(valueType345Sub, self).__init__(sopclass, instance, channels,  **kwargs_)
supermod.valueType345.subclass = valueType345Sub
# end class valueType345Sub


class containerType346Sub(supermod.containerType346):
    def __init__(self, flag=None, id=None, template=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, **kwargs_):
        super(containerType346Sub, self).__init__(flag, id, template, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference,  **kwargs_)
supermod.containerType346.subclass = containerType346Sub
# end class containerType346Sub


class referenceType347Sub(supermod.referenceType347):
    def __init__(self, id=None, ref=None, relationship=None, **kwargs_):
        super(referenceType347Sub, self).__init__(id, ref, relationship,  **kwargs_)
supermod.referenceType347.subclass = referenceType347Sub
# end class referenceType347Sub


class valueType348Sub(supermod.valueType348):
    def __init__(self, sopclass=None, instance=None, channels=None, **kwargs_):
        super(valueType348Sub, self).__init__(sopclass, instance, channels,  **kwargs_)
supermod.valueType348.subclass = valueType348Sub
# end class valueType348Sub


class containerType349Sub(supermod.containerType349):
    def __init__(self, flag=None, id=None, template=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, **kwargs_):
        super(containerType349Sub, self).__init__(flag, id, template, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference,  **kwargs_)
supermod.containerType349.subclass = containerType349Sub
# end class containerType349Sub


class textType350Sub(supermod.textType350):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(textType350Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.textType350.subclass = textType350Sub
# end class textType350Sub


class codeType351Sub(supermod.codeType351):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, scheme=None, meaning=None, **kwargs_):
        super(codeType351Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, scheme, meaning,  **kwargs_)
supermod.codeType351.subclass = codeType351Sub
# end class codeType351Sub


class numType352Sub(supermod.numType352):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, float_=None, rational=None, unit=None, qualifier=None, **kwargs_):
        super(numType352Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value, float_, rational, unit, qualifier,  **kwargs_)
supermod.numType352.subclass = numType352Sub
# end class numType352Sub


class datetimeType353Sub(supermod.datetimeType353):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(datetimeType353Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.datetimeType353.subclass = datetimeType353Sub
# end class datetimeType353Sub


class dateType354Sub(supermod.dateType354):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(dateType354Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.dateType354.subclass = dateType354Sub
# end class dateType354Sub


class timeType355Sub(supermod.timeType355):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(timeType355Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.timeType355.subclass = timeType355Sub
# end class timeType355Sub


class uidrefType356Sub(supermod.uidrefType356):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(uidrefType356Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.uidrefType356.subclass = uidrefType356Sub
# end class uidrefType356Sub


class pnameType357Sub(supermod.pnameType357):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(pnameType357Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.pnameType357.subclass = pnameType357Sub
# end class pnameType357Sub


class scoordType358Sub(supermod.scoordType358):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoordType358Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoordType358.subclass = scoordType358Sub
# end class scoordType358Sub


class fiducialType359Sub(supermod.fiducialType359):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType359Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType359.subclass = fiducialType359Sub
# end class fiducialType359Sub


class scoord3dType360Sub(supermod.scoord3dType360):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, fiducial=None, **kwargs_):
        super(scoord3dType360Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data, fiducial,  **kwargs_)
supermod.scoord3dType360.subclass = scoord3dType360Sub
# end class scoord3dType360Sub


class dataType361Sub(supermod.dataType361):
    def __init__(self, uid=None, valueOf_=None, **kwargs_):
        super(dataType361Sub, self).__init__(uid, valueOf_,  **kwargs_)
supermod.dataType361.subclass = dataType361Sub
# end class dataType361Sub


class fiducialType362Sub(supermod.fiducialType362):
    def __init__(self, uid=None, **kwargs_):
        super(fiducialType362Sub, self).__init__(uid,  **kwargs_)
supermod.fiducialType362.subclass = fiducialType362Sub
# end class fiducialType362Sub


class tcoordType363Sub(supermod.tcoordType363):
    def __init__(self, type_=None, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, data=None, **kwargs_):
        super(tcoordType363Sub, self).__init__(type_, id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, data,  **kwargs_)
supermod.tcoordType363.subclass = tcoordType363Sub
# end class tcoordType363Sub


class dataType364Sub(supermod.dataType364):
    def __init__(self, type_=None, valueOf_=None, **kwargs_):
        super(dataType364Sub, self).__init__(type_, valueOf_,  **kwargs_)
supermod.dataType364.subclass = dataType364Sub
# end class dataType364Sub


class compositeType365Sub(supermod.compositeType365):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(compositeType365Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.compositeType365.subclass = compositeType365Sub
# end class compositeType365Sub


class imageType366Sub(supermod.imageType366):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(imageType366Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.imageType366.subclass = imageType366Sub
# end class imageType366Sub


class valueType367Sub(supermod.valueType367):
    def __init__(self, sopclass=None, instance=None, frames=None, segments=None, pstate=None, mapping=None, **kwargs_):
        super(valueType367Sub, self).__init__(sopclass, instance, frames, segments, pstate, mapping,  **kwargs_)
supermod.valueType367.subclass = valueType367Sub
# end class valueType367Sub


class waveformType368Sub(supermod.waveformType368):
    def __init__(self, id=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, value=None, **kwargs_):
        super(waveformType368Sub, self).__init__(id, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference, value,  **kwargs_)
supermod.waveformType368.subclass = waveformType368Sub
# end class waveformType368Sub


class valueType369Sub(supermod.valueType369):
    def __init__(self, sopclass=None, instance=None, channels=None, **kwargs_):
        super(valueType369Sub, self).__init__(sopclass, instance, channels,  **kwargs_)
supermod.valueType369.subclass = valueType369Sub
# end class valueType369Sub


class containerType370Sub(supermod.containerType370):
    def __init__(self, flag=None, id=None, template=None, relationship=None, concept=None, observation=None, text=None, code=None, num=None, datetime=None, date=None, time=None, uidref=None, pname=None, scoord=None, scoord3d=None, tcoord=None, composite=None, image=None, waveform=None, container=None, reference=None, **kwargs_):
        super(containerType370Sub, self).__init__(flag, id, template, relationship, concept, observation, text, code, num, datetime, date, time, uidref, pname, scoord, scoord3d, tcoord, composite, image, waveform, container, reference,  **kwargs_)
supermod.containerType370.subclass = containerType370Sub
# end class containerType370Sub


class referenceType371Sub(supermod.referenceType371):
    def __init__(self, id=None, ref=None, relationship=None, **kwargs_):
        super(referenceType371Sub, self).__init__(id, ref, relationship,  **kwargs_)
supermod.referenceType371.subclass = referenceType371Sub
# end class referenceType371Sub


class referenceType372Sub(supermod.referenceType372):
    def __init__(self, id=None, ref=None, relationship=None, **kwargs_):
        super(referenceType372Sub, self).__init__(id, ref, relationship,  **kwargs_)
supermod.referenceType372.subclass = referenceType372Sub
# end class referenceType372Sub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Report'
        rootClass = supermod.Report
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:dsr="http://dicom.offis.de/dcmsr"',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Report'
        rootClass = supermod.Report
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Report'
        rootClass = supermod.Report
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:dsr="http://dicom.offis.de/dcmsr"')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Report'
        rootClass = supermod.Report
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from dsr2xml_api import *\n\n')
        sys.stdout.write('import dsr2xml_api as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
