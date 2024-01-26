"""
Write a function:

    def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

    { i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2
within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

        A and B are integers within the range [0..2,000,000,000];
        K is an integer within the range [1..2,000,000,000];
        A ≤ B.
"""
from typing import List


def naive_solution(a: int, b: int, k: int) -> List[int]:
    start = max(1, a)  # eliminate zero
    end = max(1, b)
    if k == end:
        return [k]

    return [x for x in range(start, end + 1) if x % k == 0]


def efficient_solution(a: int, b: int, k: int) -> int:
    assert 0 <= a <= 2000 * 1000 * 1000, "a parameter out of range"
    assert 0 <= b <= 2000 * 1000 * 1000, "b parameter out of range"
    assert 1 <= k <= 2000 * 1000 * 1000, "k parameter out of range"
    assert a <= b

    bottom_zero_mod = a
    while (bottom_zero_mod % k != 0) and (bottom_zero_mod != b):
        bottom_zero_mod += 1
    top_zero_mod = b
    while (top_zero_mod % k != 0) and (top_zero_mod != a):
        top_zero_mod -= 1

    return (top_zero_mod // k) - (bottom_zero_mod // k) + 1


if __name__ == '__main__':
    a, b, k = 6, 11, 2
    answer = naive_solution(a, b, k)
    assert len(answer) == 3
    assert efficient_solution(a, b, k) == 3

    a, b, k = 1, 13, 2
    answer = naive_solution(a, b, k)
    print(answer)
    assert len(answer) == 6
    assert efficient_solution(a, b, k) == 6

    a, b, k = 1, 13, 3
    answer = naive_solution(a, b, k)
    print(answer)
    assert answer == [3, 6, 9, 12]
    assert efficient_solution(a, b, k) == 4

    n = 2000 * 1000 * 1000
    answer = efficient_solution(0, n, n // 2)
    print(answer)
