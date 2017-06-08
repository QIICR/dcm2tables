import os, sys, json, pandas
from QDBDParser import QDBDParser
from DICOMParser import DICOMParser
import json

def main():

  tablesParser = QDBDParser(sys.argv[1])
  tablesRules = tablesParser.getTablesSchema()
  print json.dumps(tablesRules, indent=2)

  tables = {}
  for t in tablesRules.keys():
    tables[t] = pandas.DataFrame(columns=tablesRules[t])

  dicomParser = DICOMParser(sys.argv[2], tablesRules)
  dicomParser.parse()
  dicomTables = dicomParser.getTables()

  for t in dicomTables:
    print "Appending", dicomTables[t].values
    print dicomTables[t]
    tables[t] = pandas.DataFrame([dicomTables[t]])


  print "DICOM tables:"
  for t in tablesRules.keys():
    print tables[t].to_string()

if __name__ == '__main__':
  main()
