import pytest
from fractions import Fraction
from matrix_class import Matrix

def test_input_matrix(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '2')  # Мокаем ввод пользователя
    matrix = Matrix()
    matrix.input_matrix()
    assert matrix.rows == 2
    assert matrix.columns == 2

def test_input_matrix_invalid_elements():
    matrix = Matrix()
    matrix.rows = 2
    matrix.columns = 2
    with pytest.raises(ValueError):
        matrix.elements = [[Fraction(1), Fraction(2)], [Fraction(3)]]
        matrix.input_matrix()

def test_str_output(capsys):
    matrix = Matrix(2, 2, [[Fraction(1), Fraction(2)], [Fraction(3), Fraction(4)]])
    print(matrix)
    captured = capsys.readouterr()
    assert captured.out == '1 2\n3 4\n'

# Запуск тестов с помощью pytest
if __name__ == '__main__':
    pytest.main()

