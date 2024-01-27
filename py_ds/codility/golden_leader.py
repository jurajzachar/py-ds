"""
Let us consider a sequence a 0 , a 1 , . . . , a n−1 . The leader of this sequence is the element whose
value occurs more than n
2 times.

Example:
a = [6, 8, 4, 6, 8, 6, 6]

In this sequence leader is 6, with occurence=4 which is greater than n//2 = 3

Write an effective algorithm that finds the value
of the leader of the sequence a(0), a(1), . . ., a(n−1); such that 0 <= ai <= 10^9.

If there is no leader, the result should be -1.
"""


def solution(a: list[int]) -> int:
    """
    this solution runs with O(n log n) time complexity
    """
    n = len(a)
    assert 0 <= n <= 10 ** 9, "array length out of bounds"

    if n < 2:
        return a[0]

    leader_threshold = n // 2
    tmp = a.copy()
    tmp.sort()

    idx = 0
    candidate = tmp[idx]
    counter = 1
    while idx + 1 < n:
        if counter >= leader_threshold:
            break;
        next = tmp[idx + 1]
        if next == candidate:
            counter += 1
        else:
            counter = 1
            candidate = next
        idx += 1

    return candidate if counter >= leader_threshold else -1;


def efficient_solution(a: list[int]) -> int:
    """
    this solution runs with 0(n) time complexity
    """
    n = len(a)
    assert 0 <= n <= 10 ** 9, "array length out of bounds"

    if n < 2:
        return a[0]

    leader_threshold = n // 2
    frequency = dict()
    leader = -1

    # each element of the array is considered just once
    for elem in a:
        if elem not in frequency.keys():
            frequency[elem] = 1
        else:
            frequency[elem] += 1
            if frequency[elem] >= leader_threshold:
                leader = elem
                break;

    # no golder leader found
    return leader


if __name__ == '__main__':
    a = [6, 8, 4, 6, 8, 6, 6]
    slow_answer = solution(a)
    assert slow_answer == 6, f"(slow) {slow_answer} was not expected"
    e_answer = efficient_solution(a)
    assert e_answer == 6, f"(efficient) {e_answer} was not expected"

    # this blows up memory for storing twice the number of 4 * 10**9 bytes (8 gigabytes)
    a = [x for x in range(10 ** 9)]
    answer = efficient_solution(a)
    assert answer == -1, f"{answer} was not expected"
