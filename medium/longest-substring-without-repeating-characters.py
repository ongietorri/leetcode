https: // leetcode.com/problems/longest-substring-without-repeating-characters/submissions/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """ linear time or O(n^2) worst case (?) """

        max_length = 0
        substring_start_index = 0
        charset = {}

        for index, char in enumerate(s):
            rep_index = charset.get(char, -1)
            if rep_index == -1 or rep_index < substring_start_index:
                max_length = max(max_length, index - substring_start_index + 1)
            else:
                substring_start_index = rep_index + 1

            charset[char] = index
        return max_length

    def lengthOfLongestSubstring_(self, s: str) -> int:
        """ brute force O(n^2) and O(n^3) worst case """
        max_length = 0

        def get_length(s_cur):
            chars = set()
            for c in s_cur:
                if c not in chars:
                    chars.add(c)
                else:
                    break
            return len(chars)

        for ix, c in enumerate(s):
            max_length = max(max_length, get_length(s[ix:]))

        return max_length
