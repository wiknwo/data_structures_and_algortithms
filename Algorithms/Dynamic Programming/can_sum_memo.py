"""
Program to solve canSum problem.

Write a function can_sum(target, numbers)
that takes in a target and a list of numbers
as arguments. 

The funciton should return a boolean indicating
whether or not it is possible to generate the
target using numbers from the list.

You may use an item of the list as many times
as needed.

You may assume that all input numbers are nonnegative

Time Complexity: O(m * n)
Space Complexity: O(m)
where m = target and n = list length
"""
def can_sum(target, numbers, memo = {}):
    # Base cases / stopping conditions
    if target in memo:
        print(memo)
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False
    # Iterate through numbers in list and
    # check if there exists a number whose
    # difference from the target is equal to 0
    # then return true
    for number in numbers:
        difference = target - number
        # Inductive step: Do some work to shrink the problem space
        if can_sum(difference, numbers, memo):
            # Look at all return values that were not base cases
            # and determine the value to store in the memo
            memo[target] = True
            print(memo)
            return True
    memo[target] = False
    print(memo)
    return False
    
if __name__ == '__main__':
    # The below test cases return the correct truth values 
    # when executed individually but when executed in 
    # sequence, we get the wrong truth values. An overflow
    # of sorts perhaps.

    print(can_sum(7, [2, 3])) # True
    # print(can_sum(7, [5, 3, 4, 7])) # True
    # print(can_sum(7, [2, 4])) # False
    # print(can_sum(8, [2, 3, 5])) # True
    # print(can_sum(300, [7, 14])) # False
    