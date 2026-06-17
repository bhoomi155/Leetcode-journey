# LeetCode 67
# Add Binary
# Difficulty: Easy
# Link: https://leetcode.com/problems/add-binary/

# Problem:
# Given two binary strings a and b, return their sum
# as a binary string.
#
# The input strings consist only of characters '0' and '1'.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

# Approach:
# Use two pointers starting from the end of both strings
# since binary addition is performed from right to left.
#
# - Initialize a carry variable with 0.
# - Add the current digits from both strings along with carry.
# - Store total % 2 as the current binary digit.
# - Update carry as total // 2.
# - Continue until all digits and any remaining carry
#   have been processed.
# - Reverse the result before returning because digits
#   are collected from right to left.
#
# This simulates the way binary addition is performed manually.

# Time Complexity: O(max(n, m))
# Space Complexity: O(max(n, m))

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))
            carry = total // 2

        return ''.join(result[::-1])
