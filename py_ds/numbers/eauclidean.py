"""
The Euclidean algorithm is based on the principle that the greatest common divisor of two numbers does not change if the
larger number is replaced by its difference with the smaller number. For example, 21 is the GCD of 252 and 105 (as 252 =
21 × 12 and 105 = 21 × 5), and the same number 21 is also the GCD of 105 and 252 − 105 = 147. Since this replacement
reduces the larger of the two numbers, repeating this process gives successively smaller pairs of numbers until the two
numbers become equal. When that occurs, they are the GCD of the original two numbers.
"""


def gcd(a: int, b: int) -> int:
    """original Euclid's version that works on positive integers"""
    assert a > 0, f"a={a} must be positive"
    assert b > 0, f"b={b} must be positive"
    while a != b:
        if a > b:
            a = a -b
        else:
            b = b - a
    return a

def gcd_mod(a: int, b: int) -> int:
    """extended version which also works on negative inters"""
    while a > 0:
        tmp = a
        a = b % a
        b = tmp
    return b

if __name__ == '__main__':
    answer = gcd(252, 105)
    expected = 21
    assert answer == expected, f"expected={expected} is not equal to actual={answer}"

    answer = gcd_mod(252, 105)
    expected = 21
    assert answer == expected, f"expected={expected} is not equal to actual={answer}"