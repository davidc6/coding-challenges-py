# Task: Run-length encoding (RLE) compression offers a fast way to do efficient on-the-fly compression and decompression of strings

# 1. Encode a string
def run_length_encoding (s):
    prev = None
    count = 0
    list = []
    result = ''

    for char in s:
        if (prev != char):
            if prev != None:
                list.append({ prev: count })
            prev = char
            count = 1
        else:
            count += 1

    list.append({ prev: count })

    for entity in list:
        for k,v in entity.items():
            result = result + k + str(v)
        
    return result
    
# 2. Decode a string
# TODO

print(run_length_encoding ("aaaabcccaa"))
