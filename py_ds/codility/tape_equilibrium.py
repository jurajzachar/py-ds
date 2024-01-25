"""
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

We can split this tape in four places:

        P = 1, difference = |3 − 10| = 7
        P = 2, difference = |4 − 9| = 5
        P = 3, difference = |6 − 7| = 1
        P = 4, difference = |10 − 3| = 7

Write a function:

    def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [2..100,000];
        each element of array A is an integer within the range [−1,000..1,000].
"""
import time
from typing import List


def solution_efficient(a: List[int]) -> int:
    sum_front, sum_back = 0, sum(a)
    diff_list = []
    for elm in a:
        sum_front += elm
        sum_back -= elm
        diff_list.append(abs(sum_front - sum_back))

    return min(diff_list)

def solution(a: List[int]) -> int:
    """
    return a tuple consisting of the minimal sum and index position P
    """
    assert 2 < len(a) < 100 * 1000, f"length of array limit exceeded ({len(a)})"

    min_sum = sum(a) # with p = 0
    for p in [index for index in range (1, len(a))]:
        x = abs(sum(a[0:p]) - sum(a[p:len(a)]))
        if x < min_sum:
            min_sum = x

    return min_sum

if __name__ == '__main__':
    a = [x for x in range(100 * 1000 - 1)]
    start = time.perf_counter()
    answer = solution_efficient(a)
    end = time.perf_counter()

    print(f"solution found in {end - start}")
    print(answer)

    assert answer == 16611