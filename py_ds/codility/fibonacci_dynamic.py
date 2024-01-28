"""
Enumeration of the Fibonacci numbers can be done faster simply by using a basis of
dynamic programming. We can calculate the values F(0) , F(1) , . . . , F(n) based on the previously
calculated numbers (it is sufficient to remember only the last two values)
"""
def solution(n: int)  -> list[int]:
    assert n > 0, "fib number must be positive"
    # initialize the first two elements
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib


if __name__ == '__main__':
    print(solution(10))