"""
There are n > 0 canoeists weighing respectively 1 <= w(0) <= w(1) <= . . . <= w(n−1) <= 10^9.
The goal is to seat them in the minimum number of double canoes whose displacement (the maximum load) equals k.

You may assume that w(i) <= k.
"""


def solution(w: list[int], k: int) -> int:
    """
    The heaviest canoeist is seated with the lightest, as long as their weight
    is less than or equal to k. If not, the heaviest canoeist is seated alone in the canoe.
    """

    tmp = w.copy()
    tmp.sort() # guarantees the canoeists are sorted from the lightest to the heaviest

    # short-circuit eval, if the lightest and heaviest canoeist exceed the limit
    if tmp[0] + tmp[-1] > k:
        return len(w)

    canoes, x, y = 0, 0, (len(w) - 1)
    while y >= x:
        if w[x] + w[y] <= k:
            x += 1
        y -= 1
        canoes += 1

    return canoes

if __name__ == '__main__':
    w = [14, 10, 12 ,12, 13, 12, 11]

    k = 23
    answer = solution(w, k)
    print(f"for k={k}, number of canoes is {answer}")
    expected = 7
    assert answer == expected, f"expected={expected} is not equal to actual={answer}"

    k = 24
    answer = solution(w, k)
    print(f"for k={k}, number of canoes is {answer}")
    expected = 6
    assert answer == expected, f"expected={expected} is not equal to actual={answer}"

    k = 27
    answer = solution(w, k)
    print(f"for k={k}, number of canoes is {answer}")
    expected = 4
    assert answer == expected, f"expected={expected} is not equal to actual={answer}"

    # number of canoes does not increase beyond len(w) // 2 + 1
    k = 28
    answer = solution(w, k)
    print(f"for k={k}, number of canoes is {answer}")
    expected = 4
    assert answer == expected, f"expected={expected} is not equal to actual={answer}"