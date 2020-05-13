import csv
import pandas as pd
'''
export_file = "Chicoria_Q1_BBALL.csv"
f = open(export_file, "w")

headers = "Game_ID,Player_ID,Player_Plus/Minus"
f.write(headers)
'''
output ={}

'''

data = pd.read_csv("Play_by_Play_Data_Sample.csv")

print(data.describe())
'''
with open("Game_LineUp_Data_Sample.csv", "r") as data_file:
	readCSV = csv.DictReader(data_file, delimiter = ',')

	for row in readCSV:
		games = output.get(row["Game_id"],dict())
		games[row["Person_id"]] = 0

		output[row["Game_id"]] = games




print(output)



#f.close()
