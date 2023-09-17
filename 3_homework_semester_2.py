# 1. написать скрипт на Python, который представляет пару вырожденных праймеров в виде регулярного выражения и ищет ампликоны в референсном геноме. Геном в формате FASTA

import re

from Bio import SeqIO

# Вырожденные праймеры
forward_primer = 'GAGCCTGCGTTCTTCGATGC'
reverse_primer = 'TTCTTCCGGCACGGAGTACT'

# Создаем регулярное выражение
primer_regex = re.compile(f'({forward_primer}|{reverse_primer})')

# FASTA-файл с референсным геномом
fasta_file = 'example.fasta'

# читаем FASTA-файла с помощью SeqIO
for record in SeqIO.parse(fasta_file, 'fasta'):
    genome_sequence = str(record.seq)
# Ищем все ампликонов с помощью регулярного выражения
    amplicons = primer_regex.findall(genome_sequence)
# Вывод найденных ампликонов
    for amplicon in amplicons:
        print(amplicon)
