from collections import deque

class PriorityQueue:
    def __init__(self):
        self.dictWithQueue = {}

    def push(self, numb_i, priority_k):
        if priority_k in self.dictWithQueue:
            self.dictWithQueue[priority_k].append(numb_i)
        else:
            self.dictWithQueue[priority_k] = deque([numb_i])

    def pop_top(self):
        if self.size() == 0:
            return "-1"
        
        maxK = max(self.dictWithQueue.keys())
        numb_i = self.dictWithQueue[maxK].popleft()

        if len(self.dictWithQueue[maxK]) == 0:
            del self.dictWithQueue[maxK]
        return numb_i
    
    def pop(self, priority_k):
        if priority_k in self.dictWithQueue and len(self.dictWithQueue[priority_k]) > 0:
            numb_i = self.dictWithQueue[priority_k].popleft()

            if len(self.dictWithQueue[priority_k]) == 0:
                del self.dictWithQueue[priority_k]
            
            return numb_i
        return "-1"
    
    def size(self):
        count = 0
        for _ in self.dictWithQueue.values():
            count += len(_)
        return count
    
    def pop_all(self, priority_k):
        if priority_k in self.dictWithQueue:
            numbers_person = self.dictWithQueue[priority_k]
            self.dictWithQueue.pop(priority_k)
            return " ".join(str(numbers_person) for numbers_person in numbers_person)
        return -1
    
    def clear(self):
        self.dictWithQueue = {}

compensation_queue = PriorityQueue()
result = []

while True:
    command = input().split()

    if command[0] == "push":
        compensation_queue.push(int(command[1]), int(command[2]))
        result.append("ok")
    elif command[0] == "pop":
        if command[1] == "top":
            result.append(compensation_queue.pop_top())
        else:
            result.append(compensation_queue.pop(int(command[1])))
    elif command[0] == "popall":
        result.append(compensation_queue.pop_all(int(command[1])))
    elif command[0] == "size":
        result.append(compensation_queue.size())
    elif command[0] == "clear":
        compensation_queue.clear()
        result.append("ok")
    elif command[0] == "exit":
        result.append("bye")
        break
print(*result, sep='\n')