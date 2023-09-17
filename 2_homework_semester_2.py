# 2. написать программу, которая читает файл в формате fasta с последовательностями ДНК, находит в них все неперекрывающиеся рамки считывания и записывает соответствующие им белки в отдельные файлы в заданной директории

import os

def read_fasta(fasta_file):
    sequences = {}
    with open(fasta_file) as file:
        seq = ''
        for line in file:
            if line.startswith('>'):
                sequences[line.strip().split(" ")[0]] = ""
                seq_id = line.strip().split(" ")[0]
            else:
                sequences[seq_id] += line.strip()
    return sequences


sequences = read_fasta("F:\sequence_input.fasta")
sequences_orf = {i: [] for i in list(sequences.keys())}

for key in sequences.keys():
    seq = sequences[key]
    while seq[seq.find("ATG"):] != -1:
        seq = seq[seq.find("ATG"):]
        stop_index = [float("inf")]
        for stop_codon in ["TAA", "TAG", "TGA"]:
            if seq.find(stop_codon) % 3 == 0:
                stop_index += seq.find(stop_codon)
        if  min(stop_index) == float("inf"):
            break
        sequences_orf[key].append(seq[0: min(stop_index) + 3])
        seq = seq[min(stop_index) + 3:]

for key in sequences_orf.keys():
    for i in sequences_orf[key]
        f_name = f"{key}_orf{sequences_orf[key].index(i)}.fasta"
        f_path = os.path.join(output_dir, f_name)
        with open(f_path, "w") as f:
            f.write(f">pro {sequences_orf[key].index(i)}\n{i}\n")


