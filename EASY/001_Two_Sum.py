# LeetCode 66
# Plus One
# Difficulty: Easy
# Link: https://leetcode.com/problems/plus-one/

# Problem:
# You are given a large integer represented as an integer array digits,
# where each digits[i] is the ith digit of the integer.
#
# The digits are ordered from most significant to least significant
# in left-to-right order. The large integer does not contain any
# leading zeros.
#
# Increment the large integer by one and return the resulting array
# of digits.

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]

# Example 3:
# Input: digits = [9]
# Output: [1,0]

# Approach:
# Reverse the array so that we can process digits
# from least significant to most significant.
#
# - Initialize a carry with value 1 since we need
#   to add one to the number.
# - If the current digit is 9, change it to 0 and
#   keep the carry.
# - Otherwise, increment the digit and stop the process.
# - If all digits become 0, append 1 to handle the
#   remaining carry.
# - Reverse the array back before returning.
#
# This simulates the way addition is performed manually.

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]

        carry = 1
        i = 0

        while carry:

            if i < len(digits):

                if digits[i] == 9:
                    digits[i] = 0

                else:
                    digits[i] += 1
                    carry = 0

            else:
                digits.append(1)
                carry = 0

            i += 1

        return digits[::-1]
