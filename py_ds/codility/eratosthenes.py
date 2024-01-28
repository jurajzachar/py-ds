"""
a sample solution to sieve of Eratosthenes
"""
from typing import List


def solution(n: int) -> List[int]:
    assert n > 1, "number of primes must be greater than 1"

    def gen_composites(x: int) -> List[int]:
        until = n - x
        return [x*i for i in range(2, until)]

    marked = []
    primes = []
    for x in range(2, n + 1):
        if x in marked:
            continue
        else:
            primes.append(x)
            marked += gen_composites(x)

    return primes

if __name__ == '__main__':
    answer = solution(100)
    print(answer)
