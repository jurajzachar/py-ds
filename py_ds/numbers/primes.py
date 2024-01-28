"""
Let’s count the number of divisors of n. The easiest approach is to iterate through all the
numbers from 1 to n and check whether or not each one is a divisor. The time complexity of
this solution is O(n).
There is a simple way to improve the above solution. Based on one divisor, we can find
the symmetric divisor. More precisely, if number a is a divisor of n, then n
a is also a divisor.
One of these two divisors is less than or equal to √n. (If that were not the case, n would be
a product of two numbers greater than √n, which is impossible.)
"""
def divisors(n: int) -> list[int]:
    i = 1
    result = []
    while i**2 < n: # reduces range to change quadratically from (1..n) to (1..i**2)
        if n % i == 0:
            divisor = n // i
            result += [i, divisor]
        i += 1

    if i ** 2 == n:
        result.append(n)

    return sorted(set(result))

def primality(n: int):
    i = 2
    while i**2 < n:
        if n % i == 0:
            return False
        i += 1
    return True

if __name__ == '__main__':
    for n in [10**1, 10**2, 10**3, 10**4, 10**5, 10**6]:
        print(f"divisors of N={n} are {divisors(n)} and then number {n} is",  f" prime" if primality(n) else " is not prime")