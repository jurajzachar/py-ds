"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""


def lengthOfLongestSubstring(s: str) -> int:
    assert len(s) > 0, "string must be non-empty"

    l = [c for c in s]
    # minimum length of any given string
    answer = 1

    for i in range(len(l)):
        idx = i
        elem = l[idx]
        uniq = set(elem)

        while (idx := idx + 1) < len(s):
            elem = l[idx]
            # found a unique character
            if elem not in uniq:
                uniq.add(elem)
            # already seen the character
            else:
                # reset uniq
                uniq.clear()
            answer = max(answer, len(uniq))

    return answer


if __name__ == '__main__':
    assert lengthOfLongestSubstring("abcabcbb") == 3
    assert lengthOfLongestSubstring("bbbbb") == 1
    assert lengthOfLongestSubstring("pwwkew") == 3
    assert lengthOfLongestSubstring("123abc123456xyz") == 12