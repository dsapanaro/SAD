import csv

with open("colon3_table_export.csv", "r") as f:

	Female_Artists = []

	reader = csv.reader(f)
	for row in reader:
		#print (row[1] + row[26])
			#print(row[1])
		if row[26] == "y" or "Y":
			Female_Artists.append(row[1])
	#print(Female_Artists)

with open('Female_Artists.csv', 'w') as csvfile:
    writer = csv.writer(csvfile.excel class='excel_tab')
    writer.writerows(Female_Artists)



#problems: space between every letter, separating into two columns, want 'Vives, Carmen' to be in one column
#excel_tab and excel might be possible solutions 
#dialect='excel_tab'
#class='excel'