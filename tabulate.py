import os
import sys
import pandas
import logging
import argparse
from DICOMParser import DCMQINotFoundError, TIDNotSupportedError
from QDBDParser import QDBDParser
from SRCDParser import SRCDParser


tempPath = '.'

# Inputs:
#  #1 - DB schema file from https://app.quickdatabasediagrams.com
#    (remove all layout components from the bottom if exporting
#    from the web, or use the included in the repo schema.qdbd)
#  #2 - directory with the files from TCIA QIN-HEADNECK collection
#
# Output: one csv file per table defined in the schema
#  attributes not found will be empty!

def main(argv):

  parser = argparse.ArgumentParser(description="")
  parser.add_argument("-s", "--schema-file", dest="schema", metavar="PATH", default="schema.qdbd", required=False,
                      help="Input schema for organizing data retrieved from input DICOM directories")
  parser.add_argument("-d", "--input-directory", dest="inputDirectory", metavar="PATH", default="-", required=True,
                      help="Input directory to recursively search and read DICOM information into tables")
  parser.add_argument("-o", "--output-directory", dest="outputDirectory", metavar="PATH", default="-", required=True,
                      help="Output directory to write tables in csv format to")
  parser.add_argument("-dcmqi", "--dcmqi-path", dest="dcmqiPath", metavar="PATH",
                      default=os.environ.get('DCMQI_PATH', None), required=False,
                      help="Binary directory of dcmqi which is needed for reading DICOM SR TID1500")
  args = parser.parse_args(argv)

  if not args.dcmqiPath:
    logging.warning("Parsing of DICOM SR TID 1500 won't be possible without specifying the location of your dcmqi "
                    "executables. You can either specify dcmqi as an environment variable 'DCMQI_PATH' or as an "
                    "additional parameter '-dcmqi <DCMQI binary path>'")

  if not os.path.exists(args.outputDirectory):
    create = raw_input('Output directory does not exist. Would you like to create it? [y/n]:\n')
    if create.lower() in ["y", "yes", "true"]:
      print("Creating directory %s" % args.outputDirectory)
      os.makedirs(args.outputDirectory)
    else:
      if not create.lower() in ["", "n", "no", "false"]:
        print ("Entered letters %s unknown to this program." % create)
      return

  tablesParser = QDBDParser(args.schema)
  tablesRules = tablesParser.getTablesSchema()

  for root,dirs,files in os.walk(args.inputDirectory):
    for f in files:
      tables = {
        "Instance2File": []
      }
      for t in tablesRules.keys():
        tables[t] = []

      dcmName = os.path.join(root,f)
      print("Parsing "+dcmName)

      try:
        dicomParser = SRCDParser(dcmName, tablesRules, tempPath=tempPath, dcmqiPath=args.dcmqiPath)
      except:
        print("Failed to read as DICOM: %s" % dcmName)
        continue

      try:
        dicomParser.parse()
      except DCMQINotFoundError as exc:
        print ("Reading of DICOM SR measurements impossible: %s " % exc)
        print ("Make sure that you specified dcmqi path either in your environment variable 'DCMQI_PATH' or as an "
              "additional parameter '-dcmqi <DCMQI binary path>'")
        print ("Continuing without reading DICOM SR measurements.")
      except TIDNotSupportedError as exc:
        print (exc)
        continue
      except Exception:
        print ("Failed to parse: %s " % dcmName)
        import traceback
        traceback.print_exc()
        continue

      dcmFileTables = dicomParser.getTables()

      if len(dcmFileTables.keys()) == 0:
        print("Error: no tables generated for %s" % dcmName)

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
          fileName = os.path.join(args.outputDirectory,t+".tsv")
          if not os.path.isfile(fileName):
            tables[t].to_csv(fileName,index=False,sep='\t')
          else:
            tables[t].to_csv(fileName,index=False,sep='\t',mode='a',header=False)


if __name__ == "__main__":
  main(sys.argv[1:])
