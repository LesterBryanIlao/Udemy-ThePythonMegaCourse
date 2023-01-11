import glob
import re

txt_files = glob.glob('The_Basics\section34\*.txt')

myList=[]
for file in txt_files:
    with open(file, 'r') as f:
        for line in f:
            myList.append(f.readlines())
            
all_lines = sum(myList, [])
matches = [re.compile("[0-9]+\.*[0-9]*").search(line) for line in all_lines]

numbers = [float(match.group(0)) for match in matches if match]
mean = sum(numbers)/len(numbers)

with open("mean.txt", "w") as file:
    file.write(str(mean)) 
