# Tarik Hireche | 202 301 89

import sys

# Space for auxilary functions :

def find_median(numbers):
    """
    this function compute the median of a sorted list.
    If the list has an odd length, returns the middle element.
    If the list has an even length, returns the integer division of the sum of the two middle elements.
    """
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        return (numbers[n // 2 - 1] + numbers[n // 2]) // 2


def solve(numbers):
    """
    Finds the number of distinct pairs in a sorted list whose sum equals the median.
    Uses a two-pointer technique to efficiently count the pairs.
    source used : https://www.geeksforgeeks.org/two-pointers-technique/
    Parameters:
    numbers (list of int): A sorted list of integers.

    Returns:
    int: The number of unique pairs whose sum equals the median.
    """
    n = len(numbers)
    if n == 0:
        return 0

    # Compute the median value with the aux function
    median = find_median(numbers)

    # we use the two pointers to find distinct pairs summing to the median
    left = 0
    right = n - 1
    pairs = set() # We create a set to store the distinct pairs

    while left < right:
        s = numbers[left] + numbers[right]

        # If the sum matches the median, store the pair and move both pointers
        if s == median:
            pairs.add((numbers[left], numbers[right]))
            left += 1
            right -= 1

        # If the sum is less than the median, move left pointer to increase the sum
        elif s < median:
            left += 1

        # If the sum is greater than the median, move right pointer to decrease the sum
        else:
            right -= 1

    return pairs
# Ne pas modifier le code ci-dessous :
# Do not modify the code below :

def process_numbers(input_file):
    try:
        # Read integers from the input file
        with open(input_file, "r") as f:
            content = f.read()
        
        # Convert content into a list of integers
        numbers = list(map(int, content.split()))

        pairs = solve(numbers)

        return(len(pairs))

    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python Q3.py <input_file>")
        return

    input_file = sys.argv[1]

    print(f"Input File: {input_file}")
    res = process_numbers(input_file)
    print(f"Result: {res}")

if __name__ == "__main__":
    main()

