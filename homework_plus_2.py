#Написать программу, которая принимает на вход fastq файл и возвращает fastq файл, в котором прочтения отсортированы по среднему индексу качества на нуклеотид

def read_fastq(file_name):
    sequences = {}
    iter = 1
    with open(file_name, 'r') as file:
        for line in file:
            if iter == 4:
                iter = 1
                sequences[last_key].append(line.strip())
                continue
            if iter == 3:
                iter = 4
                continue
            if iter == 2:
                sequences[last_key].append(line.strip())
                iter = 3
                continue
            if iter == 1:
                sequences[line] = []
                last_key = line
                iter = 2
                continue
    return sequences


file_name = 'fastq_test_original.fastq'
sequences = read_fastq(file_name)

mean_fastq = {}

for seq_key in sequences.keys():
    mean_fastq[seq_key] = 0
    for i in range(len(sequences[seq_key][0])):
        mean_fastq[seq_key] += ord(sequences[seq_key][1][i]) - 33
    mean_fastq[seq_key] = mean_fastq[seq_key] / len(sequences[seq_key][0])

seq_order = list(mean_fastq.keys())

for i in range(len(seq_order)-1):
    for j in range(len(seq_order)-i-1):
        print((i/len(seq_order)-1) * (j / len(seq_order)-i-1))
        if mean_fastq[seq_order[j]] > mean_fastq[seq_order[j+1]]:
            seq_order[j], seq_order[j+1] = seq_order[j+1], seq_order[j]

with open("fasta_order.fastq", "w") as file:
    for line in seq_order[::-1]:
        file.write('>' + line + '\n')
        file.write(sequences[line][0] + '\n')
        file.write(sequences[line][1] + '\n')

with open("fasta_order_mean.fastq", "w") as file:
    for line in seq_order[::-1]:
        file.write('>' + line + '\n')
        file.write(sequences[line][0] + '\n')
        file.write(sequences[line][1] + '\n')
        file.write(str(mean_fastq[line]) + '\n')

