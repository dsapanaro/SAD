import csv
fieldnames = "RN", "WNAM", "", "LCN", "FRESCOSH", "BDATN", "BQN", "BQEN", "BDQN", "DDATN", "DQN", "DQEN", "DDQN", "OPRN", "OQN", "OOQN", "WDATES", "SDATN", "SDAT2N", "CENN", "CNUMN", "SCHN", "NSCHP","CLNON", "MEDN", "NBN", "UDATN", "FEM", "CLN", "UNCLN", "SUPN", "STAMPN", "UPN", "teaser", "SORTNAME", "FirstLetter","SEARCH","alts","","holdings","bestname","recid","notes","earliestdate","latestdate","latest","earliest","problem","teasterweb","event","more","teasterweb2","",""
with open("colon3_table_export2.csv", "r") as f:
	with open ("colon3_table_export_fresco.csv", "w") as h:

		colondictionary = csv.DictReader(f)
		# for row in colondictionary:
		# #	print(dict.items(row))
		writer = csv.DictWriter(h, fieldnames=fieldnames)
		headers = dict((n,n) for n in fieldnames)
		writer.writerow(headers)

		for a_row in colondictionary:
	 		writer.writerow(a_row)