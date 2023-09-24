#Написать программу, которая получает на вход fastq файл с прочтениями illumina, и порог качества, и возвращает fasta файл, в котором прочтения обрезаны с концов, если концевые нуклеотиды ниже порога качества, и в которых нуклеотиды внутри прочтения, не проходящие порог качества, заменены на N.

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


quality_score = 30
file_name = 'fastq_test.fastq'
sequences = read_fastq(file_name)
sequences_fasta = {}

for seq_key in sequences.keys():
    start_index = 0
    end_index = 0
    for i in range(len(sequences[seq_key][0])):
        if ord(sequences[seq_key][1][i]) - 33 < quality_score:
            sequences[seq_key][0] = sequences[seq_key][0][:i] + "N" + sequences[seq_key][0][i+1:]
            if start_index == i-1:
                start_index = i
        else:
            end_index = i
    sequences_fasta[seq_key] = sequences[seq_key][0][start_index+1:end_index+1]

with open("fasta_test.fasta", "w") as file:
    for line in sequences_fasta.keys():
        file.write('>' + line + '\n')
        file.write(sequences_fasta[line]+ '\n')


