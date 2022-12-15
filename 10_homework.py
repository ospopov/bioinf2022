string = input("Введите строку ")
kmer_size = int(input("Введите размер k-mera "))
if kmer_size > 11:
    print("Недопустимое значение")
else:
    result = []
    for i in range(len(string)):
        if len(string[i:i + kmer_size:]) == kmer_size:
            result.append(string[i:i + kmer_size:])
    print("kmer\tКол-во\tпервое\tпоследнее\tсреднее")
    for kmer in result:
        first = string.find(kmer)
        last = string.rfind(kmer)
        amount = string.count(kmer)
        print(f'{kmer}\t{first}\t{last}\t{amount}\t')