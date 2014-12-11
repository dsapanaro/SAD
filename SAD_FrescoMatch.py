import csv, difflib
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from fuzzywuzzy import utils
from fuzzywuzzy.string_processing import StringProcessor


def compare(SADstring,FRESCOstring):
#going to pass the SADstring to the function that will then perform levenstein matching/fuzzy match and 
#want to break up each name string into words, then see if substrings are present, and what percentage of the words are the same.
#might also want to explore breaking a name into its parts using nameparser and comparing those elements.
#might also want to figure out how to tell the compare function to not take dates into account.

    c = fuzz.token_set_ratio(SADstring, FRESCOstring)
    #d = fuzz.ratio(SADstring,FRESCOstring)
    if c > 90: #and d > 80:
    	#print("high match:", SADstring, ":", FRESCOstring, c)
    	return(FRESCOstring)
    else:
    	return(False)
   #if it is a match, want to update
   #should return LCSH or false

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

		for fresconame in FRESCO_list:
			match = compare(mainSADname,fresconame)
			if match != False:
				#put frescoSH in column
 				row["FRESCOSH"] = match
 				print(row["FRESCOSH"])
		# print("got it")
		colondictionary_list.append(colondictionary_item)
	
	with open ("colon3_table_export_fresco.csv", "w") as h:

		writer = csv.DictWriter(h, fieldnames=fieldnames)
		headers = dict((n,n) for n in fieldnames)
		writer.writerow(headers)

		for a_row in colondictionary_list:
	 		writer.writerow(a_row)
