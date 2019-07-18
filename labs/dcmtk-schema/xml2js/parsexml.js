// print process.argv
process.argv.forEach(function (val, index, array) {
  console.log(index + ': ' + val);
});

fs = require("fs")
var util = require("util")
const xml = require("xml-parse")
//var parseString = require("xml2js").parseString
xml2js = require('xml2js');
parser = new xml2js.Parser({"preserveChildrenOrder": true, "explicitChildren": true})

fs.readFile(process.argv[2], 'utf8', function (err,data) {
  if (err) {
    return console.log(err);
  }

  //var parsedXML = xml.parse(data);
  //console.log(parsedXML);

  parser.parseString(data, function(err, result) {
    console.log(util.inspect(result, false, null));
    //console.log(result);
  })
//  parseString(data, {preserveChildrenOrder: true}, function(err, result) {
//  parseString(data, function(err, result) {
//    console.dir(JSON.stringify(result));
//  });
});
