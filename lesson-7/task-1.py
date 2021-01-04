# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.


class Matrix:

    def __init__(self, lists_list):

        self.matrix = lists_list

    def __str__(self):

        def join_func(list_item):

            to_str = map(lambda item: str(item), list_item)

            return ' '.join(to_str)

        strings_list = map(join_func, self.matrix)

        string = '\n'.join(strings_list)

        return string

    def __add__(self, other):

        other = other.matrix

        result = []

        for index, item in enumerate(self.matrix):

            item = self.matrix[index].copy()

            if index < len(other):

                other_item = other[index]

                for ind, num in enumerate(item):

                    if ind < len(other_item):

                        other_num = other_item[ind]

                        item[ind] = num + other_num

                result.append(item)

        return Matrix(result)


matrix_1 = Matrix([[1, 2, 3, 4, 5], [0, 1, 2, 3, 4], [3, 1, 5, 3, 8]])
matrix_2 = Matrix([[1, 2, 3, 4], [0, 1, 2, 3], [3, 1, 5, 3]])

print(matrix_1, end='\n\n')
print(matrix_1 + matrix_2)
