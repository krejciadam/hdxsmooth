# HDXsmooth
### Version 0.3
Calculate per-position deuteration levels from HDX (hydrogen-deuterium exchange) data.


## Description:
HDX data are measured per-fragment. This utility calculates the level of deuteration on each position of the protein. It uses deuteration levels of all the fragments. It also takes into the account the fact that N-termini of the fragments do not contribute to the fragments' deuteration levels.

## Installation:
    python3 setup.py build
    python3 setup.py install

## Synopsis:
    hdxmooth -i <input_file> -o <output_file> [options]

## Options:
    -t --times <time1,time2,time3...>: a comma-separated list of time points to process. Default: process all time points
    -p --protein <protein1,protein2,protein3...>: a comma-separated list of protein names to use. These must match input column names. Defautl: process all proteins

## Input
The software accepts .csv files containing exactly these columns in this order:

    From To Time Protein1_%deut Protein2_%deut ...
Multiple protein deuteration percentage columns can be present. Their names will be used to name the corresponding columns in the output. Other columns can have arbitrary names.

## Output
The output is a .csv file in the protienPilot format, i.e. with these columns:
