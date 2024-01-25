"""
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

is a permutation, but array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3

is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

    def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

the function should return 1.

Given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3

the function should return 0.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [1..1,000,000,000]
"""
from typing import List


def solution(a: List[int]) -> int:
    assert len(a) > 0, "array must be non-empty"
    tmp = a.copy()
    tmp.sort()
    front = 0
    back = len(tmp) - 1
    result = 1  # indicates the sequence is a permutation
    while front < back:
        i = min(front + 1, len(tmp) - 1)
        j = max(back - 1, 0)
        if (tmp[i] - tmp[front] > 1) or (tmp[back] - tmp[j] > 1):
            result = 0
            break
        # move front and back
        front += 1
        back -= 1

    return result


if __name__ == '__main__':
    assert solution([4, 1, 2, 3]) == 1
    assert solution([4, 1, 3]) == 0

    n = 100
    nums = [x for x in range(n + 1)]
    assert solution(nums) == 1
    nums.remove(n // 2)  # remove mid element
    assert solution(nums) == 0
