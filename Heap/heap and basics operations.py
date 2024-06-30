class Heap:
    def __init__(self):
        self.heap = []
    
    def add(self, n):
        self.heap.append(n)
        self._pop_up(len(self.heap) - 1)
    
    def min(self):
        if self.heap:
            return self.heap[0]
        return None
    
    def size(self):
        return(len(self.heap))
    
    def _pop_up(self, idx):
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.heap[parent_idx] <= self.heap[idx]:
                break
            self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
            idx = parent_idx

heap = Heap()
result = []
while True:
    commands = input().split()
    if commands[0] == "add":
        n = int(commands[1])
        heap.add(n)
        result.append("ok")
    elif commands[0] == "min":
        result.append(heap.min())
    elif commands[0] == "size":
        result.append(heap.size())
    else:
        result.append("bye")
        break
print(*result, sep='\n')