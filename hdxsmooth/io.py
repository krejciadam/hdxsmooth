import csv
from hdxsmooth import core


def load_csv_input(path):
    protein_fragments = {}
    protein_names = []
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
            if protein not in protein_names:
                protein_names.append(protein)
            fragment = core.Fragment(positions, deut)
            if time not in protein_fragments.keys():
                protein_fragments[time] = {protein:[fragment]}
            elif protein not in protein_fragments[time].keys():
                protein_fragments[time][protein] = [fragment]
            else:
                protein_fragments[time][protein].append(fragment)
    return protein_fragments, protein_names, proline_positions


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