import pytest
import l36

def test_l36(fc=l36.find_codon_lesson6):

    DNA = 'ATGGAGAACAACGAAGCCCCCTCCCCCTCGGGATCCAACAACAACGAGAACAACAATGCAGCCCAGAAGAAGCTGCAGCAGACCCAAGCCAAGGTGGACGAGGTGGTCGGGATTATGCGTGTGAACGTGGAGAAGGTCCTGGAGCGGGACCAGAAGCTATCGGAACTGGGCGAGCGTGCGGATCAGCTGGAGCAGGGAGCATCCCAGTTCGAGCAGCAGGCCGGCAAGCTGAAGCGCAAGCAATGGTGGGCCAACATGAAGATGATGATCATTCTGGGCGTGATAGCCGTTGTGCTTCATCGTTCTGGTGTCGCTTTTCAATTGA'
    assert fc('ATG', DNA) == 0

    return None
