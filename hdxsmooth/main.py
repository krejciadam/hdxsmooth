import sys, getopt
from hdxsmooth import io, core


def main(argv):
    infile = ''
    outfile = ''
    sequence_file = None
    times = None
    try:
        opts, args = getopt.getopt(argv, "i:o:t:s:", ["infile=", "outfile=", "times=", "sequence="])
    except getopt.GetoptError:
        print('Error. Invalid arguments')
        sys.exit(1)
    for opt, arg in opts:
        if opt in ("-i", "--infile"):
            infile = arg
        elif opt in ("-o", "--outfile"):
            outfile = arg
        elif opt in ("-t", "--times"):
            times = map(int, arg.split(','))
        elif opt in ("-s", "--sequence"):
            sequence_file = arg
    if len(outfile) < 1:
        print("Error. Output file not specified.")
        sys.exit(1)
    if len(infile) < 1:
        print("Error. Input file not specified.")
        sys.exit(1)
    try:
        if (sequence_file is not None):
            sequence = io.load_prolines_fasta(sequence_file)
            proline_positions = set(core.find_prolines(sequence))
            end = len(sequence)
        else:
            proline_positions = set([])
            end = None
        fragments_map, protein_names = io.load_fragment_file(infile, proline_positions, end)
        if times is None:
            times = fragments_map.keys()
        positions_map = {}
        for time in times:
            positions_map[time] = []
            for frag_set in fragments_map[time]:
                result = core.calculate_denaturation(frag_set)
                factor = core.get_scaling_factor(frag_set, result)
                result = {key:value * factor for key, value in result.items()}
                positions_map[time].append(result)
        io.write_result_table(outfile, positions_map, protein_names)
    except KeyError as e:
        print("Error. Time not defined in the data: {}".format(e))
        sys.exit(1)
    except FileNotFoundError as e:
        print("Error. File not found: " + str(e))
        sys.exit(1)
    except ValueError as e:
        print("Error while parsing input: " + str(e))
        sys.exit(1)
    except Exception as e:
        print("Error :{}".format(e))
        sys.exit(1)
    sys.exit(0)


