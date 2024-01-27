"""
Let’s define a problem relating to maximum slices. You are given a sequence of n integers
a(0) , a(1) , . . . , a(n−1) and the task is to find the slice with the largest sum. More precisely, we are
looking for two indices p, q such that the total a(p) + a(p+1) + . . . + a(q) is maximal. We assume
that the slice can be empty and its sum equals 0.

Example:

    a = [5, -7, 3, 5, -2, 4, -1]
    largest_slice = a[2:6] = [3, 5, -2, 4]

"""

def solution(a: list[int]) -> tuple[int, int, int]:
    assert len(a) > 0, "array must be non-empty"
    start = 0
    end = 0
    max_ending = max_slice = end
    for index, elem in enumerate(a):
        new_max_ending = max_ending + elem
        if new_max_ending > max_ending:
            end = index
        max_ending = max(0, new_max_ending)
        new_max_slice = max(max_slice, max_ending)
        if new_max_slice > max_ending:
            start = index
        max_slice = new_max_slice
    return (start, end, max_slice)

if __name__ == '__main__':
    a = [5, -7, 3, 5, -2, 4, -1]
    answer = solution(a)
    print(answer)