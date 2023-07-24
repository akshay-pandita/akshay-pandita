"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

"""



# Solution uses backtracking logic

def combinationSum(candidates, target):
    candidates.sort()  # Sort the candidates in non-decreasing order
    result = []
    combinationSumHelper(candidates, target, [], 0, 0, result)
    return result


def combinationSumHelper(candidates, target, current_combination, start, current_sum, result):
    if current_sum == target:
        result.append(current_combination[:])
        return
    if current_sum > target:
        return
    for i in range(start, len(candidates)):
        candidate = candidates[i]
        current_combination.append(candidate)
        combinationSumHelper(candidates, target, current_combination, i, current_sum + candidate, result)
        current_combination.pop()


# Example usage:
candidates = [2, 3, 6, 7]
target = 7
result = combinationSum(candidates, target)
print(result)