# LeetCode 58
# Length of Last Word
# Difficulty: Easy
# Link: https://leetcode.com/problems/length-of-last-word/

# Problem:
# Given a string s consisting of words and spaces,
# return the length of the last word in the string.
#
# A word is a maximal substring consisting of
# non-space characters only.

# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation:
# The last word is "World" with length 5.

# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation:
# The last word is "moon" with length 4.

# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation:
# The last word is "joyboy" with length 6.

# Approach:
# Traverse the string from right to left.
#
# - Ignore trailing spaces by finding the first
#   non-space character from the end.
# - Store its index as the end of the last word.
# - Continue moving left until a space is found.
# - The difference between the end index and the
#   space index gives the length of the last word.
# - If no space is encountered, the entire string
#   up to the end index is the last word.
#
# This approach avoids using extra space and
# processes the string in a single reverse traversal.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j = -1

        for i in range(len(s) - 1, -1, -1):

            if s[i] != ' ' and j == -1:
                j = i

            elif s[i] == ' ' and j != -1:
                return j - i

        return j + 1
