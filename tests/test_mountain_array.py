import pytest
import ctypes

from py_ds.search.mountain_array import MountainArray, Solution


@pytest.mark.parametrize("type_code, elems", [
    ('i', [1, 2, 3, 4, 5, 3, 1]),  # signed int
    ('I', [ctypes.c_uint(x).value for x in [1, 5, 1, 4, 2, 3, 3]]),  # unsigned integer
    ('f', [ctypes.c_float(x).value for x in [1, 1, 2, 3, 3, 4, 5]]),  # floating-point
    ('d', [ctypes.c_double(x).value for x in [5, 4, 3, 3, 2, 1, 1]]),  # double-precision floating point
    ('b', [ctypes.c_int8(x).value for x in [1, 2, 3, 4, 1, 3, 5]]),  # signed integer (1 byte)
    ('B', [ctypes.c_uint8(x).value for x in [1, 2, 5, 4, 3, 3, 1]])  # unsigned integer (1 byte)
])
def test_initialized_mount_array(type_code, elems):
    candidate = MountainArray(elems, type_code)
    assert candidate.length() == 7
    assert candidate.toList() == [1, 2, 3, 4, 5, 3, 1]
    # each internal array is balanced: [1, 2, 3, 4, 5, 3, 1]
    assert candidate.get(0) == 1
    assert candidate.get(1) == 2
    assert candidate.get(2) == 3
    assert candidate.get(3) == 4
    assert candidate.get(4) == 5
    assert candidate.get(5) == 3
    assert candidate.get(6) == 1
    # index error
    assert candidate.get(7) == None


def test_large_mountain_array():
    candidate = MountainArray([x for x in range(1000)] + [x for x in range(10000)])
    assert candidate.length() == 11000
    left = [x for x in range(10000)]
    right = [x for x in range(1000)]
    right.sort(reverse=True)
    assert candidate.toList() == left + right  # [1 .. 10000, 1000 .. 1]


def test_solution_mountain_array():
    elems = [1, 2, 3, 4, 5, 3, 1]
    ma = MountainArray(elems)
    candidate = Solution()
    assert candidate.findMinimumIndex(1, ma) == 0
    assert candidate.findMinimumIndex(2, ma) == 1
    assert candidate.findMinimumIndex(3, ma) == 2
    assert candidate.findMinimumIndex(4, ma) == 3
    assert candidate.findMinimumIndex(5, ma) == 4
