"""A matrix is a collection of scalar values arranged in rows and columns as a rectan-
gular grid of a fixed size. The elements of the matrix can be accessed by specifying
a given row and column index with indices starting at 0.
"""
from typing import Any

from py_ds.arrays.array import Array
from py_ds.arrays.array2d import Array2D


class Matrix():
    def __init__(self, numRows: int, numCols: int):
        """initializes internal 2d array and sets all values to 0"""
        self.__matrix = Array2D(numRows, numCols)
        self.__matrix.zeros()

    @classmethod
    def of(cls, *arrays: Array):
        """initializes internal 2d array with the specific elements"""
        nrRows = len(arrays)
        nrCols = len(arrays[0])
        obj = cls(nrRows, nrCols)
        for idx in range(nrRows):
            row = arrays[idx]
            for col_idx in range(len(row)):
                obj.__setitem__((idx, col_idx), row[col_idx])
        return obj

    def getNumOfRows(self) -> int:
        """returns the number of rows in the matrix"""
        return self.__matrix.getNumOfRows()

    def getNumOfColumns(self):
        """returns the number of columns in the matrix"""
        return self.__matrix.getNumOfColumns()

    def __getitem__(self, ndxTuple):
        """returns the values stored in the given matrix element. both row and col must be within the valid range"""
        return self.__matrix.__getitem__(ndxTuple)

    def __setitem__(self, ndxTuple, scalar):
        """sets the matrix element at the given row and col to scalar. the element indices must be within the valid range"""
        self.__matrix.__setitem__(ndxTuple, scalar)

    def scaleBy(self, scalar):
        """mutliplies each element of the matrix by the given scalar value. The underlying matrix is modified by this
             operation"""
        for array in self.__matrix:
            for idx in range(len(array)):
                array[idx] *= scalar

    def transpose(self):
        """return a new matrix that is the transpose of this matrix"""
        newNrRows = self.getNumOfColumns()
        newNrCols = self.getNumOfRows()
        transposed = Array2D(newNrRows, newNrCols)
        for ridx in range(self.getNumOfRows()):
            for cidx in range(self.getNumOfColumns()):
                value = self.__getitem__((ridx, cidx))
                transposed.__setitem__((cidx, ridx), value)
        self.__matrix = transposed

    def __applyOperator(self, rhsMatrix: 'Matrix', func, row_index: int, column_index: int) -> None:
        value = self.__operator(rhsMatrix, func, row_index, column_index)
        self.__setitem__((row_index, column_index), value)

    def __operator(self, rhsMatrix: 'Matrix', func, row_index: int, column_index: int) -> Any:
        return func(self.__getitem__((row_index, column_index)), rhsMatrix.__getitem__((row_index, column_index)))

    def add(self, rhsMatrix: 'Matrix') -> None:
        """creates and returns a new matrix that is the result of adding this matrix to the given rhsMatrix. The size of
        the two matrices must be the same"""
        """creates and returns a new matrix that is the result of adding this matrix to the given rhsMatrix. The size of
              the two matrices must be the same"""
        assert self.getNumOfRows() == rhsMatrix.getNumOfRows(), "Number of rows must be the same"
        assert self.getNumOfColumns() == rhsMatrix.getNumOfColumns(), "Number of columns must be the same"
        for ridx in range(self.getNumOfRows()):
            for cidx in range(self.getNumOfColumns()):
                self.__applyOperator(rhsMatrix, (lambda x, y: x + y), ridx, cidx)

    def subtract(self, rhsMatrix: 'Matrix'):
        """the same as Matrix.add() operation but subtracts the two matrices"""
        """creates and returns a new matrix that is the result of adding this matrix to the given rhsMatrix. The size of
              the two matrices must be the same"""
        assert self.getNumOfRows() == rhsMatrix.getNumOfRows(), "Number of rows must be the same"
        assert self.getNumOfColumns() == rhsMatrix.getNumOfColumns(), "Number of columns must be the same"
        for ridx in range(self.getNumOfRows()):
            for cidx in range(self.getNumOfColumns()):
                self.__applyOperator(rhsMatrix, (lambda x, y: x - y), ridx, cidx)

    def multiply(self, rhsMatrix: 'Matrix') -> 'Matrix':
        """ Creates and returns a new matrix resulting from matrix multiplication.
        Multiplication. Matrix multiplication is only defined for matrices where the number of columns in the matrix on
        the lefthand side is equal to the number of rows in the matrix on the righthand side. The result is a new matrix
        that contains the same number of rows as the matrix on the lefthand side and the same number of columns as the
        matrix on the righthand side. In other words, given a matrix of size m × n multiplied by a matrix of size n × p,
        the resulting matrix is of size m × p. In multiplying two matrices, each element of the new matrix is the result
        of summing the product of a row in the lefthand side matrix by a column in the righthand side matrix.
        """
        assert self.getNumOfRows() == rhsMatrix.getNumOfColumns(), "Number columns must equal the other number of rows"
        assert self.getNumOfColumns() == rhsMatrix.getNumOfRows(), "Number of rows must equal the other number of columns"
        multiplied = Matrix(
            max(self.getNumOfRows(), rhsMatrix.getNumOfRows()),
            max(self.getNumOfColumns(), rhsMatrix.getNumOfColumns())
        )
        multiplied.__matrix.zeros()
        for a_ridx in range(self.getNumOfRows()):
            for b_cidx in range(rhsMatrix.getNumOfColumns()):
                for b_ridx in range(rhsMatrix.getNumOfRows()):
                    tmp = multiplied.__getitem__((a_ridx, b_cidx))
                    tmp += self.__getitem__((a_ridx, b_ridx)) * rhsMatrix.__getitem__((b_ridx, b_cidx))
                    multiplied.__setitem__((a_ridx, b_cidx), tmp)
        return multiplied

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        if not other.getNumOfColumns() == self.getNumOfColumns() and other.getNumOfRows() == self.getNumOfRows():
            return False
        # delegate to Array2D
        return other.__matrix.__eq__(self.__matrix)

    def __str__(self):
        def print_row(row) -> str:
            token = "|\t"
            for idx in range(len(row)):
                token += str(row[idx])
                if idx < len(row) - 1:
                    token += "\t"
            token += "\t|\n"
            return token

        val = "\nMatrix\n"
        for array in self.__matrix:
            val += print_row(array)
        return val
