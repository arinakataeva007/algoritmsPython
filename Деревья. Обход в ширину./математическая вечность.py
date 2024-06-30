from collections import deque

source_number = input()
target_number = input()
ndigits = len(source_number)
source_number = int(source_number)
target_number = int(target_number)

base = 10 ** (ndigits - 1)
def addOne(number):
    return (number + base) if (number // base != 9) else number
def minusOne(number):
    return (number - 1) if (number % 10 != 1) else number
def shiftLeft(n):
    return (n % base) * 10 + n // base
def shiftRight(n):
    return (n % 10) * base + n // 10
operations = [addOne, minusOne, shiftRight, shiftLeft]


used_numbers = set()
prev_number = dict()

queue = deque()
queue.append(source_number)
used_numbers.add(source_number)
prev_number[source_number] = -1
while queue:
    number = queue.popleft()
    if number == target_number:
        break
    for op in operations:
        next_number = op(number)
        if next_number not in used_numbers:
            used_numbers.add(next_number)
            prev_number[next_number] = number
            queue.append(next_number)

def printPath(number):
    if (number == -1):
        return
    printPath(prev_number[number])
    print(number)
printPath(target_number)
