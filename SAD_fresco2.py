

import csv, difflib
import json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from fuzzywuzzy import utils
from fuzzywuzzy.string_processing import StringProcessor
#import nltk
SADnames = []
FRESCOnames = []
HighMatches = {}

def compare(SADstring,FRESCOstring):
#going to pass the SADstring to the function that will then perform levenstein matching/fuzzy match and 
#want to break up each name string into words, then see if substrings are present, and what percentage of the words are the same.

    c = fuzz.token_set_ratio(SADstring, FRESCOstring)
    d = fuzz.ratio(SADstring,FRESCOstring)
    if c > 90 and d > 80:
    	#print("high match:", SADstring, ":", FRESCOstring, c)
    	return(FRESCOstring)
    else:
    	return(False)
   #if it is a match, want to update
   #should return LCSH or false

  # if the percent match is over 75%, dump the FRESCO name into the extant LC column in the CSV (row[3]). or, add a new column?? (just make a new one directly in the CSV)
#to figure out: how to make a new column in an already existing CSV (diana is working on this)
#how do i make sure the name goes into the right row?
#for name matching: could i both match tokens (name elements like first name or last name) and # of similar letters?
FRESCO_list = []
fieldnames = "RN", "WNAM", "", "LCN", "FRESCOSH", "BDATN", "BQN", "BQEN", "BDQN", "DDATN", "DQN", "DQEN", "DDQN", "OPRN", "OQN", "OOQN", "WDATES", "SDATN", "SDAT2N", "CENN", "CNUMN", "SCHN", "NSCHP","CLNON", "MEDN", "NBN", "UDATN", "FEM", "CLN", "UNCLN", "SUPN", "STAMPN", "UPN", "teaser", "SORTNAME", "FirstLetter","SEARCH","alts","","holdings","bestname","recid","notes","earliestdate","latestdate","latest","earliest","problem","teasterweb","event","more","teasterweb2","",""
colondictionary_list = []

with open("FRESCO_spanish_names.csv", "r", encoding="ISO-8859-1") as g:
	FRESCO_spanish_names = csv.reader(g)
	for row in FRESCO_spanish_names:
		FRESCO_list.append(row[0])

with open("colon3_table_export3.csv", "r") as f:

	colondictionary = csv.DictReader(f)
	for row in colondictionary:
		colondictionary_item = row
		mainSADname = colondictionary_item["WNAM"]
		#fresconame = row["FRESCOSH"]
		#print(mainSADname)
		#dictionary_item = row
		for fresconame in FRESCO_list:
			match = compare(mainSADname,fresconame)
			if match != False:
				#put frescoSH in column
 				row["FRESCOSH"] = match
 				print(row["FRESCOSH"])
		# print("got it")
	# 	colondictionary_list.append(colondictionary_item)
	# print(dict.items(colondictionary_item))
	
	with open ("colon3_table_export_fresco.csv", "w") as h:

		writer = csv.DictWriter(h, fieldnames=fieldnames)
		headers = dict((n,n) for n in fieldnames)
		writer.writerow(headers)

		for a_row in colondictionary_list:
	 		writer.writerow(a_row)

#make it a JSON dictionary
#replace the value i want to
#then write the JSON dictionary to a CSV
		# variable = compare function, returns true or false
		# if it's true, then update 