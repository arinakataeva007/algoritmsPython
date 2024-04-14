from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()
    def push(self, element):
        self.queue.append(element)
        return "ok"
    def pop(self):
        return self.queue.popleft()
    def front(self):
        return self.queue[0]
    def view(self):
        return ', '.join(map(str, self.queue))
    def clear(self):
        self.queue.clear()
        return "ok"
    def size(self):
        return len(self.queue)
result = []
myQueue = Queue()
while True:
    command = input().split()
    if (command[0] == "push"):
        myQueue.push(int(command[1]))
        result.append("ok")
    elif (command[0] == "pop"):
        result.append(myQueue.pop())
    elif (command[0] == "front"):
        result.append(myQueue.front())
    elif (command[0] == "size"):
        result.append(myQueue.size())
    elif (command[0] == "view"):
        result.append(myQueue.view())
    elif (command[0] == "clear"):
        result.append(myQueue.clear())
    else:
        result.append("bye")
        break
print(*result, sep="\n")