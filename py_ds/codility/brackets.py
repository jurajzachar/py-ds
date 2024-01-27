"""
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

        S is empty;
        S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
        S has the form "VW" where V and W are properly nested strings.

For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

    def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0,
as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..200,000];
        string S is made only of the following characters: '(', '{', '[', ']', '}' and/or ')'.
"""


def solution(s: str):
    open_chars = {'(', '{', '['}
    closed_chars = {']', '}', ')'}
    # boundary check
    assert len(s) <= 200 * 1000, "string length limit exceeded"
    tokens = [x for x in s]
    diff = set(tokens).difference(open_chars.union(closed_chars))
    assert len(diff) == 0, f"invalid characters detected: {diff}"

    # short-circuit, if the string is not symmetrical
    if len(s) % 2 > 0:
        return 0

    eval_q = []
    for token in tokens:
        if len(eval_q) == 0:
            if token in open_chars:
                eval_q.append(token)
            else:
                return 0
            continue
        peek = eval_q[-1]
        if token in open_chars:
            eval_q.append(token)
        else:
            if (peek == '[' and token == ']') or (peek == '(' and token == ')') or (peek == '{' and token == '}'):
                eval_q.pop()

    return 1 if len(eval_q) == 0 else 0

if __name__ == '__main__':
    s = "{[()()]}"
    assert solution(s) == 1

    s = "([)()]"
    assert solution(s) == 0
