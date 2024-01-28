"""
You are given n binary values x(0), x(1), . . . , x(n−1) , such that x i ∈ {0, 1}. This array
represents holes in a roof (1 is a hole). You are also given k boards of the same size. The goal
is to choose the optimal (minimal) size of the boards that allows all the holes to be covered
by boards.
"""


def solution(a: list[int], k: int) -> int:
    assert len(a), "input list must be non empty"
    n = len(a)

    def check(x: int) -> int:
        boards, last = 0, -1
        for i in range(n):
            if a[i] == 1 and last < i:
                boards += 1
                last = i + x - 1
        return boards

    start, end, result = 0, n-1, -1
    while start <= end:
        mid = (start + end) // 2
        if check(mid) <= k:
            end = mid - 1
            result = mid
        else:
            start = mid + 1
    return result


if __name__ == '__main__':
    a = [0, 1, 1, 0, 1, 0]
    answer = solution(a, 2)
    print(answer)

    a = [0, 1, 1, 1, 0, 1, 0]
    answer = solution(a, 2)
    print(answer)

    a = [1, 0, 0, 0, 0, 0, 1]
    answer = solution(a, 2)
    print(answer)