# the code aims to detect the restriction enzyme cut site in a given DNA sequence.
# and show the position of all of the cut sites.
# the code contains several checks to ensure the security
# the code is written in python 3.10.0
# the code is written by using the python programming language
import re


def find_cut_site(dna_sequence, enzyme_sequence):
    # Find the position of the enzyme sequence in the DNA sequence
    position = dna_sequence.find(enzyme_sequence)
    # to check if the sequence is valid
    if re.match("^[ATCG]*$", dna_sequence):
        if position != -1:
            return position + 1
        else:
            print("Enzyme sequence not found in the DNA sequence.")
            return None
    else:
        print("Invalid DNA sequence. Please enter a valid DNA sequence.")
        return None


def find_cut_site(dna_sequence, enzyme_sequence):
    # Find the position of the enzyme sequence in the DNA sequence
    position = re.finditer(fr'{enzyme_sequence}', dna_sequence)
    # to check if the sequence is valid
    if re.match("^[ATCG]*$", dna_sequence):
        if re.match("^[ATCG]*$", enzyme_sequence):
            if position:
                list = []
                for i in position:
                    list.append(i.start() + 1)
                return list
        else:
            print("Enzyme sequence not found in the DNA sequence.")
            return None
    else:
        print("Invalid DNA sequence. Please enter a valid DNA sequence.")
        return None


dna_sequence = input("Enter the DNA sequence: ")
enzyme_sequence = input("Enter the enzyme sequence: ")
cut_site_position = find_cut_site(dna_sequence, enzyme_sequence)
print("The cut site position is:", cut_site_position)
# example of the code
# Enter the DNA sequence: ATCGATCGATCG
# Enter the enzyme sequence: CGAT
# The cut site position is: 3 7
