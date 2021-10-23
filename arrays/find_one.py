# Task: Find the element that appears once in an array where every other element appears twice

# 1. Extra space to count numbers
def find_one (A):
    num_count = {}
    
    for x in A:
        if x in num_count:
            num_count[x] += 1
        else:
            num_count[x] = 1

    for k,v in num_count.items():
        if v == 1:
            return k
            
# 2. Sort and pointers
def find_one_sort (A):
    A = sorted (A)

    l = 0
    r = 1
    prev = None

    while r < len(A) and A[l] == A[r]:
        prev = A[r]
        l += 2
        r += 2
        
    if A[l] == prev:
        return A[r]
    elif r + 2 == len(A):
        return A[r + 1]
    else:
        return A[l]
        
# Tests
# first should be 1, second should be 7
test_sets = [[10, 2, 2, 1, 0, 0, 10], [7, 3, 5, 4, 5, 3, 4]]

for x in test_sets:
    print(find_one(x))
    print(find_one_sort(x))
