import pytest

from py_ds.arrays.array import Array

SIZE = 10


@pytest.fixture
def array() -> Array:
    return Array(SIZE)


def test_initilize_array(array):
    assert len(array) == SIZE
    a, b = Array.of(6, 7, 8), Array.of(9, 1, 0)
    assert a, b is not None


def test_should_clear(array):
    array.clear(1)
    for i in range(len(array)):
        assert array[i] == 1


def test_should_get_and_set(array):
    value = 'value'
    for idx in range(len(array)):
        array.clear(None)
        assert array.__getitem__(idx) == None
        array.__setitem__(idx, 'value')
        assert array.__getitem__(idx) == value


def test_array_can_be_iterated_over(array):
    vals = [x for x in range(SIZE)]
    for i in array:
        assert i == None
    for idx in range(len(array)):
        array.__setitem__(idx, vals[idx])
    collected = []
    for i in array:
        collected.append(i)
    assert vals == collected
