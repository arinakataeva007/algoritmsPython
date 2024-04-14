from collections import deque

N = int(input())

class KnightQueue:
    def __init__(self):
        self.queue = deque()
    def push_prince(self, el):
        self.queue.appendleft(el)
    def push_simple_knight(self, el):
        self.queue.append(el)
    def push_nobleman(self, el):
        if len(self.queue) % 2 != 0:
            self.queue.insert((len(self.queue) + 1) // 2, el)
        else:
            self.queue.insert((len(self.queue)) // 2, el)
    def pop(self):
        return self.queue.popleft()

knightQueue = KnightQueue()
result = []
for _ in range(N):
    request = input().split()
    if(request[0] == "+"):
        knightQueue.push_simple_knight(request[1])
    elif(request[0] == "*"):
        knightQueue.push_nobleman(request[1])
    elif(request[0] == "!"):
        knightQueue.push_prince(request[1])
    else:
        result.append(knightQueue.pop())
print(*result, sep='\n')