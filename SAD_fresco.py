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
# if the percent match is over 75%, dump the FRESCO name into a new column in the CSV.
#to figure out: how to make a new column in an already existing CSV (diana is working on this)	
#want to break up each name string into words, then see if substrings are present, and what percentage of the words are the same.

    #return difflib.SequenceMatcher(x=SADstring.lower(), y=FRESCOstring.lower()).ratio() > 0.9
  #  comparison = difflib.SequenceMatcher(None, SADstring, FRESCOstring)
  #  comparison.ratio()
  #  if comparison.ratio() > .5:
   # 	print(SADstring, ":",FRESCOstring)
    c = fuzz.token_set_ratio(SADstring, FRESCOstring)
    if c > 90:
    	print("high match:", SADstring, ":", FRESCOstring, c)
   
   # if c < 90 and c > 75:
    #	print ("mid match:", SADstring, ":", FRESCOstring, c)

with open("colon3_table_export.csv", "r") as f:

	reader = csv.reader(f)
	for row in reader:
		mainSADname = row[1]
		SADnames.append(mainSADname)
	#print (SADnames)
with open("FRESCO_spanish_names.csv", "r", encoding="ISO-8859-1") as f:

	reader = csv.reader(f)
	for row in reader:
		frescoSH = row[0]
		FRESCOnames.append(frescoSH)
	#print(FRESCOnames)

for x in SADnames:
	SADname = x

	for y in FRESCOnames:

		FRESCOname = y

		compare(SADname, FRESCOname)
	#print(compare)


#' '.join([j for j, m in zip(SADnames.split(), FRESCOnames.split()) if j==m])
#eventually need to write back into this CSV, and tell it exactly where to write the new column