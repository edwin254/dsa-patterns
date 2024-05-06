"""
"""

def insertion_sort(seq: list) -> list:
    index_size = len(seq)

    for i in range(1, index_size):
        for j in range(i):
            if seq[i] < seq[j]:
                seq[i], seq[j] = seq[j], seq[i]
    return seq



s = [5, 8, 2, 6, 9, 1, 0, 7]

# print(insertion_sort(s))

def lengthOfLongestSubstring(s: str) -> int:

    longest_sub=""
    length = 0
    cur_length=0
    
    if s=="":
        return 0

    for char in s:
        print("BB",longest_sub)
        if char not in longest_sub:
            longest_sub = longest_sub + char
            print("BB",longest_sub)
            cur_length += 1
            length = cur_length if  cur_length > length else length
        else:
            length = cur_length if  cur_length > length else length

            longest_sub=char
            cur_length = 1
    return length

print(lengthOfLongestSubstring(s=" "))