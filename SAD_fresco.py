#establish match between main name and FRESCO subject heading.
#use two csv files
#loop through each file, and if the name is the same
#then I want to pull out the FRESCO name and insert it into the LC name column in the CSV.
#how can i determine probable but not exact matches? looking for similarity.

import csv

with open("colon3_table_export.csv", "r") as f:


#eventually need to write back into this CSV, and tell it exactly where to write the new column