import pytest

from py_ds.arrays.array import Array
from py_ds.arrays.matrix import Matrix

SIZE = 5


@pytest.fixture
def zero_matrix() -> Matrix:
    return Matrix(SIZE, SIZE)


@pytest.fixture()
def some_matrix() -> Matrix:
    return Matrix.of(Array.of(1, 2, 3), Array.of(4, 5, 7), Array.of(8, 9, 10))


def test_initialize_matrix(zero_matrix: Matrix):
    assert zero_matrix.getNumOfColumns() == SIZE
    assert zero_matrix.getNumOfRows() == SIZE
    for row in range(SIZE):
        for column in range(SIZE):
            assert zero_matrix.__getitem__((row, column)) == 0
            zero_matrix.__setitem__((row, column), 1)
            assert zero_matrix.__getitem__((row, column)) == 1


def test_should_scale_matrix(some_matrix):
    some_matrix.scaleBy(10)
    assert some_matrix == Matrix.of(Array.of(10, 20, 30), Array.of(40, 50, 70), Array.of(80, 90, 100))
    some_matrix.scaleBy(0.1)
    assert some_matrix == Matrix.of(Array.of(1, 2, 3), Array.of(4, 5, 7), Array.of(8, 9, 10))


def test_should_transpose_matrix(some_matrix):
    some_matrix.transpose()
    assert some_matrix == Matrix.of(Array.of(1, 4, 8), Array.of(2, 5, 9), Array.of(3, 7, 10))


def test_should_add_up(some_matrix):
    m = Matrix(3, 3)
    print(m)
    m.add(some_matrix)
    print(m)
    assert m == some_matrix
    m.add(some_matrix)  # should double every element
    print(m)
    assert m == Matrix.of(Array.of(2, 4, 6), Array.of(8, 10, 14), Array.of(16, 18, 20))


def test_should_subtract(some_matrix):
    m = Matrix(3, 3)
    print(m)
    some_matrix.subtract(m)
    print(some_matrix)
    assert some_matrix == Matrix.of(Array.of(1, 2, 3), Array.of(4, 5, 7), Array.of(8, 9, 10))
    some_matrix.subtract(some_matrix)  # should double every element
    print(some_matrix)
    assert m == Matrix(3, 3)


def test_should_multiply():
    a = Matrix.of(Array.of(0, 1), Array.of(2, 3), Array.of(4, 5))
    print(a)
    b = Matrix.of(Array.of(6, 7, 8), Array.of(9, 1, 0))
    print(b)
    res = a.multiply(b)
    print(res)
    expected = Matrix.of(Array.of(9, 1, 0), Array.of(39, 17, 16), Array.of(69, 33, 32))
    assert res == expected
