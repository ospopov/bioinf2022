class Sequence():
    def __init__(self, seq, name_seq):
        self.seq = seq
        self.name = name_seq
        self.lenght = len(self.seq)
        self.alphabet = ['A', 'G', 'T', 'C']
        self.tebahpla = ['T', 'C', 'A', 'C']
        self.alphabet_rna = ['U', 'C', 'A', 'G']
        self.tebahpla_rna = ['A', 'G', 'U', 'C']
        self.mass = [135.13, 151.13, 126.11, 111.1]
        self.mass_rna = [112.086, 111.1, 135.13, 151.13]
        self.stat = dict({(i, self.seq.count(i)) for i in self.alphabet})
        self.stat_RNA = dict({(i, self.seq.count(i)) for i in self.alphabet_rna})

    def make_symmetrical(self):
        new_seq = str()
        for i in self.seq:
            new_seq += self.tebahpla[self.alphabet.index(i)]
        return Sequence(seq=new_seq, name_seq=self.name+'_sym')

    def mass_eval(self):
        mass_count = 0
        for i in self.alphabet:
            mass_count += self.mass[self.alphabet.index(i)] * self.stat[i]
        return mass_count

    def make_rna(self):
        new_seq = str()
        for i in self.seq:
            new_seq += self.alphabet_rna[self.alphabet.index(i)]
        return [new_seq, self.name+'_RNA']


class RNA_Sequence(Sequence):

    def make_symmetrical_RNA(self):
        new_seq = str()
        for i in self.seq:
            new_seq += self.alphabet_rna[self.tebahpla_rna.index(i)]
        return Sequence(seq=new_seq, name_seq=self.name + '_sym')

    def mass_eval_RNA(self):
        mass_count = 0
        for i in self.alphabet_rna:
            mass_count += self.mass_rna[self.alphabet_rna.index(i)] * self.stat_RNA[i]
        return mass_count


def rule(letter):
    inp = ["A", "T", "G", "C"]
    out = ["T", "A", "C", "G"]
    return out[inp.index(letter)]

def replace(seq):
    result = ""
    for letter in seq:
    result += rule(letter)
    return result

class Sequence:
    def new_rules(new_alpha):
        new_seq = str()
        for i in self.seq:
            new_seq += new_alpha[self.alphabet.index(i)]
        return new_seq

class Sequence:
    def new_rules_plus(new_alpha):
        new_seq = str()
        for i in self.seq:
            new_seq = new_seq[:-1]
            new_seq += new_alpha[self.alphabet.index(i)]
            new_seq = new_seq[:-1]
        new_seq = new_seq[-len(new_seq)+1:]
        return new_seq


