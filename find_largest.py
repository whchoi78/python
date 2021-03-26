from typing import TextIO
from io import StringIO
import time_series

def find_largest(line: str) -> int:
    largest = -1
    for value in line.split():
        value = int(value[:-1])
    if value > largest :
        largest = value

    return largest

def process_file(reader: TextIO) -> int:
    line = time_series.skip_header(reader)            

    largest = find_largest(line)

    for line in reader:
        large = find_largest(line)
        if large > largest:
            largest = large
    return largest

if __name__ == "__main__":
    with open('laxy.txt', 'r') as input_file:
        print(process_file(input_file))
