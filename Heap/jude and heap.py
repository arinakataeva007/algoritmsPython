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

def calculate_max_cost(cakes_to_thief):
    heap = Heap()
    for v, w in cakes_to_thief:
        heap.add((-v/w, w))  

    total_value = 0
    total_weight = 0
    while total_weight < W and heap.min() != float('inf'):
        cake = heap.pop()
        if cake is None:  
            break
        v_w, w = cake
        v_w = -v_w  
        if total_weight + w <= W:
            total_weight += w
            total_value += v_w * w
        else:
            remaining_weight = W - total_weight
            total_value += v_w * remaining_weight
            break

    print(f"{total_value:.2f}")

n, W = map(int, input().split())
cakes_arr = [[int(x) for x in input().split()] for _ in range(n)]

calculate_max_cost(cakes_arr)