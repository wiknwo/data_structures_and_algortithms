"""
    Program to generate all permuatations of a 
    list of numbers and return the permutations in
    any order demonstrating a medium recursion
    and backtracking.
"""
def permute(numbers):
    permutations = []

    # Base case / stopping condition
    if len(numbers) == 1:
        return [numbers[:]]
    
    # Go through every value in numbers
    for i in range(len(numbers)):
        number = numbers.pop(0)
        # Inductive step: Do some work to shrink the problem space
        intermediate_permutations = permute(numbers)
        # Appending the popped value to each of the intermediate permutations
        for permutation in intermediate_permutations:
            permutation.append(number)
        # Add intermediate permutations to permutations list
        permutations += intermediate_permutations
        # Backtrack: Append number to the end of the list
        # instead of the front as we have calculated 
        # permutations with that number already
        numbers.append(number)
    return permutations

if __name__ == '__main__':
    print(permute([1, 2, 3]))