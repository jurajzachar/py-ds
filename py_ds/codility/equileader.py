"""
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ...,
A[N − 1] have leaders of the same value.

For example, given array A such that:
    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2

we can find two equi leaders:

        0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
        2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.

The goal is to count the number of equi leaders.

Write a function:

    class Solution { public int solution(int[] A); }

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:
    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2

the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
"""


def solution(a: list[int]) -> int:
    n = len(a)
    assert 0 <= n <= 10 ** 9, "array length out of bounds"

    if n < 2:
        return a[0]

    leader_threshold = n // 2
    frequency = dict()
    equileaders = []

    # each element of the array is considered just once
    for index, elem in enumerate(a):
        if elem not in frequency.keys():
            frequency[elem] = [index]
        else:
            frequency[elem].append(index)
            if len(frequency[elem]) >= leader_threshold:
                equileaders = frequency[elem]
                break;

    # no golder leader found
    return equileaders


if __name__ == '__main__':
    a = [4, 3, 4, 4, 4, 2]
    answer = solution(a)
    print((answer[0],answer[1]))
