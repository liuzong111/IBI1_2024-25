seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
max_length = 0

for i in range(len(seq) - 1):
    if seq[i:i+2] == 'GT':
        for j in range(i+2, len(seq) - 1):
            if seq[j:j+2] == 'AG':
                intron_length = j + 2 - i
                if intron_length > max_length:
                    max_length = intron_length
                break  # Only consider the first "AG" after "GT"

print("Longest intron length:", max_length)
