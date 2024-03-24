from numbers import Number 
from collections.abc import Iterable


class Matrix:
    def __init__(self, rows: list[list[Number]]):
        self.__rows = rows
        self.n = len(rows) 
        self.m = len(rows[0]) 
        if not self.is_valid(self.__rows):
            raise ValueError('невозможно сконструировать матрицу')
    
    @property
    def transpose(self):
        test_out = []
        test_out_all = []
        result = ''
        for i in range(len(self.__rows[0])):
            test = []
            for __rows in self.__rows:
                test.append(__rows[i])
            test_out.append(test)
            test_out_all.extend(test)        
        str_digits = [len(str(num)) for num in test_out_all]
        max_len_digit = max(str_digits)
        for i in range(self.m):
            for j in range(self.n):
                result += (' '+str(test_out[i][j])).rjust(max_len_digit + 1)
            result += '\n'
        return result
    @staticmethod
    def is_valid(item: Iterable[Iterable[Number]]) -> bool:
        a = len(item[-1])
        for i in range(len(item) - 1):
            if a != len(item[i]):
                return False
            else:
                continue
        return True



    def __getitem__(self, key):
        return self.__rows[key]
    def __add__(self, other):
        if self.is_valid(self.__rows):
            if isinstance(other, Matrix):
                if self.n == other.n and self.m == other.m:
                    for i in range(self.n):
                        for j in range(self.m):
                            self[i][j] = self[i][j] + other[i][j]
                    return self
                else:
                    raise TypeError('Матрицы должны иметь одинаковый размер')
            elif isinstance(other, Number):
                for i in range(self.n):
                    for j in range(self.m):
                        self[i][j] = self[i][j] + other
                return self
            else:
                raise TypeError
        else:
            raise TypeError
        
    def __radd__(self, other):
        if self.is_valid(self.__rows):
            if isinstance(other, Matrix):
                if self.n == other.n and self.m == other.m:
                    for i in range(self.n):
                        for j in range(self.m):
                            self[i][j] = self[i][j] + other[i][j]
                    return self
                else:
                    raise TypeError('Матрицы должны иметь одинаковый размер')
            elif isinstance(other, Number):
                for i in range(self.n):
                    for j in range(self.m):
                        self[i][j] = self[i][j] + other
                return self
            else:
                raise TypeError
        else:
            raise TypeError
    def __sub__(self, other):
        if self.is_valid(self.__rows):
            if isinstance(other, Matrix):
                if self.n == other.n and self.m == other.m:
                    for i in range(self.n):
                        for j in range(self.m):
                            self[i][j] = self[i][j] - other[i][j]
                    return self
                else:
                    raise TypeError('Матрицы должны иметь одинаковый размер')
            elif isinstance(other, Number):
                for i in range(self.n):
                    for j in range(self.m):
                        self[i][j] = self[i][j] - other
                return self
            else:
                raise TypeError
        else:
            raise TypeError
        
    def __rsub__(self, other):
        if self.is_valid(self.__rows):
            if isinstance(other, Matrix):
                if self.n == other.n and self.m == other.m:
                    for i in range(self.n):
                        for j in range(self.m):
                            self[i][j] = self[i][j] - other[i][j]
                    return self
                else:
                    raise TypeError('Матрицы должны иметь одинаковый размер')
            elif isinstance(other, Number):
                for i in range(self.n):
                    for j in range(self.m):
                        self[i][j] = self[i][j] - other
                return self
            else:
                raise TypeError
        else:
            raise TypeError
    def __neg__(self):
        for i in range(self.n):
            for j in range(self.m):
                self[i][j] = self[i][j] * -1
        return self
    def __repr__(self):
        result =""
        test___rows = []
        for row in self.__rows:
            test___rows.extend(row)
        str___rows = [len(str(num)) for num in test___rows]
        max_len_digit = max(str___rows)
        for i in range(self.n):
            for j in range(self.m):
                result += (' '+str(self.__rows[i][j])).rjust(max_len_digit + 1)
            result +='\n'
        return result
    def __mul__(self, other):
        if isinstance(other, Matrix):
            raise NotImplementedError('умножение матриц будет реализовано в будущем')
        elif isinstance(other, Number):
            for i in range(self.n):
                for j in range(self.m):
                    self[i][j] = self[i][j] * other
            return self
        else:
            raise TypeError
    def __rmul__(self, other):
        if isinstance(other, Matrix):
            raise NotImplementedError('умножение матриц будет реализовано в будущем')
        elif isinstance(other, Number):
            for i in range(self.n):
                for j in range(self.m):
                    self[i][j] = self[i][j] * other
            return self
        else:
            raise TypeError

#>>> Matrix([(1,2),(1,2,3,4)])
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# File "E:\Users\doter\Desktop\python_main\dz\Eremeev\2024.02.20\1.py", line 11, in __init__
#    raise ValueError('невозможно сконструировать матрицу')
#ValueError: невозможно сконструировать матрицу
#>>> matrix1 = Matrix([[2,2,2],[1,1,1]])
#>>> matrix2 = Matrix([[5,5,5],[3,3,3]])
#>>> matrix1
# 2 2 2
# 1 1 1

#>>> matrix2
# 5 5 5
# 3 3 3

#>>> matrix1.transpose
#' 2 1\n 2 1\n 2 1\n'
#>>> print(matrix1.transpose)
# 2 1
# 2 1
# 2 1

#>>> matrix1 + matrix2
# 7 7 7
# 4 4 4

#>>> matrix1.__repr__()
#' 7 7 7\n 4 4 4\n'
#>>> matrix1
# 7 7 7
# 4 4 4  
#>>> matrix1[0][2] = 8
#>>> matrix1[1][2] = 8
#>>> matrix1
# 7 7 8
# 4 4 8          