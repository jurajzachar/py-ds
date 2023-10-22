"""A matrix is a collection of scalar values arranged in rows and columns as a rectan-
gular grid of a fixed size. The elements of the matrix can be accessed by specifying
a given row and column index with indices starting at 0.
"""
import numpy as numpy


class Matrix():
    def __init__(self, numRows: int, numCols: int):
        """initializes internal 2d array with 0s using numpy"""
        self.__matrix = numpy.zeros((numRows, numCols))
    def numRows(self):
        """returns the number of rows in the matrix"""
        pass

    def numCols(self):
        """returns the number of columns in the matrix"""
        pass

    def __getitem__(self, item):
        """returns the values stored in the given matrix element. both row and col must be within the valid range"""
        pass

    def __setitem__(self, row, col, scalar):
        """sets the matrix element at the given row and col to scalar. the element indices must be within the valid range"""
        pass

    def scaleBy(self, scalar):
        """mutliplies each element of the matrix by the given scalar value. The underlying matrix is modified by this
        operation"""
        pass

    def transpose(self):
        """return a new matrix that is the transpose of this matrix"""
        pass

    def add(self, rhsMatrix):
        """creates and returns a new matrix that is the result of adding this matrix to the given rhsMatrix. The size of
        the two matrices must be the same"""
        pass

    def subtract(self, rhsMatrix):
        """the same as Matrix.add() operation but subtracts the two matrices"""
        pass

    def __str__(self):
        return self.__matrix.__str__()

if __name__ == '__main__':
    print(Matrix(10, 10))