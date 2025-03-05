# Tarik Hireche | 202 301 89

import sys

# Sources used for this question:
# https://www.youtube.com/watch?app=desktop&v=LPFhl65R7ww
# https://stackoverflow.com/questions/77668355/binary-search-left-and-right-index-to-find-median-of-two-sorted-arrays

# Fonction à compléter / function to complete:
def solve(nums1, nums2):
    # Ensure nums1 is smaller to optimize binary search
    # We perform binary search on the smaller array
    if len(nums1) > len(nums2):
        temp = nums1
        nums1 = nums2
        nums2 = temp

    x = len(nums1)
    y = len(nums2)

    # Theses two pointers define the search boundaries of the binary search

    # lowPointer initially points to the start of the smaller array (0),
    # representing the scenario where we take no elements from this array into our left partition.
    lowPointer = 0

    # highPointer initially points to the length of the smaller array (x) (which is the length of nums1),
    # representing the scenario where we take all elements from this array into our left partition.
    highPointer = x

    # Binary search on smaller array
    while lowPointer <= highPointer:
        # PartitionA and partitionB are the number of elements taken from arrays nums1 and nums2 respectively
        # as explained in my PDF report.
        PartitionA = (lowPointer + highPointer) // 2
        partitionB = (x + y + 1) // 2 - PartitionA

        # Initialize default boundary values
        maxX = float('-inf')
        minX = float('inf')
        maxY = float('-inf')
        minY = float('inf')

        # Update values based on partitions.
        # maxX: The largest element in the left partition of nums1 (or -inf if partition is at the start).
        # minX: The smallest element in the right partition of nums1 (or inf if partition is at the end).
        # maxY: The largest element in the left partition of nums2 (or -inf if partition is at the start).
        # minY: The smallest element in the right partition of nums2 (or inf if partition is at the end).
        if PartitionA > 0:
            maxX = nums1[PartitionA - 1]
        else:
            maxX = float('-inf')

        if PartitionA < x:
            minX = nums1[PartitionA]
        else:
            minX = float('inf')

        if partitionB > 0:
            maxY = nums2[partitionB - 1]
        else:
            maxY = float('-inf')

        if partitionB < y:
            minY = nums2[partitionB]
        else:
            minY = float('inf')

        # Check if correct partition found
        # This verifies the key condition max(left half) <= min(right half)
        if maxX <= minY and maxY <= minX:  # When true, we've successfully found the correct partitions.
            if (x + y) % 2 == 0:
                # The median is the average of the maximum of the left partitions and minimum of the right partitions.
                return (max(maxX, maxY) + min(minX, minY)) / 2 #
            else: #  The median is simply the maximum element of the left partitions.
                return max(maxX, maxY)

        # This part corresponds to my report's idea of adjusting partitions:
          # If maxX is larger than minY, we move left in nums1.
          # Else, we move right in nums1.
        elif maxX > minY:
            highPointer = PartitionA - 1
        else:
            lowPointer = PartitionA + 1


# Ne pas modifier le code ci-dessous :
# Do not modify the code below :

def process_numbers(input_file):
    try:
        # Read integers from the input file
        with open(input_file, "r") as f:
            lines = f.readlines() 
            l0 = list(map(int, lines[0].split()))    
            l1 = list(map(int, lines[1].split()))    

        return solve(l0,l1)
    
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python Q6.py <input_file>")
        return

    input_file = sys.argv[1]

    print(f"Input File: {input_file}")
    res = process_numbers(input_file)
    print(f"Result: {res}")

if __name__ == "__main__":
    main()