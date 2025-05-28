

import re

# Define regex pattern for TATA-box
tata_pattern = re.compile(r'TATA[AT]A[AT]')


def read_fasta(file_path):
    genes = {}
    gene_name = None
    seq_lines = []
    with open(file_path, 'r') as f:
        #   FOR each line in the file:
        #       TRIM whitespace from line
        #       IF line starts with ">":
        #           IF gene_name is not None and sequence_lines is not empty:
        #               COMBINE sequence_lines and add entry to genes with key gene_name
        #           EXTRACT gene_name from the line (e.g., the part after ">" until the first space)
        #           RESET sequence_lines to empty list
        #       ELSE:
        #           APPEND line to sequence_lines
        #   AFTER loop, add the last gene entry to genes if present
        #   RETURN genes
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if gene_name is not None and seq_lines:
                    genes[gene_name] = ''.join(seq_lines)
                # Extract gene name from header (assuming gene name is the first word after '>')
                gene_name = line[1:].split()[0]
                seq_lines = []
            else:
                seq_lines.append(line)
    if gene_name is not None and seq_lines:
        genes[gene_name] = ''.join(seq_lines)
    return genes


# Set the input FASTA file name (modify the file path if necessary)
input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
genes = read_fasta(input_file)

# Write genes containing TATA-box to a new FASTA file
with open("tata_genes.fa", 'w') as out:
    for gene, seq in genes.items():
        if tata_pattern.search(seq):
            out.write(f">{gene}\n")
            out.write(seq + "\n")
