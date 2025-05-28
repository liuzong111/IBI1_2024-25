import re
import sys

# Define acceptable splice combinations
splice_options = ["GTAG", "GCAG", "ATAC"]

# Prompt the user for splice combination input
splice_combination = input(
    "Please enter a splice donor/acceptor combination (GTAG, GCAG, ATAC): ").strip().upper()

# Extract the splice donor and acceptor from the user input
# First two characters represent the donor site
splice_donor = splice_combination[:2]
# Last two characters represent the acceptor site
splice_acceptor = splice_combination[2:]


tata_pattern = re.compile(r'TATA[AT]A[AT]')

# Specify the input FASTA file containing gene sequences
input_filename = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"

# Define the output file, naming it based on the splice combination
output_filename = f"{splice_combination}_spliced_genes.fa"

# Open the input FASTA file for reading and the output file for writing
with open(input_filename, 'r') as fasta_file, open(output_filename, 'w') as out_file:
    gene_name = None  # Variable to store the current gene's name
    gene_seq = ""  # Variable to accumulate the sequence of the current gene

    # Read the input file
    for line in fasta_file:
        if line.startswith(">"):  # Check if the line is a gene identifier
            # If there is a previously read gene, process it
            if gene_name and tata_pattern.search(gene_seq):
                # Count TATA boxes in the sequence
                tata_count = len(tata_pattern.findall(gene_seq))

                # Check if the sequence contains the splice donor and acceptor
                if re.search(splice_donor + r".+" + splice_acceptor, gene_seq):
                    out_file.write(
                        f">{gene_name} TATA count: {tata_count}\n{gene_seq}\n")

            # Extract the gene name from the identifier line
            gene_name = re.search(r'gene:(\S+)', line)
            if gene_name:
                gene_name = gene_name.group(1)  # Get the actual gene name
            gene_seq = ""  # Reset the sequence for the next gene

        else:  # If it's not a gene identifier line, it must be a sequence line
            gene_seq += line.strip()  # Append the sequence to gene_seq

    # Process the last gene in the file (if any)
    if gene_name and tata_pattern.search(gene_seq):
        tata_count = len(tata_pattern.findall(gene_seq))

        # Check if the sequence contains the splice donor and acceptor
        if re.search(splice_donor + r".+" + splice_acceptor, gene_seq):
            out_file.write(
                f">{gene_name} TATA count: {tata_count}\n{gene_seq}\n")
