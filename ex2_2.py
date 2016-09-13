def gc_con(seq):
    """Count G's and C's"""
    gc = 0
    gc=(seq.count('G')+seq.count('C'))/len(seq)
    return gc


def readfna(file):
    """Reads a fasta file and outputs the sequence string only without gaps"""
    seq = ''
    seq_list = ''
    with open(file,'r') as f:
        seq_list = f.readlines()
        i=1
        while i < len(seq_list):
            seq += seq_list[i].rstrip()
            i+=1
    return seq

def gc_blocks(seq, block_size):
    seq_gc = []
    seq_list = []
    for i in range(len(seq)//block_size):
        seq_gc.append(gc_con(seq[i*block_size:(i+1)*block_size]))
        seq_list.append(seq[i*block_size:(i+1)*block_size])
    return (seq_gc, seq_list)

def gc_map(seq, block_size, threshold):
    seq_gc = []
    seq_list = []
    seqfinal = ''
    for i in range(len(seq)//block_size):
        seq_gc.append(gc_con(seq[i*block_size:(i+1)*block_size]))
        seq_list.append(seq[i*block_size:(i+1)*block_size])

    for j in range(len(seq_list)):
        if seq_gc[j] < threshold:
            seq_list[j]=seq_list[j].lower()
    k=0
    while k < len(seq_list):
        seqfinal += seq_list[k]
        k += 1

    return seqfinal
