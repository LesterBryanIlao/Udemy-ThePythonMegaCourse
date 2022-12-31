import time
import os
import sys
import pandas

file_location = r"C:\Users\ilale\Personal\Python\ThePythonMegaCourse\The_Basics\files\fruits.txt"
file_location_veggies = r"C:\Users\ilale\Personal\Python\ThePythonMegaCourse\The_Basics\files\vegetables.txt"
file_location_temps_today = r"C:\Users\ilale\Personal\Python\ThePythonMegaCourse\The_Basics\files\temps_today.csv"

while True:
    if os.path.exists(file_location_temps_today):
        with open(file_location_temps_today) as file:
            data = pandas.read_csv(file_location_temps_today)
            print(data.mean()['st1'])
    else: 
        print("File not found.")
    time.sleep(5)

