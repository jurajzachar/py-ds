import pytest

from py_ds.arrays.array import Array
from py_ds.arrays.matrix import Matrix

SIZE = 5


@pytest.fixture
def zero_matrix() -> Matrix:
    return Matrix(SIZE, SIZE)


def test_initialize_matrix(zero_matrix: Matrix):
    assert zero_matrix.getNumOfColumns() == SIZE
    assert zero_matrix.getNumOfRows() == SIZE
    for row in range(SIZE):
        for column in range(SIZE):
            assert zero_matrix.__getitem__((row, column)) == 0


def test_should_scale_matrix():
    matrix = Matrix.of(Array.of(1, 2, 3), Array.of(4, 5, 7), Array.of(8, 9, 10))
    matrix.scaleBy(10)
    assert matrix == Matrix.of(Array.of(10, 20, 30), Array.of(40, 50, 70), Array.of(80, 90, 100))
