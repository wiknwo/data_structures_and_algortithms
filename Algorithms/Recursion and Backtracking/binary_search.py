"""
    Program to perform a binary search algorithm demonstrating recursion.
    In a nutshell, this search algorithm takes advantage of a collection 
    of elements that is already sorted by ignoring half of the elements 
    after just one comparison. It is an example of a decrease-and-conquer
    algorithm and two pointers
"""
def binary_search(arr, left_index, right_index, target):
    # Base case / stopping condition
    # Target was not found in the list
    if left_index > right_index:
        return -1

    midpoint_index = (left_index + right_index) // 2

    # Base case / stopping condition
    # Target found in list
    if target == arr[midpoint_index]:
        return midpoint_index
    
    # Inductive step: Do some work to shrink the problem space
    # If the target is not in the right half of the list then
    # we search the left half
    if target < arr[midpoint_index]:
        return binary_search(arr, left_index, midpoint_index - 1, target)
    else:
        # If the target is not in the right half of the list then
        # we search the left half
        return binary_search(arr, midpoint_index + 1, right_index, target)

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6]
    print(binary_search(a, 0, len(a) - 1, 6))
    print(binary_search(a, 0, len(a) - 1, 10))    
