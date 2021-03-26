from typing import TextIO
from io import StringIO

def skip_header(reader: TextIO) -> str:
    line = reader.readline()
    line = reader.readline()
    while line.strip().startswith("#"):
        line = reader.readline()
    return line

def process_file(reader: TextIO) -> None:
    line = skip_header(reader).strip()
    print(line)
    for line in reader:
        line = line.strip()
        print(line)

if __name__ == "__main__":
    with open('hopedale.txt', 'r') as input_file:    
        process_file(input_file)