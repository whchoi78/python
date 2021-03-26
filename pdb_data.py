from typing import TextIO
from io import StringIO

def read_molecule(reader: TextIO) -> list:
    line = reader.readline()
    if not line:
        return None
    parts = line.split()
    name = parts[1]
    molecule = [name]

    reading = True
    while reading:
        line = reader.readline()
        if line.startswith('END'):
            reading = False
        else:
            parts = line.split()
            molecule.append(parts[2:])
    return molecule

def read_all_molecules(reader: TextIO) -> list:
    result = []

    reading = True
    while reading:
        molecule = read_molecule(reader)
        if molecule:
            result.append(molecule)
        else:
                reading = False
    return result

if __name__ == "__main__":
    molecule_file = open('multimole.pdb.txt', 'r')
    molecules = read_all_molecules(molecule_file)
    molecule_file.close()
    print(molecules)    

