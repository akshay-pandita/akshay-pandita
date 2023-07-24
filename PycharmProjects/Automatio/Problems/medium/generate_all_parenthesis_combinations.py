# Important problem # recursion

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

# Uses backtracking logic

def generateParentheses(n):
    result = []

    def backtrack(left, right, current):
        if left == 0 and right == 0:
            result.append(current)
            return

        if left > 0:
            backtrack(left - 1, right, current + '(')

        if right > left:
            backtrack(left, right - 1, current + ')')

    backtrack(n, n, "")
    return result

print (generateParentheses(3))

