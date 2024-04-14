from collections import deque

size = int(input())

class LimitedSizeStack:
    def __init__(self, size):
        self.stack = deque()
        self.size = size
    def push(self, n):
        if self.size != 0:
            if len(self.stack) >= self.size:
                self.stack.popleft()
            self.stack.append(n)
        return "ok"
    def count(self):
        return len(self.stack)
    def pop(self):
        return self.stack.pop()

limited_stack = LimitedSizeStack(size)
protocol = []

while True:
    command = input().split()

    if command[0] == "push":
        protocol.append(limited_stack.push(command[1]))
    if command[0] == "pop":
        protocol.append(limited_stack.pop())
    if command[0] == "count":
        protocol.append(limited_stack.count())
    if command[0] == "exit":
        protocol.append("bye")
        break
print(*protocol, sep="\n")