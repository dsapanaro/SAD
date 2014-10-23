import csv

with open("colon3_table_export.csv", "r") as f:

	reader = csv.reader(f)
	for row in reader:
		print (row[26])
