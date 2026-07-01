<h1 align="center">🚀 LeetCode DSA (Python) Solutions</h1>

<p align="center">
  <img src="https://img.shields.io/badge/LEETCODE-PROBLEMS-orange?style=for-the-badge&logo=leetcode" />
  <img src="https://img.shields.io/badge/LANGUAGE-PYTHON-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/FOCUS-DSA-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/STATUS-ACTIVE-brightgreen?style=for-the-badge" />
</p>

<p align="center">
  <b>Daily LeetCode Solutions in Python</b><br>
  Building Strong DSA Foundations • Interview Preparation • Consistent Learning
</p>

---

## Overview

This repository contains my daily LeetCode problem-solving practice using Python.

The goal of this repository is to strengthen:

- Data Structures & Algorithms (DSA)
- Python Programming
- Problem-Solving Skills
- Coding Interview Preparation
- Consistency in Daily Practice

---

## Topics Covered

- Arrays
- Strings
- Hash Maps
- Two Pointers
- Sliding Window
- Linked Lists
- Stacks
- Queues
- Binary Search
- Trees
- Recursion
- Backtracking
- Dynamic Programming
- Graphs
- Greedy Algorithms

---

## Repository Structure

```text
leetcode-python-dsa-solutions/
│
├── Easy/
├── Medium/
├── Hard/
└── README.md
```

---

## Problem Format

Each solution file contains:

- Problem Name
- Approach / Intuition
- Python Solution
- Time Complexity
- Space Complexity
- Key Learning

### Example

```python
# LeetCode 35
# Search Insert Position

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
```

**Time Complexity:** O(log n)

**Space Complexity:** O(1)

**Key Learning:** Binary Search can be used not only to find an element but also to determine its correct insertion position.

---

## 🎯 Progress Target

- ✅ Complete 50 Easy Problems
- ⏳ Complete 50 Medium Problems
- ⏳ Complete 20 Hard Problems
- 🎯 Reach 120+ LeetCode Problems Solved
- 🎯 Strengthen DSA Fundamentals
- 🎯 Become Interview Ready

---


## 📊 Problem Difficulty Guide

| Symbol | Difficulty |
|---------|------------|
| 🟢 | Easy |
| 🟡 | Medium |
| 🔴 | Hard |

---

## Solved Problems

| Day | Problem ID | Problem Name | Difficulty | Solution |
|------|------------|----------------------------------------------------|------------|----------|
| Day 1 | 1 | Two Sum | 🟢 Easy | [🔗 View](https://leetcode.com/problems/two-sum/) ||
| Day 2 | 9 | Palindrome Number | 🟢 Easy | [🔗 View](https://leetcode.com/problems/palindrome-number/) |
| Day 3 | 13 | Roman to Integer | 🟢 Easy | [🔗 View](https://leetcode.com/problems/roman-to-integer/) |
| Day 4 | 14 | Longest Common Prefix | 🟢 Easy | [🔗 View](https://leetcode.com/problems/longest-common-prefix/) |
| Day 5 | 20 | Valid Parentheses | 🟢 Easy | [🔗 View](https://leetcode.com/problems/valid-parentheses/) |
| Day 6 | 21 | Merge Two Sorted Lists | 🟢 Easy | [🔗 View](https://leetcode.com/problems/merge-two-sorted-lists/) |
| Day 7 | 26 | Remove Duplicates from Sorted Array | 🟢 Easy | [🔗 View](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) |
| Day 8 | 27 | Remove Element | 🟢 Easy | [🔗 View](https://leetcode.com/problems/remove-element/) |
| Day 9 | 28 | Find the Index of the First Occurrence in a String | 🟢 Easy | [🔗 View](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) |
| Day 10 | 35 | Search Insert Position | 🟢 Easy | [🔗 View](https://leetcode.com/problems/search-insert-position/) |
| Day 11 | 58 | Length of Last Word | 🟢 Easy | [🔗 View](https://leetcode.com/problems/length-of-last-word/) |
| Day 12 | 66 | Plus One | 🟢 Easy | [🔗 View](https://leetcode.com/problems/plus-one/) |
| Day 13 | 67 | Add Binary | 🟢 Easy | [🔗 View](https://leetcode.com/problems/add-binary/) |
| Day 14 | 189 | Rotate Array | 🟡 Medium | [🔗 View](https://leetcode.com/problems/rotate-array/) |
| Day 15 | 53 | Maximum Subarray | 🟡 Medium | [🔗 View](https://leetcode.com/problems/maximum-subarray/) |
| Day 16 | 152 | Maximum Product Subarray | 🟡 Medium | [🔗 View](https://leetcode.com/problems/maximum-product-subarray/) |


---

## Progress Tracker

| Difficulty | Problems Solved |
|------------|----------------|
|  Easy | 13 |
|  Medium | 3 |
|  Hard | 0 |
| **TOTAL** | **16** |

---

## Goals

- Solve LeetCode problems consistently
- Master Data Structures & Algorithms
- Improve coding interview skills
- Strengthen Python programming
- Build a strong GitHub portfolio
- Document and share my learning journey

---

## Connect With Me

- [LinkedIn](https://www.linkedin.com/in/bhoomisingh2305/)
  
---

⭐ If you find these solutions helpful in your learning journey, please consider giving this repository a star. Your support is greatly appreciated!
