# 1. написать программу, которая читает файл в формате fasta и возвращает список последовательностей

def read_fasta(fasta_file):
    sequences = []
    with open(fasta_file) as file:
        seq = ''
        for line in file:
            if line.startswith('>'):
                if seq != '':
                    sequences.append(seq)
                    seq = ''
            else:
                seq += line.strip()
        sequences.append(seq)
    return sequences


fasta_address = input("Введите адрес fasta файла")
sequences = read_fasta(fasta_address)
print(sequences)
