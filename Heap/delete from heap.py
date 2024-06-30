class Heap:
    def __init__(self):
        self.heap = []
    
    def add(self, n):
        self.heap.append(n)
        self._shift_up(len(self.heap) - 1)
    
    def min(self):
        if self.heap:
            return self.heap[0]
        return None
    
    def size(self):
        return(len(self.heap))
    
    def _shift_up(self, idx):
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.heap[parent_idx] <= self.heap[idx]:
                break
            self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
            idx = parent_idx
    
    def _shift_down(self, idx):
        min_idx = idx
        left_node_idx = idx * 2 + 1 
        right_node_idx = idx * 2 + 2 

        if left_node_idx < len(self.heap):
            if self.heap[left_node_idx] < self.heap[min_idx]:
                min_idx = left_node_idx

        if right_node_idx < len(self.heap):
            if self.heap[right_node_idx] < self.heap[min_idx]:
                min_idx = right_node_idx

        if min_idx != idx:
            self.heap[min_idx], self.heap[idx] = self.heap[idx], self.heap[min_idx]
            self._shift_down(min_idx)

    
    def pop(self):
        if self.size():
            delete_value = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self._shift_down(0)
            return delete_value
        return None
    
    def structure(self):
        if (self.size() == 0):
            print("---STRUCTURE START---")
            print("---STRUCTURE END---")
            return
        print("---STRUCTURE START---")
        levels_size = [0] * self.size()
        for i in range(1, self.size()):
            parent_index = (i - 1) // 2
            levels_size[i] = levels_size[parent_index] + 1
        depths = {}
        for i, depth in enumerate(levels_size):
            if depth not in depths:
                depths[depth] = []
            depths[depth].append(self.heap[i])
        for d in sorted(depths.keys()):
            print(' '.join(map(str, depths[d])))
        print("---STRUCTURE END---")

heap = Heap()
while True:
    commands = input().split()
    if commands[0] == "add":
        n = int(commands[1])
        heap.add(n)
        print("ok")
    elif commands[0] == "min":
        print(heap.min())
    elif commands[0] == "size":
       print(heap.size())
    elif commands[0] == "pop":
        print(heap.pop())
    elif commands[0] == "structure":
        heap.structure()
    else:
        print("bye")
        break