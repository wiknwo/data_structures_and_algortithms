"""
    Program to solve Tower of Hanoi puzzle recursively.
    It is also another example of a decrease-and-conquer 
    algorithm. Decrease-and-Conquer only requires reducing 
    the problem to a single smaller problem, such as the 
    classic Tower of Hanoi puzzle, which reduces moving a 
    tower of height n to moving a tower of height n - 1.

    The Tower of Hanoi / The Problem of Benares Temple / Tower of Brahma / Lucas' Tower / Towers / Pyramid Puzzle
    is a mathematical game or puzzle consisting of three rods and a number of disks of various diameters, which can
    slide onto any rod. The puzzle begins with the disks stacked on one rod in order of decreasing size, the smallest 
    at the top and largest at the bottom. The objective of the puzzle is to move the entire stack to the last rod, 
    obeying the following rules:

    1. Only one disk may be moved at a time.
    2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or 
    on an empty rod.
    3. No disk may be placed on top of a disk that is smaller than it.

    With 3 disks, the puzzle can be solved in 7 moves. The minimal number of moves required to solve a Tower of Hanoi 
    puzzle is 2^n - 1, where n is the number of disks.
"""
def tower_of_hanoi(n , source, destination, auxiliary):
    """Function to solve Tower of Hanoi puzzle recursively

    Params:
        n(int): Number of disks to be moved
        source(char): Rod where disk is present
        destination(char): Rod where disk is to be moved
        auxiliary(char): The remaining rod

    Return:

    Raises:
    """
    # Base case / stopping condition
    if n == 1:
        # Print the move made
        print("Move disk 1 from source", source, "to destination", destination)
        return

    # Inductive step: Do some work to shrink the problem space
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    # Print the move made
    print("Move disk", n, "from source", source, "to destination", destination)
    # Inductive step: Do some work to shrink the problem space
    tower_of_hanoi(n - 1, auxiliary, destination, source)

if __name__ == '__main__':
    tower_of_hanoi(3, 'A', 'B', 'C')