#!python

"""
Python script to count the number of aminoacids or nucleotides per sequence in a FASTA file
Call it like so:
    python fasta_length.py sequences.fasta
"""

import sys

sequence_length = 0
fasta_sequence_lengths = []

# Getting the filename from the list of arguments
fasta_filename = sys.argv[1]

# Opening the file:
fastafile = open(fasta_filename, 'r') #'r' open it for reading

# Iterating over all lines in the file:
for line in fastafile.readlines():
    if line.startswith('>'):
        if sequence_length:
            fasta_sequence_lengths.append(sequence_length)
        sequence_length = 0
    else:
        sequence_length += len(line.strip())
fasta_sequence_lengths.append(sequence_length)

# Closing the file:
fastafile.close()

#print(sorted(fasta_sequence_lengths))

#print the maximmum length of sequences
#print(max(fasta_sequence_lengths))

#create a function which prints the sorted sequence length as well as 
# the max and min seq length

def sort_function(sequence):
	print(sorted(sequence))
	max_seq = max(sequence)
	min_seq = min(sequence)
	print(f"the maximum is {max_seq} and the minimum is {min_seq}")  

sort_function(fasta_sequence_lengths)


	
