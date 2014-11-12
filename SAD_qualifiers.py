# find term exh. in OQN
# put artist name in column A
# if there's a value in BDATN, put that in column B and OPRN in column C
# if there's a value in DDATN, put OPRN in column B and DDATN in column C
# REG EXPRESSIONS:
# if there's a ], include only the number
# if there's a 4 dig number and then a -, put the first 4 digit number in column B, put the second 4 digit number in column C

import csv
import re
p = re.compile("\]")
q = re.compile("\-")

with open("colon3_table_export.csv", "r") as f:

	date_qualifiers_range = []
	date_qualifiers = []
	data = []

	reader = csv.reader(f)
	for row in reader:
		row[12] = p.sub("", row[12])
		#row[12] = q.sub(",", row[12])
		#use a split function from CSV module to split row 12? how to split the date ranges
		#that end up in row 12 into two separate rows?
		if row[13] == "exh." or row[13] == "[exh." and row[13] != "":
			date_qualifiers.append([row[1], row[12]])
			#data.append(row)
			#print(data)
		# if row[13] == "exh." or "[exh.":
			if row[4] != "":
				date_qualifiers_range.append([row[1], row[4], row[12]])
			elif row[4] == "" and row[8] != "":
				date_qualifiers_range.append([row[1], row[12], row[8]])
	# for date_cell in date_qualifiers:
	# 	#print(date_cell)
	# 	for s in date_cell:
	# 		s = p.sub("", s)
	# 		s = q.sub(",",s)
	# 		date_qualifiers = [[s]]
	# 		print (date_qualifiers)
#how do i get these cleaned values back into the date_qualifiers list?

# with open('data.csv', 'w') as csvfile:	
# 	writer = csv.writer(csvfile)
# 	for a_row in data:
# 		writer.writerow(a_row)

			with open('date_qualifiers.csv', 'w') as csvfile:	
				writer = csv.writer(csvfile)
				for a_row in date_qualifiers:
					writer.writerow(a_row)

# with open('date_qualifiers_range.csv', 'w') as csvfile:	
# 	writer = csv.writer(csvfile)
# 	for a_row in date_qualifiers_range:
# 		writer.writerow(a_row)