#establish match between main name and VIAF cluster.
#use viaf API
#want to look in VIAF cluster's heading, preferred forms, and alternate name forms
#question: in a VIAF record, in the about section,
#under personal information, there is a field called Nationality.
#Is it possible for me to query this and therefore limit to "spanish"?
#is the SAD main entry name the same as any of those?
#if yes
#then I want to pull out the name contributed by LC and insert it into the LC name column in the CSV.
#and I also want to pull out the VIAF URI and the LC URI and put those in new fields.

#want to look in VIAF cluster's heading, preferred forms, and alternate name forms
#for each main name entry in SAD, create a new viaf search with that name as the search term.
#is the SAD main entry name the same as any of those?
#if yes
#then I want to pull out the name contributed by LC and insert it into the LC name column in the CSV.
#and I also want to pull out the VIAF URI and the LC URI and put those in new fields.

#http://www.voidspace.org.uk/python/articles/OOP.shtml

import requests, json, csv
import xml.etree.ElementTree as etree

#payload = { "query" : "local.names"}
#r = requests.get('http://viaf.org/viaf/search', params=payload)
#class viafSearch:

viafurl = "http://viaf.org/viaf/search?query=cql.any+=+{NAME}&httpAccept=text/xml"
sourceFile = 'colon3_table_export.csv'

def __init__(self):
	self.processFile()

def requestProcess(self,searchVal):	

	with open("colon3_table_export.csv", "r") as f:

		reader = csv.reader(f)
		for row in reader:
			mainSADname = row[1]
			mainSADname = '"' + mainSADname + '"'
		#print(mainSADname)

#def viaf_search(mainSADname):
	
r = requests.get(viafurl.replace('{NAME}',mainSADname))
viafurl.replace('{NAME}',mainSADname)
print(viafurl)
#data = json.loads(r.text)
#print(data)