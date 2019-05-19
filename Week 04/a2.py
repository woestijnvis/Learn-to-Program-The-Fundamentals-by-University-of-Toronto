def get_length(dna):
    """ (str) -> int

    Return the length of the dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if dna1 is longer than dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if get_length(dna1) > get_length(dna2):
        return True
    else:
        return False


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if dna2 occurs in the dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    """
    if dna2 in dna1:
        return True
    else:
        return False


def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if dna contains the characters A, C, G and T.

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('BUGGCa')
    False
    """
    character_count = 0

    for character in dna:
        if character not in 'ATCG':
            character_count = character_count + 1
    if character_count < 1:
        return True
    else:
        return False


def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    Return new_dna_sequence by inserting dna2 into dna1 at the given index.

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('CGGC', 'GT', 3)
    'CGGGTC'
    """
    new_dna_sequence = dna1[:index] + dna2[:] + dna1[index:]
    return new_dna_sequence


def get_complement(nucleotide):
    """ (str) -> str

    Return the complement of the given nucleotide.

    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'
    """
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'
    elif nucleotide == 'T':
        return 'A'
    else:
        return ''


def get_complementary_sequence(dna_sequence):
    """ (str) -> str

    Return the complement of the given dna_sequence.

    >>> get_complementary_sequence()
    output
    >>> get_complementary_sequence()
    output
    """
    new_sequence = ''

    for character in dna_sequence:
        new_sequence = new_sequence + get_complement(character)
    return new_sequence
