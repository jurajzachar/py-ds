"""
An array A consisting of N integers is given. It contains daily prices of a stock share for a period of N consecutive
days. If a single share was bought on day P and sold on day Q, where 0 ≤ P ≤ Q < N, then the profit of such transaction is
equal to A[Q] − A[P], provided that A[Q] ≥ A[P]. Otherwise, the transaction brings loss of A[P] − A[Q].

For example, consider the following array A consisting of six elements such that:
  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367

If a share was bought on day 0 and sold on day 2, a loss of 2048 would occur because A[2] − A[0] = 21123 − 23171 = −2048.
If a share was bought on day 4 and sold on day 5, a profit of 354 would occur because A[5] − A[4] = 21367 − 21013 = 354.
Maximum possible profit was 356. It would occur if a share was bought on day 1 and sold on day 5.

Write a function,

    def solution(A)

that, given an array A consisting of N integers containing daily prices of a stock share for a period of N consecutive
days, returns the maximum possible profit from one transaction during this period. The function should return 0 if it was
impossible to gain any profit.

For example, given array A consisting of six elements such that:
  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367

the function should return 356, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..400,000];
        each element of array A is an integer within the range [0..200,000].
"""

def solution(log: list[int]):
    assert len(log) > 0, "input list myst be non-empty"
    # sort stock prices off a copy to stay pure without side effects
    x = sorted([x for x in enumerate(log.copy())], key=lambda x : x[1])
    print(x)
    buy_on = x[0]

    def profit(sell: tuple[int, int]):
        return sell[1] - buy_on[1]

    pnl = 0
    sell_on = buy_on  # no profit being default case

    for idx, price in x[1:]:
        # check day is consecutive wrt. buy_on
        if idx < buy_on[0]:
            continue
        check = profit((idx, price))
        if check > pnl:
            pnl = check
            sell_on = (idx, price)

    return pnl, sell_on

if __name__ == '__main__':
    log = [23171, 21011, 21123, 21366, 21013, 21367]
    answer = solution(log)
    print(answer)
    assert answer[0] == 356

