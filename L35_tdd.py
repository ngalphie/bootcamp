import pytest
import bioinfo_dicts

def n_neg(seq):
    """Number of negative residues in a protein seqeunce."""
    seq=seq.upper()
    for aa in seq:
        if aa not in bioinfo_dicts.aa.keys():
            raise RuntimeError(aa + 'is not a valid amino acid.')
    # Count E's and D's and return Count
    return seq.count('D') + seq.count('E')
