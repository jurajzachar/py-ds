"""
You are given n sticks (of lengths 1 <= a(0) <= a(1) <= . . . <= a(n−1) <= 10^9).

The goal is to count the number of triangles that can be constructed using these sticks. More precisely,
we have to count the number of triplets at indices x < y < z, such that a(x) + a(y) > a(z).
"""

def solution(a: list[int]) -> int:
    n = len(a)
    assert n > 0, "input list must be non-empty"
    result = 0
    for x in range(n):
        z = x + 2
        y = x + 1
        for yi in range(y, n):
            while z < n and a[x] + a[yi] > a[z]:
                z += 1
            result += (z - y - 1)

    return result

if __name__ == '__main__':
    a = [3, 2, 4]
    answer = solution(a)
    print(answer)