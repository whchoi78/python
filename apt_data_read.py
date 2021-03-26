import csv

dat1_list = [] 
dat2_list = [] 
with open('apt-data.csv', 'r') as raw: 
    reader = csv.reader(raw) 
    for lines in reader: 
        print(lines) 
        dat1_list.append(lines) 
        start = len(dat2_list) 
        dat2_list[start:start] = lines
