import csv

with open("colon3_table_export.csv", "r") as f:

	Female_Artists = []

	reader = csv.reader(f)
	for row in reader:
		#print (row [1] + row[26])
			#print(row[1])
		if row[26] == "y":
		


