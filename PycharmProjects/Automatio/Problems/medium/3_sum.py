"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

"""

# Algo:

"""
Sort the nums array in ascending order.
Initialize an empty list result to store the triplets.
Iterate through the array from index i = 0 to len(nums) - 3 (we go up to len(nums) - 3 to ensure enough elements for a triplet).
a. If i > 0 and nums[i] == nums[i-1], skip the current iteration to avoid duplicates.
b. Initialize two pointers, left = i + 1 and right = len(nums) - 1.
c. While left < right, do the following:
i. Calculate the current sum as curr_sum = nums[i] + nums[left] + nums[right].
ii. If curr_sum == 0, we found a valid triplet. Append it to result.
- Increment left and decrement right.
- Check for duplicate elements and move left and right accordingly to avoid duplicates.
iii. If curr_sum < 0, increment left to increase the sum.
iv. If curr_sum > 0, decrement right to decrease the sum.
Return the result list containing all the valid triplets.

"""