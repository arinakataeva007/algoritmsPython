import heapq
from collections import Counter

class Node:
    def __init__(self, left_child, right_child):
        self.left_child = left_child
        self.right_child = right_child
    def bypass(self, char_codes, current_code):
        self.left_child.bypass(char_codes, current_code + "0")
        self.right_child.bypass(char_codes, current_code + "1")

class Leaf:
    def __init__(self, ch):
        self.ch = ch
    def bypass(self, char_codes, current_code):
        char_codes[self.ch] = current_code or "0"

def calculate_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def huffman_code(s):
    frequency = calculate_frequency(s)

    heapqq = []
    for char, freq in frequency.items():
        heapqq.append((freq, len(heapqq), Leaf(char)))
    heapq.heapify(heapqq)

    count = len(heapqq)
    while len(heapqq) > 1:
        freq1, _count1, left = heapq.heappop(heapqq)
        freq2, _count2, right = heapq.heappop(heapqq)
        heapq.heappush(heapqq, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if heapqq:
        [(_freq, _count, root)] = heapqq
        root.bypass(code, "")
    return code

str = input()
codes = huffman_code(str)
encoded_length = sum(len(codes[char]) for char in str)
print(encoded_length)