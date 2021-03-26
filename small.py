from typing import TextIO
from io import StringIO
import time_series

def smallest_value(reader: TextIO) -> int:
    line = time_series.skip_header(reader)
    smallest = int(line)

    for line in reader:
        value = int(line.strip())
        if value < smallest:
            smallest = value
    return smallest

def smallest_value_skip(reader: TextIO) -> int:
    line = time_series.skip_header(reader)
    smallest = int(line)

    for line in reader:
        line = line.strip()
        if line != '-':
            value = int(line)
            smallest = min(smallest, value)
    
    return smallest        

if __name__ == "__main__":
    with open ('hopedale.txt', 'r') as input_file:
        print(smallest_value(input_file))
        print(smallest_value_skip(input_file))

