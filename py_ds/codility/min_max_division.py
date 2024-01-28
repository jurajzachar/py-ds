"""
You are given integers K, M and a non-empty array A consisting of N integers. Every element of the array is not greater than M.

You should divide this array into K blocks of consecutive elements. The size of the block is any integer between 0 and N.
Every element of the array should belong to some block.

The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y]. The sum of empty block equals 0.

The large sum is the maximal sum of any block.

For example, you are given integers K = 3, M = 5 and array A such that:
  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2

The array can be divided, for example, into the following blocks:

        [2, 1, 5, 1, 2, 2, 2], [], [] with a large sum of 15;
        [2], [1, 5, 1, 2], [2, 2] with a large sum of 9;
        [2, 1, 5], [], [1, 2, 2, 2] with a large sum of 8;
        [2, 1], [5, 1], [2, 2, 2] with a large sum of 6.

The goal is to minimize the large sum. In the above example, 6 is the minimal large sum.

Write a function:

    def solution(K, M, A)

that, given integers K, M and a non-empty array A consisting of N integers, returns the minimal large sum.

For example, given K = 3, M = 5 and array A such that:
  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2

the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

        N and K are integers within the range [1..100,000];
        M is an integer within the range [0..10,000];
        each element of array A is an integer within the range [0..M].
"""

def solution(k: int, m: int, a: list[int]) -> int:
    """
    apply binary search where the start is the maximum element and end is the sum. The minimum largest sum would be in this
    range.

    For each trial, check whether we can squeeze the elements into fewer blocks than the block number requested.
    If it is fewer, it is okay because we can use empty blocks. If it is equal, that is also acceptable.
    However, it is greater, then we can conclude that the tried minimum largest sum needs to be higher to allow
    individual blocks to be larger to reduce the block count.

    One general principle can be observed above that the more fairly we distribute the sums of the blocks,
    the largest will become the minimum possible. For this, we need to squeeze as many elements into an individual block
    as possible.

    If the number of blocks for a tried minimum largest sum is smaller than the expected block count, then we can try
    a slightly smaller minimum largest sum, otherwise we have to try a bit greater until we eventually find the best number.
    """

    n = len(a)
    assert  1 < n < 10**5
    start = max(a)
    end = sum(a)

    def check(largest_sum: int):
        _sum, count = 0, 0
        for elem in a:
            print(f"sum={_sum}, count={count}")
            if _sum + elem > largest_sum:
                # reset sum
                _sum = 0
                # update counter
                count += 1
                # stop looping if we've exceeded the size of the requested block
                if count >= k:
                    break
            _sum += elem
        return count

    while start <= end:
        mid = (start + end) // 2
        print(f"start={start}, end={end}, mid={mid}")
        if check(mid) < k:
            end = mid -1
        else:
            start = mid + 1

    return start

if __name__ == '__main__':
    a = [2, 1, 5, 1, 2, 2, 2]
    answer = solution(3, 5, a)
    print(answer)
