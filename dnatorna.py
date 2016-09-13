"""
Convert DNA sequence to RNA sequences
"""
def rna(seq):
    """
    Convert DNA sequewnce to RNA.
    The returned sequences have the same capitalization
    """
    #convert to uppercase
    seq = seq.upper()

    return seq.replace('T','U')
