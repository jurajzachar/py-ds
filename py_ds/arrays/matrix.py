"""A matrix is a collection of scalar values arranged in rows and columns as a rectan-
gular grid of a fixed size. The elements of the matrix can be accessed by specifying
a given row and column index with indices starting at 0.
"""
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
        pass

    def add(self, rhsMatrix):
        """creates and returns a new matrix that is the result of adding this matrix to the given rhsMatrix. The size of
        the two matrices must be the same"""
        pass

    def subtract(self, rhsMatrix):
        """the same as Matrix.add() operation but subtracts the two matrices"""
        pass

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        if not other.getNumOfColumns() == self.getNumOfColumns() and other.getNumOfRows() == self.getNumOfRows():
            return False
        # delegate to Array2D
        return other.__matrix.__eq__(self.__matrix)

    def __str__(self):
        def print_row(row) -> str:
            val = "|\t"
            for idx in range(len(row)):
                val += str(row[idx])
                if idx < len(row) - 1:
                    val += "\t"
            val += "\t|\n"
            return val

        val = "\nmatrix\n"
        for array in self.__matrix:
            val += print_row(array)

        return val


if __name__ == '__main__':
    print(Matrix.of(Array.of(10, 10), Array.of(1, 9)))
