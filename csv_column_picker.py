#!/bin/python3

import os, re, sys, csv
import argparse

parser = argparse.ArgumentParser(description="input: input_csv output_file list_of_cols")

parser.add_argument('csv_file', help='name of the input csv file')
parser.add_argument('output_file', help='name of the output file')
parser.add_argument('cols', nargs='+', type=int, help='choose the column numbers you wish to extract, first col is 0.')

args = parser.parse_args()
csv_file = args.csv_file
output_file = args.output_file
included_cols = args.cols

with open(csv_file, 'r') as csvfile, open(output_file, 'w') as outfile:
    reader = csv.reader(csvfile)
    num_cols = len(next(reader))
    csvfile.seek(0)

    print("Print columns",included_cols," from",csv_file,"to",output_file)

    for row in reader:
        content = list(row[i] for i in included_cols)
        outfile.write(', '.join(map(str,content))+'\n')
        # print(', '.join(map(str,content)))