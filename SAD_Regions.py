import csv

with open("colon3_table_export.csv", "r") as f:

	Spanish_Regions = []

	reader = csv.reader(f)
	for row in reader:
		Spanish_Regions.append([row[1],row[20]])
			
with open('Regions.csv', 'w') as csvfile:	
	writer = csv.writer(csvfile)
	for a_row in Spanish_Regions:
    	writer.writerow(a_row)



