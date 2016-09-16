import pytest
import bioinfo_dicts

def find_codon_lesson6(codon, seq):
    """Find a specified codon with a given sequence."""

    i = 0
    # Scan sequence until we hit the start codon or the end of the sequence
    while seq[i:i+3] != codon and i < len(seq):
        i += 1

    if i == len(seq):
        return -1

    return i
