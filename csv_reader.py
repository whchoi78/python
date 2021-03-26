import csv

with open('score.csv', 'r', encoding='utf-8') as csv_file:
    for line in csv_file:
        datas = line.strip().split(',')
        for data in datas:
            print(data, end="\t")
        print()

with open('score.csv', 'r', encoding='utf-8') as csv_file:
    csv_data = csv.reader(csv_file)
    for datas in csv_data:
        for data in datas:
            print(data, end="\t")
        print()

