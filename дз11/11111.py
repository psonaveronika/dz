class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    def input_matrix(self):
        for i in range(self.rows):
            row = list(map(int, input(f"Enter elements for row {i+1}: ").split()))
            if len(row) != self.cols:
                print("Invalid number of elements. Please enter again.")
                self.input_matrix()
                return
            self.matrix[i] = row

    def display_matrix(self):
        for row in self.matrix:
            print(" ".join(str(elem) for elem in row))

# Пример использования класса Matrix
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = Matrix(rows, cols)
matrix.input_matrix()

print("\nMatrix:")
matrix.display_matrix()
