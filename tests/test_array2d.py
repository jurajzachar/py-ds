import pytest

from py_ds.arrays.array import Array
from py_ds.arrays.array2d import Array2D

SIZE = 10


@pytest.fixture
def array2d_10x10() -> Array2D:
    return Array2D(SIZE, SIZE)


@pytest.fixture
def array2d_3x4() -> Array2D:
    return Array2D(3, 4)


def test_initilize_array2d(array2d_3x4: Array2D):
    assert array2d_3x4.getNumOfColumns() == 4
    assert array2d_3x4.getNumOfRows() == 3


def test_should_clear(array2d_10x10: Array2D):
    array2d_10x10.zeros()
    for i in range(SIZE):
        assert array2d_10x10.__getitem__((i, i)) == 0


def test_should_get_and_set(array2d_10x10):
    value = 'value'
    for idx in range(SIZE):
        array2d_10x10.clear(None)
        assert array2d_10x10.__getitem__((idx, idx)) == None
        array2d_10x10.__setitem__((idx, idx), 'value')
        assert array2d_10x10.__getitem__((idx, idx)) == value


def test_array2d_can_be_iterated_over(array2d_10x10):
    for column in array2d_10x10:
        assert column == Array(SIZE)  # initializes to [None, ... ]
    otherArray2D = Array2D(SIZE, SIZE)
    otherArray2D.__setitem__((0, 9), 'value')  # modifies one of the elements
    with pytest.raises(AssertionError):
        assert array2d_10x10 == otherArray2D
