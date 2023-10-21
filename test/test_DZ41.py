from dz4.DZ41 import shifted_lst


def test_shifted_lst():
    assert shifted_lst(['1', '2', '3', '4', '5'], 2) == ['4', '5', '1', '2', '3']
    assert shifted_lst(['1', '2', '3', '4', '5'], 3) == ['3', '4', '5', '1', '2']
    assert shifted_lst(['1', '2', '3', '4', '5'], 0) == ['1', '2', '3', '4', '5']