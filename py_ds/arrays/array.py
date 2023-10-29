import ctypes


class Array:
    """this is simple array implementation using ctypes"""

    def __init__(self, size):
        """creates an aray with size elements"""
        assert size > 0, "Array size must be > 0"
        self._size = size
        # create array data structure using C's type module (allocates memory slots)
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # initialize each slot
        self.clear(None)

    def __len__(self):
        return self._size

    def __ensure_valid_index(self, index):
        assert 0 <= index < len(self), "array subscript out of range"

    def __getitem__(self, index):
        """get content of the array at index position"""
        self.__ensure_valid_index(index)
        return self._elements[index]

    def __setitem__(self, index, value) -> None:
        """puts the value in the array element at index position"""
        self.__ensure_valid_index(index)
        self._elements[index] = value

    def clear(self, value) -> None:
        """clears the array by setting each element to the given value"""
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        return _ArrayIterator(self._elements)

    def __str__(self):
        val = "["
        for idx in range(len(self)):
            val += str(self._elements[idx])
            if idx < len(self) - 1:
                val += ","
        val += "]"
        return val


class _ArrayIterator:
    def __init__(self, array):
        self._arrayRef = array
        self._curIndex = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curIndex < len(self._arrayRef):
            entry = self._arrayRef[self._curIndex]
            self._curIndex += 1
            return entry
        else:
            raise StopIteration
