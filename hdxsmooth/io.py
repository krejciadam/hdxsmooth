import csv
from hdxsmooth import core


def load_csv_input(path):
    protein_fragments = {}
    proline_positions = set()
    with open(path, newline=None) as file:
        next(file, None)  # skip header
        reader = csv.reader(file, delimiter=',', quoting=csv.QUOTE_NONE)
        for row in reader:
            protein, start, end, seq, time, deut = row[0], int(row[1]), int(row[2]), row[3], int(row[4]), float(row[7])
            positions = list(range(start + 1, end + 1)) #start + 1 because N-terminus does not count
            for i, letter in enumerate(seq):
                if letter == "P":
                    proline_positions.add(start + i)
                    if i > 0:
                        del(positions[i - 1])
            fragment = core.Fragment(positions, deut)
            if time not in protein_fragments.keys():
                protein_fragments[time] = {protein:[fragment]}
            elif protein not in protein_fragments[time].keys():
                protein_fragments[time][protein] = [fragment]
            else:
                protein_fragments[time][protein].append(fragment)
    return protein_fragments



def load_fragment_file(path, proline_positions = set([]), protein_end=None):
    with open(path, newline=None) as file:
        reader = csv.reader(file, delimiter=';', quoting=csv.QUOTE_NONE)
        for i, row in enumerate(reader):
            if i == 0: #header
                protein_names = row[3:]
                protein_fragments = {}
            else:
                time = int(row[2])
                if time not in protein_fragments.keys():
                    protein_fragments[time] = [[] for _ in protein_names]
                for i in range(len(protein_names)):
                    start, end = int(row[0]), int(row[1])
                    deuteration = float(row[i + 3])
                    if deuteration < 0:
                        raise ValueError('Negative deuteration level ({})'.format(deuteration))
                    if start >= end:
                        raise ValueError('Fragment start ({}) is greater than end ({})'.format(start, end))
                    if protein_end is not None and end > protein_end:
                        raise ValueError('Fragment end ({}) is greater than total protein length ({})'.format(end, protein_end))
                    positions = set(range(start + 1, end + 1)) #start + 1 because N-terminus does not count
                    positions = positions - proline_positions
                    protein_fragments[time][i].append(core.Fragment(positions, deuteration))
    return(protein_fragments, protein_names)


def load_prolines_fasta(path):
    sequence = ''
    with open(path) as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if not (line.startswith('>')):
                sequence += line
    return sequence


def write_result_table(path, time_map, protein_names):
    header = ['Position', 'Time(sec)'] + protein_names
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for time, position_map_list in time_map.items():
            for position in position_map_list[0].keys():
                row = [position, time]
                for position_map in position_map_list:
                    row.append(position_map[position])
                writer.writerow(row)