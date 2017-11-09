# HDXsmooth
Calculate per-position deuteration levels from HDX (hydrogen-deuterium exchange) data.

## Description:
HDX data are measured per-fragment. This utility calculates the level of deuteration on each position of the protein. It uses deuteration levels of all the fragments. It also takes into the account the fact that C-termini of the fragments do not contribute to the fragments' deuteration levels.

## Installation:
    python3 setup.py build
    python3 setup.py install

## Synopsis:
    hdxmooth -i <input_file> -o <output_file> -t <time>

## Input
The software accepts .csv files in the protienPilot format, i.e. with these columns:

    From To Time Protein1_deut Protein2_deut ...
all the protein deuteration columns will be included in the output.
