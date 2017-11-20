# HDXsmooth
### Version 0.4
Calculate per-position deuteration levels from HDX (hydrogen-deuterium exchange) data.


## Description:
HDX data are measured per-fragment. This utility calculates the level of deuteration at each position of the protein.
It uses deuteration levels of all the fragments. It also takes into the account the fact that N-termini of the
fragments do not contribute to the deuteration levels, as well as proline residues.

## Installation:
    python3 setup.py build
    python3 setup.py install

## Synopsis:
    hdxmooth -i <input_file> -o <output_file> [options]

## Options:
    -t --times <time1,time2,time3...>: a comma-separated list of time points to process. Default: process all time points
    -p --protein <protein1,protein2,protein3...>: a comma-separated list of protein names to use. These must match input column names. Defautl: process all proteins
    -d --delimiter <delimiter>: a delimiter to be used in both input and output .csv files. Default: comma (,)

## Input
The software accepts .csv files containing exactly these columns in this order:

    Protein,Start,End,Sequence,Deut Time (sec),maxD,#D,%D,Conf Interval (#D),#Pts,Confidence,Stddev,p
Columns can have arbitrary names.

## Output
The output is a .csv file with these columns:

    Position,Time(sec),protein1,protein2,...
