import csv

f = open('apt-data.csv','r')
rdr = csv.reader(f)

min_apt=''
min = 0

for line in rdr:
    if "부평" in line[0]:
        a=int(line[8].replace(",",""))
    if min == 0 or a < min:
        min_apt = line[4]

        
'''
def smallest_value(reader: TextIO) -> int:
    line = time_series.skip_header(reader)
    smallest = int(line)

    for line in reader:
        value = int(line.strip())
        if value < smallest:
            smallest = value
    return smallest
'''
f.close()        
                