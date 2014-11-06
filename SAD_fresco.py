#establish match between SAD name and FRESCO subject heading.
#use two csv files
#loop through each file, and if the name is the same
#then I want to pull out the FRESCO name and insert it into the LC name column in the CSV.
#how can i determine probable but not exact matches? looking for similarity.

#have two lists of different lengths, want to compare (intersect?) the two and determine which are probable matches.


import csv

SADnames = []
FRESCOnames = []

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

#' '.join([j for j, m in zip(SADnames.split(), FRESCOnames.split()) if j==m])
#eventually need to write back into this CSV, and tell it exactly where to write the new column