import csv
from hdxsmooth import core

def load_fragment_file(path, time):
    with open(path, newline='') as file:
        reader = csv.reader(file, delimiter=';', quoting=csv.QUOTE_NONE)
        for i, row in enumerate(reader):
            if (i == 0): #header
                protein_names = row[3:]
                protein_fragments = [[] for _ in protein_names]
            else:
                if (row[2] == str(time)):
                    for i in range(len(protein_fragments)):
                        protein_fragments[i].append(core.Fragment(int(row[0]), int(row[1]), float(row[i + 3])))
    return(protein_fragments, protein_names)

def write_result_table(path, results, protein_names, time):
    if (len(results) != len(protein_names)):
        raise ValueError('Different numbers of proteins and protein names ({}) and ({})'.format(len(results), len(protein_names)))
    header = ['Position', 'Time(sec)'] + protein_names
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for position in results[0].keys():
            row = [position, time]
            for protein in results:
                row.append(protein[position])
            writer.writerow(row)