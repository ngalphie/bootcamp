import pytest
import L35_tdd

def test_n_neg():
    assert L35_tdd.n_neg('E') == 1
    assert L35_tdd.n_neg('D') == 1
    assert L35_tdd.n_neg('') == 0
    assert L35_tdd.n_neg('ACKLWTTAE') == 1
    assert L35_tdd.n_neg('DEDEDDEE') == 8
    assert L35_tdd.n_neg('acklwtae') == 1

    pytest.raises(RuntimeError, "L35_tdd.n_neg('Z')")
    return None
