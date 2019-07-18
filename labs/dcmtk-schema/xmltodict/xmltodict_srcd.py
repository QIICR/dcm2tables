import xmltodict, json, sys

'''
class ClinicalDocument(Object):
  def __init__(self, document_json):
    self.document_json = document_json
    self.top_level_container = document_json["report"]["document"]["content"]["container"]

'''

with open(sys.argv[1], "r") as f:
  # note this solution uses a customized fork of xmltodict to store the order
  #   attributes (note the extra option):
  #   https://github.com/lindsay-stevens/xmltodict/tree/ordered-children-short-tags
  json_report = xmltodict.parse(f.read(), ordered_mixed_children=True)
  print(json.dumps(json_report, indent=2))
