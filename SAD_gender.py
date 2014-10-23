import csv

with open("colon3_table_export.csv", "r") as f:

	reader = csv.reader(f)
	for row in reader:
		#print (row [1] + row[26])
		#if row[26] == "y":
			#print(row[1])
		if row[26] == '':
			print("This is a male artist", row[1])


