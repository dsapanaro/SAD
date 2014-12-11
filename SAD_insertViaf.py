#if mapping quality is low
# and colon_name = row[1] of colon csv
# insert document[0]

import csv, json


# def compare(SADstring,FRESCOstring):
# #going to pass the SADstring to the function that will then perform levenstein matching/fuzzy match and 
# #want to break up each name string into words, then see if substrings are present, and what percentage of the words are the same.
# #might also want to explore breaking a name into its parts using nameparser and comparing those elements.
# #might also want to figure out how to tell the compare function to not take dates into account.

#     c = fuzz.token_set_ratio(SADstring, FRESCOstring)
#     #d = fuzz.ratio(SADstring,FRESCOstring)
#     if c > 90: #and d > 80:
#     	#print("high match:", SADstring, ":", FRESCOstring, c)
#     	return(FRESCOstring)
#     else:
#     	return(False)
#    #if it is a match, want to update
#    #should return LCSH or false

FRESCO_list = []
fieldnames = "RN", "WNAM", "", "LCN", "FRESCOSH", "VIAFLINK", "BDATN", "BQN", "BQEN", "BDQN", "DDATN", "DQN", "DQEN", "DDQN", "OPRN", "OQN", "OOQN", "WDATES", "SDATN", "SDAT2N", "CENN", "CNUMN", "SCHN", "NSCHP","CLNON", "MEDN", "NBN", "UDATN", "FEM", "CLN", "UNCLN", "SUPN", "STAMPN", "UPN", "teaser", "SORTNAME", "FirstLetter","SEARCH","alts","","holdings","bestname","recid","notes","earliestdate","latestdate","latest","earliest","problem","teasterweb","event","more","teasterweb2","",""
colondictionary_list = []
colon_name_list = []


with open("colon_results.json") as colon_json:
	colon_jason_data = json.load(colon_json)
	for colon_element in colon_jason_data:
		for el in colon_jason_data[colon_element]:
			if el == "colon_name":
				colon_name = colon_jason_data[colon_element][el]
	colon_name_list.append(colon_name)


with open("colon3_table_export3.csv", "r") as f:



	colondictionary = csv.DictReader(f)
	for row in colondictionary:

		colondictionary_item = row
		mainSADname = colondictionary_item["WNAM"]
		for colon_name in colon_name_list:
			if mainSADname == colon_name:
				for colon_element in colon_jason_data:
					for el in colon_jason_data[colon_element]:
						if el == "mapping":
							for value in colon_jason_data[colon_element]["mapping"]:
								mapping = value
								for map_el in mapping:
								 	if map_el == "Document":
								 		for document_value in mapping[map_el]:
								 			VIAF_id = document_value
								 			row["VIAFLINK"] = VIAF_id
								 			#print(row["VIAFLINK"])
		# print("got it")
		colondictionary_list.append(colondictionary_item)
		print(colondictionary_list)
		with open ("colon3_table_export_VIAFLINK.csv", "w") as h:

			writer = csv.DictWriter(h, fieldnames=fieldnames)
			headers = dict((n,n) for n in fieldnames)
			writer.writerow(headers)

			for a_row in colondictionary_list:
		 		writer.writerow(a_row)
