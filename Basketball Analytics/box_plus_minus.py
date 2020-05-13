import csv
import pandas as pd
'''
export_file = "Chicoria_Q1_BBALL.csv"
f = open(export_file, "w")

headers = "Game_ID,Player_ID,Player_Plus/Minus"
f.write(headers)
'''
data = pd.read_csv("Play_by_Play_Data_Sample.csv")

print(data.describe())
'''
with open("Play_by_Play_Data_Sample.csv") as csvfile:
	readCSV = csv.reader(csvfile, delimiter = ',')

	for row in readCSV:
		for game in row[0]:




f.close()
'''