from dz4.DZ43 import is_unique


def test_is_unique():
    assert is_unique([34, 'Hello, world!', False])
    assert is_unique('12345')
    assert not is_unique('1113')