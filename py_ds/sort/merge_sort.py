from typing import List, Any


def merge_sort(a: List[Any]) -> List[Any]:
    """
    this is a top-down recursive implementation using lists
    """

    def merge(left: List[Any], right: List[Any]) -> List[Any]:
        result = []
        """
        a helper function which merges two lists together in natural ordering of the first elements
        """
        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        # either left or right have left-overs; consume them.
        while len(left) > 0:
            result.append(left.pop(0))
        while len(right) > 0:
            result.append(right.pop(0))

        return result

    # base case: a list of zero or one element is sorted, by definition
    if len(a) <= 1:
        return a

    # recursive case: divide the lists into two half
    mid = len(a) // 2
    _left = merge_sort(a[:mid])
    _right = merge_sort(a[mid:len(a)])

    # merge the singleton lists
    return merge(_left, _right)


if __name__ == '__main__':
    a = [4, 1, 2, 2, 5, 3] * 10
    print(a)
    print(merge_sort(a))
