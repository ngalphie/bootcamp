import bioinfo_dicts

def one_to_three(seq):
    seq=seq.upper()

    #Build conversion
    aa_list = []
    for amino_acid in seq:
        if amino_acid in bioinfo_dicts.aa.keys():
            aa_list += [bioinfo_dicts.aa[amino_acid],'-']
        else:
            raise RuntimeError(amino_acid + ' is no a valid amino acid.')
    return ''.join(aa_list[:-1])

try:
    import gc_content
    have_gc = True
except ImportError as e:
    have_gc = False
