import csv
 
with open('input_data.txt', 'r', encoding='utf-8') as input_file, \
    open('output_data.csv', 'w', newline='', encoding='utf-8') as output_file:
    
    lines = input_file.readlines()
 
    # 출력될 데이터를 담을 리스트
    csv_format = []
    for line in lines:
        csv_format.append(line.strip().split())
 
    csvobject = csv.writer(output_file)
    csvobject.writerows(csv_format)
