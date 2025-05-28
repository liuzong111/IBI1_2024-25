# to read the fasta sequence of aminio acids(SOD2) from files
# and compare the similarity between human, mouse and a random sequence
with open('SOD2.fasta', 'r') as f:
    seq_human = f.read().splitlines()[1:]  # read the sequence of human SOD2
    seq_human = ''.join(seq_human)  # join the sequence into a single string
with open('mouse_SOD2.fasta', 'r') as f:
    seq_mouse = f.read().splitlines()[1:]  # read the sequence of mouse SOD2
    seq_mouse = ''.join(seq_mouse)  # join the sequence into a single string
with open('random.fasta', 'r') as f:
    seq_random = f.read().splitlines()[1:]  # read the sequence of random SOD2
    seq_random = ''.join(seq_random)  # join the sequence into a single string


from Bio.Align import substitution_matrices
blosum62 = substitution_matrices.load("BLOSUM62")
diff_count1 = 0
score1 = 0
for i in range(len(seq_human)):
    if seq_human[i] != seq_mouse[i]:
        diff_count1 += 1
    score1 += blosum62[seq_human[i], seq_mouse[i]]
print(
    f'The similarity rate betweeen human and mouse SOD2 is {(1-diff_count1/len(seq_human))*100:.2f}% and the score is {score1}.')

diff_count2 = 0
score2 = 0
for i in range(len(seq_human)):
    if seq_human[i] != seq_random[i]:
        diff_count2 += 1
    score2 += blosum62[seq_human[i], seq_random[i]]
print(
    f'The similarity rate betweeen human and random SOD2 is {(1-diff_count2/len(seq_human))*100:.2f}% and the score is {score2}.')
diff_count3 = 0
score3 = 0
for i in range(len(seq_mouse)):
    if seq_mouse[i] != seq_random[i]:
        diff_count3 += 1
    score3 += blosum62[seq_mouse[i], seq_random[i]]
print(
    f'The similarity rate betweeen mouse and random SOD2 is {(1-diff_count3/len(seq_mouse))*100:.2f}% and the score is {score3}.')
