# Task: determine if two strings are anagrams

# 1. Extra space
# Time O(n), space O(n)
def is_anagram (s1, s2):
    if len(s1) != len(s2):
        return False

    char_map = {}

    for char in s1:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1

    for char in s2:
        if char in char_map:
            char_map[char] -= 1

    for _,v in char_map.items():
        if v != 0:
            return False

    return True

# 2. Sort
# Time O(n log n), space O(1)
def is_anagram_sort (s1, s2):
    if len(s1) != len(s2):
        return False

    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

print(is_anagram('hello', 'hello'))
print(is_anagram_sort('hello', 'hello'))
