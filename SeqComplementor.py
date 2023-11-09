#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SeqComplementor.py - Program to convert DNA/RNA sequence to complement sequence
"""

import sys, signal
sys.dont_write_bytecode = True
signal.signal(signal.SIGINT, signal.SIG_DFL)

import argparse
import pandas as pd

from func_prompt_io import check_exist, check_overwrite


# =============== constant =============== #
BASEPAIR = {
	"DNA": {
		"DNA": {
			"A": "T",
			"C": "G",
			"G": "C",
			"T": "A",
		},
		"RNA": {
			"A": "U",
			"C": "G",
			"G": "C",
			"T": "A",
		},
	},
	"RNA": {
		"DNA": {
			"A": "T",
			"C": "G",
			"G": "C",
			"U": "A",
		},
		"RNA": {
			"A": "T",
			"C": "G",
			"G": "C",
			"U": "A",
		},
	},
}



# =============== function =============== #
def read_list(input_file):
	"""
	Function to read csv

	Args:
		input_file (str): sequence list file with header

	Returns:
		pd.DataFrame
	"""
	df = pd.read_csv(input_file, header=0)
	return df


def convert_complementary(list_sequence, sequence_type_input, sequence_type_output, do_reverse=False):
	list_complementary = []
	basepair = BASEPAIR[sequence_type_input][sequence_type_output]
	for sequence in list_sequence:
		complementary = []
		for base in list(sequence):
			complementary.append(basepair[base])

		if do_reverse:
			complementary = reversed(complementary)

		list_complementary.append("".join(complementary))

	return list_complementary



# =============== main =============== #
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Program to convert DNA/RNA sequence to complement sequence", formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument("-i", dest="INPUT_FILE", metavar="INPUT.csv", required=True, help="sequence list file")
	parser.add_argument("-o", dest="OUTPUT_FILE", metavar="OUTPUT.csv", required=True, help="output file")
	parser.add_argument("-ti", dest="SEQUENCE_TYPE_INPUT", metavar="SEQUENCE_TYPE_INPUT", choices=["DNA", "RNA"], required=True, help="sequence type for input")
	parser.add_argument("-to", dest="SEQUENCE_TYPE_OUTPUT", metavar="SEQUENCE_TYPE_OUTPUT", choices=["DNA", "RNA"], required=True, help="sequence type for output")
	parser.add_argument("-r", dest="DO_REVERSE", action="store_true", default=False, help="reverse complementary sequence (output sequence order is 5' to 3'-terminal)")
	parser.add_argument("-O", dest="FLAG_OVERWRITE", action="store_true", default=False, help="overwrite forcibly")
	args = parser.parse_args()

	check_exist(args.INPUT_FILE, 2)

	df = read_list(args.INPUT_FILE)
	if "Sequence" not in df.columns:
		sys.stderr.write("ERROR: `{}` has not header with `Sequence`.\n")
		sys.exit(1)

	list_sequence = convert_complementary(df.loc[:,"Sequence"].values, args.SEQUENCE_TYPE_INPUT, args.SEQUENCE_TYPE_OUTPUT, args.DO_REVERSE)
	new_column = "Complementary (3' -> 5')"
	if args.DO_REVERSE:
		new_column = "Complementary (5' -> 3')"
	df.loc[:,new_column] = list_sequence

	if args.FLAG_OVERWRITE == False:
		check_overwrite(args.OUTPUT_FILE)

	df.to_csv(args.OUTPUT_FILE, header=True, index=False)
