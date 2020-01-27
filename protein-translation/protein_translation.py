data = {'AUG': 'Methionine',
        'UUU': 'Phenylalanine',
        'UUC': 'Phenylalanine',
        'UUA': 'Leucine',
        'UUG': 'Leucine',
        'UCU': 'Serine',
        'UCC': 'Serine',
        'UCA': 'Serine',
        'UCG': 'Serine',
        'UAU': 'Tyrosine',
        'UAC': 'Tyrosine',
        'UGU': 'Cysteine',
        'UGC': 'Cysteine',
        'UGG': 'Tryptophan',
        'UAA': 'STOP',
        'UAG': 'STOP',
        'UGA': 'STOP'
        }


def proteins(strand):
    result = []
    strand_range = int(len(strand)/3)
    for i in range(strand_range):
        code = strand[i*3:i*3+3]
        if code in data:
            if data[code] is 'STOP':
                break
            result.append(data[code])

    return result
