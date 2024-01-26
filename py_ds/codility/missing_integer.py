"""
Write a function:

    def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000].
"""
from typing import List


def solution(a: List[int]) -> int:
    assert len(a) > 0, "array must be non-empty"

    # if min(array) < 0 return 1
    # if array is gap-less return max(a) + 1
    # if array from min .. max has a gap, return the smallest gap

    tmp = a.copy()
    tmp.sort()
    tmp = list(set(tmp))

    if min(tmp) < 0:
        return 1
    n = 0
    while n + 1 < len(a):
        if tmp[n +1] - tmp[n] > 1:
            return tmp[n] + 1
        n += 1

    return max(a) + 1

if __name__ == '__main__':
    answer = solution([1, 3, 6, 4, 1, 2])
    assert answer == 5

    n = 1000 * 1000
    input = [x for x in range(1, n + 1)]
    answer = solution(input)
    assert answer == n + 1
    gap = n // 2
    input.remove(gap)
    answer = solution(input)
    assert answer == gap

