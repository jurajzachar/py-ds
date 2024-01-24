"""
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

    def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:
  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5

the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        the elements of A are all distinct;
        each element of array A is an integer within the range [1..(N + 1)].
"""
from typing import List


def solution(a: List[int]) -> int:
    assert len(a) > 1, "array must contain at least two elements"
    clone = a.copy()
    clone.sort()
    first = clone[0]
    last = clone[-1]
    missing = [x for x in range(first, last + 1) if x not in clone]
    return missing[0]

if __name__ == '__main__':
    a = [2, 3, 1, 5]
    assert solution(a) == 4

    a = [10, 5, 7, 9, 4, 2, 1, 3, 6]
    assert solution(a) == 8