iimport unittest
from unittest.mock import patch
from io import StringIO
import sys
from matrix_class import Matrix

class TestMatrixClass(unittest.TestCase):

    def test_input_matrix(self):
        with patch('builtins.input', side_effect=['1 2 3', '4 5 6', '7 8 9']):
            matrix = Matrix(3, 3)
            matrix.input_matrix()
            self.assertEqual(matrix.matrix, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_display_matrix(self):
        matrix = Matrix(2, 2)
        matrix.matrix = [[1, 2], [3, 4]]
        captured_output = StringIO()
        sys.stdout = captured_output
        matrix.display_matrix()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "1 2\n3 4\n")

if __name__ == '__main__':
    unittest.main()
