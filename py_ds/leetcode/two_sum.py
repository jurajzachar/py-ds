"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

     Given nums = [2, 7, 11, 15], target = 9,

     Because nums[0] + nums[1] = 2 + 7 = 9,

     return [0, 1]
"""
from typing import Tuple, List


def solution(l: List[int], target: int) -> Tuple[int, int]:
    assert len(l) > 1, "array must be at least of size 2 or greater"

    answer = (0, 1)

    for idx in range(0, len(l) - 1):
        a = l[idx]
        next = idx + 1
        while next < len(l):
            b = l[next]
            if b > target:
                next += 1
                continue
            if a + b == target:
                answer = (l.index(a), l.index(b))
                break
            next += 1

    return answer

if __name__ == '__main__':
    l = [2, 7, 11, 15]
    target = 9
    assert solution(l, target) == (0, 1)

    l = [1, 9, 5, 10, 19, 100]
    target = 119
    assert solution(l, target) == (4, 5)