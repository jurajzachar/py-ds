from typing import List, Any


def binary_search(l: List[Any], target: Any) -> Any:
    left, right = 0, len(l) - 1
    tmp = l.copy()
    tmp.sort()

    while left <= right:
        mid = (left + right) // 2
        candidate = tmp[mid]
        if target == candidate:
            return candidate
        elif target < candidate:
            right = mid - 1
        else:
            left = mid + 1

    return -1

if __name__ == '__main__':
    a = [x for x in range(10**9)]
    answer = binary_search(a, 123456789)
    print(answer)