# Task: Write a program that takes an array A and an index i into A, and rearranges the elements such
# that all elements less than A[i] (the "pivot") appear first, followed by elements equal to the pivot,
# followed by elements greater than the pivot.

# result should be [0, 1, 0, 1, 1, 2, 2]

# 1. Extra space with three arrays
# Time O(n), space O(n)
def dutch_flag (A, pivot_index):
    pivot = A[pivot_index]
    less_than = []
    more_than = []
    equals_to = []
    
    for v in A:
        if v > pivot:
            more_than.append(v)
        elif v < pivot:
            less_than.append(v)
        else:
            equals_to.append(v)
            
    return less_than + equals_to + more_than

# 2. Constant space
# Time O(n), space O(1)
def dutch_flag_partition (A, pivot_index):
    pivot = A[pivot_index]
    
    # On the first pass move all the elements less than pivot to the beginning
    smaller = 0
    for x in range(len(A)):
        if A[x] < pivot:
            A[x], A[smaller] = A[smaller], A[x]
            smaller += 1
    
    # On the second pass move all the elements more than pivot to the end
    larger = len(A) - 1
    for x in reversed(range(len(A))):
        if A[x] < pivot:
            break
        elif A[x] > pivot:
            A[x], A[larger] = A[larger], A[x]
            larger -= 1
            
    return A

print(dutch_flag([0,1,2,0,2,1,1], 2))
print(dutch_flag_partition([0,1,2,0,2,1,1], 2))
