"""
Given a list of coins  denominated as
  - 1 cents
  - 5 cents
  - 10 cents

Determine the total number of combinations of the coins in the given list to make up the number N.

Example:

With coins demonominated in 1, 5 and 10 cents, there are two ways of obtaining 8 cents:

  - (1 + 1 + 1 + 1 + 1 + 1 + 1 + 1) = 8
  - (1 + 1 + 1 + 5) = 8

Write a function:

    def solution(n)

Which finds all possible coin changes for given number N
"""
from typing import List, Set, Tuple


def solution(coins: Set[int], n: int) -> List[List[int]]:
    def coin_change(coin: int, x: int) -> Tuple[List[int], int]:
        '''
        helper pure function which generates a tuple of coin change and a remainder, or 0 if there's none
        '''
        floor = x // coin
        remainder = x % coin
        return ([coin] * floor, remainder)

    def get_changing_coins(x: int) -> List[int]:
        lesser = set([c for c in coins if c <= x])
        return [c for c in lesser if x % c == 0]

    combinations = []

    for coin in coins:
        change, remainder = coin_change(coin, n)
        # first outcome: there's no remainder so we enumerate all possible coin changes
        if remainder == 0:
            combinations.append(change)
            next_change = get_changing_coins(coin)
            for next in next_change:
                combinations.append([coin] + coin_change(next, coin)[0])
        # second outcome: there's a remainder which get's broken down into coin changes
        else:
            remainder_changes = get_changing_coins(remainder)
            for r in remainder_changes:
                combinations.append(change + coin_change(r, remainder)[0])

    # drop compbinations which don't add up to n and remove duplicates
    return [solution for solution in set([tuple(x) for x in combinations if sum(x) == n])]

if __name__ == '__main__':
    answer = solution({1, 5, 10}, 10)
    print(answer)
    assert len(answer) == 4
    # [(5, 1, 1, 1, 1, 1), (5, 5), (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (10,)]