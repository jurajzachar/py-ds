"""
Problem: You are given a zero-indexed array A consisting of n integers: a 0 , a 1 , . . . , a n−1 .
Array A represents a scenario in a grocery store, and contains only 0s and/or 1s:
• 0 represents the action of a new person joining the line in the grocery store,
• 1 represents the action of the person at the front of the queue being served and leaving
the line.
The goal is to count the minimum number of people who should have been in the line before
the above scenario, so that the scenario is possible (it is not possible to serve a person if the
line is empty)
"""


def grocery_store(a: list[int]) -> int:
    queue = []
    head, tail = 0, 0
    counter = 0
    for elem in a:
        print(queue, counter)
        counter += 1
        if elem == 0:
            queue.append(elem)
            tail += 1
            continue
        if elem == 1:
            if len(queue) == 0:
                break
            queue.pop()
            tail -= 1
            continue
        raise Exception(f"unsupported operation={elem}")

    return counter


if __name__ == '__main__':
    a = [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1]
    min_customers = grocery_store(a)
    print(min_customers)
    assert min_customers == 15