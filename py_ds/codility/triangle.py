"""
An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

        A[P] + A[Q] > A[R],
        A[Q] + A[R] > A[P],
        A[R] + A[P] > A[Q].

For example, consider array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20

Triplet (0, 2, 4) is triangular.

Write a function:

    def solution(A)

that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns
0 otherwise.

For example, given array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20

the function should return 1, as explained above. Given array A such that:
  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1

the function should return 0.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
"""
from typing import Tuple, List


def solution(a: List[int]) -> Tuple[int, int, int]:
    assert len(a) >= 3, "array size must be 3 or greater"
    tmp = a.copy()
    tmp.sort()
    # start from the beginning and check triangular properties
    x = 0
    while x + 2 < len(a):
        i, j, k = tmp[x], tmp[x + 1], tmp[x + 2]
        if (i + j) > k and (j + k) > i and (k + i) > j:
            return (i, j, k)
        x += 1

    # no triplet found
    return ()


if __name__ == '__main__':
    a = [10, 2, 5, 1, 8, 20]
    answer = solution(a)
    print(answer)
    assert answer == (5, 8, 10)

    a = [10, 50, 5, 1]
    answer = solution(a)
    print(answer)
    assert answer == ()
