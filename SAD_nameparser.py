import csv
from nameparser import HumanName

FRESCO_list = []

with open("FRESCO_spanish_names.csv", "r", encoding="ISO-8859-1") as g:
	FRESCO_spanish_names = csv.reader(g)
	for row in FRESCO_spanish_names:
		FRESCO_list.append(row[0])


for x in FRESCO_list:
	FrescoName = HumanName(x)
	print(FrescoName.first)