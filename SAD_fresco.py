#establish match between SAD name and FRESCO subject heading.
#use two csv files
#loop through each file, and if the name is the same
#then I want to pull out the FRESCO name and insert it into the LC name column in the CSV.
#how can i determine probable but not exact matches? looking for similarity.

#have two lists of different lengths, want to compare (intersect?) the two and determine which are probable matches.


import csv, difflib
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

    #return difflib.SequenceMatcher(x=SADstring.lower(), y=FRESCOstring.lower()).ratio() > 0.9
  #  comparison = difflib.SequenceMatcher(None, SADstring, FRESCOstring)
  #  comparison.ratio()
  #  if comparison.ratio() > .5:
   # 	print(SADstring, ":",FRESCOstring)
    c = fuzz.token_set_ratio(SADstring, FRESCOstring)
    if c > 90:
    	#print("high match:", SADstring, ":", FRESCOstring, c)
    	return(FRESCOstring)
    else:
    	return(False)
   #if it is a match, want to update
   #should return LCSH or false

  # if the percent match is over 75%, dump the FRESCO name into the extant LC column in the CSV (row[3]). or, add a new column?? (just make a new one directly in the CSV)
#to figure out: how to make a new column in an already existing CSV (diana is working on this)
#how do i make sure the name goes into the right row?

with open("colon3_table_export2.csv", "r") as f:

	colon3_table_export2 = csv.reader(f)
	for row in colon3_table_export2:
		FRESCOname = row[4]
		mainSADname = row[1]
		with open("FRESCO_spanish_names.csv", "r", encoding="ISO-8859-1") as g:
			FRESCO_spanish_names = csv.reader(g)
			for row in FRESCO_spanish_names:
				frescoSH = row[0]
				d = compare(mainSADname,frescoSH)
		
				if d != False:
					FRESCOname = d
					# writer = csv.writer(f)
					# writer.writerow(colon3_table_export2)
	# 				for row in colon3_table_export2:
			
 # with open("colon3_table_export2.csv", "w") as f:
 # 	
 # with open("colon3_table_export2.csv", "r") as f:

# 	colon3_table_export2 = csv.reader(f)
# 	for row in colon3_table_export2:
# 		mainSADname = row[1]
# 		SADnames.append(mainSADname)
# 	#print (SADnames)
# with open("FRESCO_spanish_names.csv", "r", encoding="ISO-8859-1") as g:

# 	FRESCO_spanish_names = csv.reader(g)
# 	for row in FRESCO_spanish_names:
# 		frescoSH = row[0]
# 		FRESCOnames.append(frescoSH)
# for x in SADnames:
# 	SADname = x

# 	for y in FRESCOnames:

# 		FRESCOname = y

# 		compare(SADname, FRESCOname)

		# variable = compare function, returns true or false
		# if it's true, then update 

#' '.join([j for j, m in zip(SADnames.split(), FRESCOnames.split()) if j==m])
#eventually need to write back into this CSV, and tell it exactly where to write the new column