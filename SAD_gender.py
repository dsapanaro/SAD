import csv

with open("colon3_table_export.csv", "r") as f:

	Female_Artists = []

	reader = csv.reader(f)
	for row in reader:
		#print (row[1] + row[26])
			#print(row[1])
		if row[26] == "y":
			Female_Artists.append(row[1])
	print(Female_Artists)

with open('Female_Artists.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ', quotechar=' ',
                      )
    writer.writerows(Female_Artists)



#problems: space between every letter, separating into two columns, want 'Vives, Carmen' to be in one column
		


