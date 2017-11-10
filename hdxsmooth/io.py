import csv
from hdxsmooth import core


def load_fragment_file(path):
    with open(path, newline='') as file:
        reader = csv.reader(file, delimiter=';', quoting=csv.QUOTE_NONE)
        for i, row in enumerate(reader):
            if (i == 0): #header
                protein_names = row[3:]
                protein_fragments = {}
            else:
                time = int(row[2])
                if (time not in protein_fragments.keys()):
                    protein_fragments[time] = [[] for _ in protein_names]
                for i in range(len(protein_names)):
                    protein_fragments[time][i].append(core.Fragment(int(row[0]), int(row[1]), float(row[i + 3])))

    return(protein_fragments, protein_names)


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