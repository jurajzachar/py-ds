"""
We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the
radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (
assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:
  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0

  <a href="https://codility-frontend-prod.s3.amazonaws.com/media/task_static/number_of_disc_intersections/static/images
  /auto/0eed8918b13a735f4e396c9a87182a38.png"/>

There are eleven (unordered) pairs of discs that intersect, namely:

        discs 1 and 4 intersect, and both intersect with all the other discs;
        disc 2 also intersects with discs 0 and 3.

Write a function:

    def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting
discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [0..2,147,483,647].
"""
from typing import List, Tuple


def solution(a: List[int]) -> List[Tuple[int, int]]:
    """
    returns a list of tuples that denote disc intersections
    """
    assert len(a) >= 2, "array must be of size 2 or greater"

    intersections = []
    n = len(a)
    # calculate x coordinates --> (a_index, xleft, xright) --> radius = (xright - a_index)
    x = [(x[0], ((x[0]) - x[1]), (x[0] + x[1])) for x in [x for x in enumerate(a)]]
    min_range = min(min(x, key=lambda x: x[1]))
    max_range = max(max(x, key=lambda x: x[2]))
    rs = [x for x in range(min_range, max_range + 1)]
    intersections = 0

    for check in rs:
        n = 0
        #TODO

if __name__ == '__main__':
    a = [1, 5, 2, 1, 4, 0]
    answer = solution(a)
    #print(answer)
