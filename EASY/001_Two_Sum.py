# LeetCode 1
# Two Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum/

# Problem:
# Given an array of integers nums and an integer target,
# return the indices of the two numbers such that they add up to target.
#
# You may assume that each input has exactly one solution,
# and you may not use the same element twice.
#
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation:
# nums[0] + nums[1] = 2 + 7 = 9

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Approach:
# Use a hash map (dictionary) to store numbers and their indices.
#
# Traverse the array once:
# - Calculate the complement = target - current number.
# - Check if the complement already exists in the hash map.
# - If it exists, return the stored index and current index.
# - Otherwise, store the current number and its index.
#
# This allows us to find the required pair in a single pass.

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[num] = i
