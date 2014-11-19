

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
    if c > 90:
    	#print("high match:", SADstring, ":", FRESCOstring, c)
    	return(FRESCOstring)
    else:
    	return("")
   #if it is a match, want to update
   #should return LCSH or false

  # if the percent match is over 75%, dump the FRESCO name into the extant LC column in the CSV (row[3]). or, add a new column?? (just make a new one directly in the CSV)
#to figure out: how to make a new column in an already existing CSV (diana is working on this)
#how do i make sure the name goes into the right row?

with open("colon3_table_export2.csv", "r") as f:

	colondictionary = csv.DictReader(f)
	for row in colondictionary:
		if row == "":
			print(row)
		#dictionary_item = row

		#print(row)
	# 	print(row["WNAM"])
	#print(colondictionary)
		# colonJSON = json.dumps(dictionary_item)
		# if colonJSON == "WNAM":

		# 	print(colonJSON)

		#for colonfield in colonJSON:
				#mainSADname = colonJSON[colonfield]
		#	print(colonfield)
		
	# print(colonJSON)
	#print(colon3_table_export)
	#colon3_table_export = json.loads(colon3_table_export)

	#print(colon3_table_export)
	# for row in colon3_table_export:
	# 	#define all the columns as variables, so later can write a new CSV with all the old columns plus my new data?
	# 	print(row["title"])
		#mainSADname = row[1]
		# with open("FRESCO_spanish_names.csv", "r", encoding="ISO-8859-1") as g:
		# 	FRESCO_spanish_names = csv.reader(g)
			
			# for row in FRESCO_spanish_names:
			# 	frescoSH = row[0]
			# 	d = compare(mainSADname,frescoSH)

			# 	if d != False:
			# 		FRESCOname = d
			# 		writer = csv.writer(f)
			# 		writer.writerow(colon3_table_export2)
	# 				for row in colon3_table_export2:

#make it a JSON dictionary
#replace the value i want to
#then write the JSON dictionary to a CSV
		# variable = compare function, returns true or false
		# if it's true, then update 