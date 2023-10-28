from py_ds.arrays.array import Array


class Array2D:
    def __init__(self, numRows, numCols):
        assert numRows, numCols > 0
        # create an array to store references for each column
        self._columns = Array(numCols)
        # create arrays for each column (an array of arrays)
        for i in range(numCols):
            self._columns[i] = Array(numRows)

    def getNumOfColumns(self):
        return len(self._columns)

    def getNumOfRows(self):
        return len(self._columns[0])

    def reset(self, value):
        """clears the array and sets every element to the given value"""
        for c in range(self.getNumOfColumns()):
            self._columns[c].clear
    def zeros(self):
        """the same as reset, but set 0 as default value"""
        self.reset(0)