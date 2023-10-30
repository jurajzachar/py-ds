from py_ds.arrays.array import Array


class Array2D:
    def __init__(self, numRows, numCols):
        assert numRows, numCols > 0
        self._numRows = numRows
        self._numCols = numCols
        # create an array to store references for each row
        self._rows = Array(numRows)
        # create arrays for each row (an array of arrays)
        for i in range(numRows):
            self._rows[i] = Array(numCols)

    def getNumOfColumns(self):
        return len(self._rows[0])

    def getNumOfRows(self):
        return len(self._rows)

    def clear(self, value):
        """clears the array and sets every element to the given value"""
        for c in range(self.getNumOfColumns()):
            self._rows[c].clear(value)

    def __ensure_valid_indices(self, row, column):
        assert 0 <= row < self.getNumOfRows() \
        and 0 <= column < self.getNumOfColumns(), \
        "Array subscription out of range"

    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        column = ndxTuple[1]
        self.__ensure_valid_indices(row, column)
        target_row = self._rows[row]
        return target_row[column]

    def __setitem__(self, ndxTuple, value) -> None:
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        column = ndxTuple[1]
        self.__ensure_valid_indices(row, column)
        target_row = self._rows[row]
        target_row[column] = value

    def zeros(self):
        """the same as reset, but set 0 as default value"""
        self.clear(0)

    def __iter__(self):
        return _Array2DIterator(self._rows)


    def __eq__(self, other):
        if not isinstance(other, Array2D):
            return False
        if not other._numCols == self._numCols and other._numRows == self._numRows:
            return False
        # deep elem comparison
        isEqual = True
        for i in range(self._numRows):
            if other._rows[i] != self._rows[i]:
                isEqual = False
                break
        return isEqual

    def __str__(self) -> str:
        val = "array2d([\n"
        for row in self._rows:
            val += str(row)
            val += "\n"
        val += "])"
        return val


class _Array2DIterator:
    def __init__(self, rows):
        self._rowsRef = rows
        self._curIndex = 0

    def __iter__(self):
        return self

    def __next__(self) -> Array:
        if self._curIndex < len(self._rowsRef):
            column: Array = self._rowsRef[self._curIndex]
            self._curIndex += 1
            return column
        else:
            raise StopIteration