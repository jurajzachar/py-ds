from typing import List


def prefix_sums(a: List[int]) -> List[int]:
    n = len(a)
    assert n > 0, "array must be non-empty"
    # initialize empty array holding prefix sums
    p = [0] * (n + 1)
    for k in range(1, n + 1):
        p[k] = p[k - 1] + a[k - 1]

    return p

if __name__ == '__main__':
    a = [x for x in range(1, 11)]
    print(a)
    ps = prefix_sums(a)
    print(ps)