import os

for folder in range(0,3):
    os.makedirs(f"{folder}_dir")

for folder in range(0, 3):
    for subfolder in ['mon', 'tue', 'we']:
        os.makedirs(f"{folder}_dir/{subfolder}")
