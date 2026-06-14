# LeetCode 35
# Search Insert Position
# Difficulty: Easy
# Link: https://leetcode.com/problems/search-insert-position/

# Problem:
# Given a sorted array of distinct integers and a target value,
# return the index if the target is found.
# If not, return the index where it would be inserted
# in order to maintain the sorted order.
#
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

# Approach:
# Since the array is sorted, Binary Search can be used
# to efficiently locate the target.
#
# - Initialize two pointers: left and right.
# - Find the middle element of the current search range.
# - If the target matches the middle element,
#   return its index.
# - If the target is greater, search the right half.
# - Otherwise, search the left half.
# - When the search ends, the left pointer indicates
#   the correct insertion position.
#
# This satisfies the required O(log n) runtime complexity.

# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return l
