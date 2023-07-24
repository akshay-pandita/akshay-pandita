"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

"""


# Solution:
"""
We can use binary search two times, first to find the starting index and 
then the next time to find the ending index.
"""