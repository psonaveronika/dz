from dz4.DZ42 import factorial


def test_factorial():
    assert factorial(6) == 720
    assert factorial(3) == 6
    assert factorial(1) == 1
    assert factorial(0) == 1