import csv

with open("colon3_table_export.csv", "r") as f:

	Artists_Name = []
	Artists_Gender = []

	reader = csv.reader(f)
	for row in reader:
		Artist_Name = row[1]
		Artists_Name.append(Artist_Name)
		Artist_Gender = row[26]
		Artists_Gender.append(Artist_Gender)	
	

with open('Female_Artists.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, dialect='excel-tab', newline=' ')
    writer.writerows(Artists_Name)
    writer.writerows(Artists_Gender)
    #NEED to make separate column 


#problems: space between every letter, separating into two columns, want 'Vives, Carmen' to be in one column
#excel_tab and excel might be possible solutions 
