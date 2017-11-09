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

    protein_frags, protein_names = io.load_fragment_file(infile, time)
    res = [core.calculate_denaturation(frag_set) for frag_set in protein_frags]
    io.write_result_table(outfile, res, protein_names, time)

