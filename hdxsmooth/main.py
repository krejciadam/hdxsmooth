import sys, getopt
from hdxsmooth import io, core


def main(argv):
    infile = ''
    outfile = ''
    time = None
    try:
        opts, args = getopt.getopt(argv, "i:o:t:", ["infile=", "outfile=", "time="])
    except getopt.GetoptError:
        print('Error. Invalid arguments')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-i", "--infile"):
            infile = arg
        elif opt in ("-o", "--outfile"):
            outfile = arg
        elif opt in ("-t", "--time"):
            time = int(arg)
    if (len(outfile) < 1):
        print("Error. Output file not specified.")
        exit(2)
    if (len(infile) < 1):
        print("Error. Input file not specified.")
        exit(2)
    if (time is None):
        print("Error. Time not specified.")
        exit(2)

    fragments_map, protein_names = io.load_fragment_file(infile)
    positions_map = {}
    for time, protein_fragments in fragments_map.items():
        positions_map[time] = [core.calculate_denaturation(frag_set) for frag_set in protein_fragments]
    io.write_result_table(outfile, positions_map, protein_names)

