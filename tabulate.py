import os, sys, json, pandas
from QDBDParser import QDBDParser
from SRCDParser import SRCDParser
import json

#dcmqiPath = '/Users/fedorov/local/builds/dcmqi-refactored/dcmqi-build/bin'
#dcmqiPath = '/Users/BillClifford/local/builds/dcmqi-mac/bin'
#dcmqiPath = '/Users/fedorov/Downloads/dcmqi-mac/bin'
tempPath = '.'

# Inputs:
#  #1 - DB schema file from https://app.quickdatabasediagrams.com
#    (remove all layout components from the bottom if exporting
#    from the web, or use the included in the repo schema.qdbd)
#  #2 - directory with the files from TCIA QIN-HEADNECK collection
#
# Output: one csv file per table defined in the schema
#  attributes not found will be empty!

def main():

  tablesParser = QDBDParser(sys.argv[1])
  tablesRules = tablesParser.getTablesSchema()

  for root,dirs,files in os.walk(sys.argv[2]):
    for f in files:


      tables = {}
      tables["Instance2File"] = []
      for t in tablesRules.keys():
        tables[t] = []

      dcmName = os.path.join(root,f)

      try:
        dicomParser = SRCDParser(dcmName, tablesRules, tempPath=tempPath)
      except:
        print("Failed to read as DICOM:"+dcmName)
        continue

      try:
        dicomParser.parse()
      except:
        print("Failed to parse: "+dcmName)
        import traceback
        traceback.print_exc()
        return

      dcmFileTables = dicomParser.getTables()

      if len(dcmFileTables.keys()) == 0:
        print("Error: no tables generated for "+dcmName)

      for t in dcmFileTables.keys():
        # print "Appending", dcmFileTables[t].values
        # print dicomTables[t]
        tableOrRow = dcmFileTables[t]
        if isinstance(tableOrRow,dict):
          tables[t].append(tableOrRow)
        elif isinstance(tableOrRow,list):
          for row in tableOrRow:
            tables[t].append(row)

      for t in tables.keys():
        if len(tables[t]):
          tables[t] = pandas.DataFrame(tables[t])

      for t in tables.keys():
        if type(tables[t]) == pandas.DataFrame:
          fileName = os.path.join(sys.argv[3],t+".tsv")
          if not os.path.isfile(fileName):
            tables[t].to_csv(fileName,index=False,sep='\t')
          else:
            tables[t].to_csv(fileName,index=False,sep='\t',mode='a',header=False)


if __name__ == '__main__':
  if len(sys.argv)<4:
    print("Usage: tabulate.py <schema file> <input DICOM directory> <output directory>")
  else:
    main()
