"""
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a
slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P]
+ A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[
Q]) / (Q − P + 1).

For example, array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

contains the following example slices:

        slice (1, 2), whose average is (2 + 2) / 2 = 2;
        slice (3, 4), whose average is (5 + 1) / 2 = 3;
        slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.

The goal is to find the starting position of a slice whose average is minimal.

Write a function:

    class Solution { public int solution(int[] A); }

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal
average. If there is more than one slice with a minimal average, you should return the smallest starting position of such
a slice.

For example, given array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [2..100,000];
        each element of array A is an integer within the range [−10,000..10,000].
"""
from typing import List, Tuple


def solution(a: List[int]) -> Tuple[int, int]:
    elem_upper_bound = 10 * 100
    elem_lower_bound = -10 * 100
    n = len(a)
    assert 2 <= n <= 100 * 1000, "array length out of bounds"

    # base case --> uninterrupted monotonic sequence with increment of 1
    min_distance_idx = (1, elem_upper_bound)  # (distance, index)
    neighbors = [0] * n

    for k in range(1, n):
        previous = a[k - 1]
        assert elem_lower_bound <= previous <= elem_upper_bound
        pointer = a[k]
        assert elem_lower_bound <= pointer <= elem_upper_bound

        # calculate neighbours distance
        distance = abs(a[k] - a[k - 1])
        # update neighbor distances
        neighbors[k] = distance
        # check if we found a new low watermark
        if distance < min_distance_idx[1]:
            min_distance_idx = (k - 1, distance)

    return min_distance_idx


if __name__ == '__main__':
    a = [4, 2, 2, 5, 1, 5, 8]
    answer = solution(a)
    print(answer)
    assert answer[0] == 1

    a = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10]
    answer = solution(a)
    print(answer)
    assert answer[0] == 4

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    answer = solution(a)
    print(answer)
    assert answer[0] == 0

    a = [1, 1, 1, 10, 10]
    answer = solution(a)
    print(answer)
    assert answer[0] == 0

    a = [2, 0, -1, 10, 10]
    answer = solution(a)
    print(answer)
    assert answer[0] == 3

    a = [2, 0, -2, -10, -9]
    answer = solution(a)
    print(answer)
    assert answer[0] == 3