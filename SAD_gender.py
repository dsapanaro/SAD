import csv

with open("colon3_table_export.csv", "r") as f:

	Artists_Everything= []

	reader = csv.reader(f)
	for row in reader:
		Artists_Everything.append([row[1], row[26]])

with open('Female_Artists.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for a_row in Artists_Everything:
    	writer.writerow(a_row)
    	#print(a_row)

    
    
 
