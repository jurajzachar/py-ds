from typing import List


def solution(n: int, end_values: List[int]) -> List[int]:
    # initialize counters
    counters = dict([(counter, 0) for counter in range(n)])
    max_value = n

    #iterate over end values and adjust counters
    for (index, x) in enumerate(end_values):
        # case increase specific counter
        if x < max_value:
            counters[x -1] += 1
            continue
        if x > max_value:
            for k in counters.keys():
                counters[k] = max(counters.values())

    # return value for counters
    return list(counters.values())

if __name__ == '__main__':
    n = 5
    array = [3, 4, 4, 6, 1, 4, 4]

    answer = solution(n, array)
    print(answer)

    assert answer == [3, 2, 2, 4, 2]