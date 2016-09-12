def complement_base(base, material='DNA'):
    """Return the Watson-Crick complement of a base"""
    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material =='RNA':
            return 'U'
    elif base in 'TtUu':
        return 'A'
    elif base in 'Gg':
        return 'C'
    elif base in 'Cc':
        return 'G'
    else:
        print("Error")

def reverse_complement(seq, material='DNA'):
    """Compute reverse complement of a DNA sequence."""
    # Initialize empty string
    rev_comp = ''
    seq_rev = seq[::-1]
    # Loop through and add new rev comp bases
    seq_rev = seq_rev.replace('A', 'x')
    seq_rev = seq_rev.replace('a', 'x')
    seq_rev = seq_rev.replace('T', 'y')
    seq_rev = seq_rev.replace('t', 'y')
    seq_rev = seq_rev.replace('y', 'A')
    seq_rev = seq_rev.replace('x', 'T')
    seq_rev = seq_rev.replace('G', 'x')
    seq_rev = seq_rev.replace('g', 'x')
    seq_rev = seq_rev.replace('C', 'y')
    seq_rev = seq_rev.replace('c', 'y')
    seq_rev = seq_rev.replace('y', 'G')
    seq_rev = seq_rev.replace('x', 'C')
    rev_comp = seq_rev

    return rev_comp
