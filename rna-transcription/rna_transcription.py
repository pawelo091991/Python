data = {'C': 'G',
        'G': 'C',
        'T': 'A',
        'A': 'U'}


def to_rna(dna_strand):
    result = ''
    for letter in dna_strand:
        result += data[letter]

    return result
