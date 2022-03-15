"""
Program to solve canSum problem.

Time Complexity: O(n^m)
Space Complexity: O(m)
where m = target and n = list length
"""
def can_sum(target, numbers):
    # Base cases / stopping conditions
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
        if can_sum(difference, numbers):
            return True
    return False
    
if __name__ == '__main__':
    print(can_sum(7, [2, 3])) # True
    print(can_sum(7, [5, 3, 4, 7])) # True
    print(can_sum(7, [2, 4])) # False
    print(can_sum(8, [2, 3, 5])) # True
    print(can_sum(300, [7, 14])) # False
    