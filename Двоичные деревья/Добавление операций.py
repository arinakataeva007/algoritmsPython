class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add_value(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        def _add_value(node, value):
            if value < node.value:
                if node.left is None:
                    node.left = Node(value, node)
                else:
                    _add_value(node.left, value)
            else:
                if node.right is None:
                    node.right = Node(value, node)
                else:
                    _add_value(node.right, value)

        _add_value(self.root, value)
    
    def _delete_value(self, node: Node):
        if node is None:
            return

        if node.left is None or node.right is None:
            child = None
            if node.left is not None:
                child = node.left
            else:
                child = node.right

            if node == self.root:
                self.root = child
                if child is not None:
                    child.parent = None

            if node.parent.left == node:
                node.parent.left = child
                if child is not None:
                    child.parent = node.parent
            else:
                node.parent.right = child
                if child is not None:
                    child.parent = node.parent
        else:
            successor = node.right
            while successor.left is not None:
                successor = successor.left
            node.value = successor.value
            self._delete_value(successor)

    def delete_value(self, value: int):
        if self.root is None:
            return

        node_to_delete = self.find_node(value)
        if node_to_delete is None:
            return
        self._delete_value(node_to_delete)     
    
    def _find_node(self, node, value):
        if node is None:
            return None
        
        if node.value == value:
            return node
        if node.value > value:
            return self._find_node(node.left, value)
        else:
            return self._find_node(node.right, value)
    
    def find_node(self, value):
        return self._find_node(self.root, value)
    
    def find_next_node(self, value):
        def _find_next(node: Node):
            if node is None:
                return None
            if node.right is not None:
                next_node = node.right
                while next_node.left is not None:
                    next_node = next_node.left
                return next_node
            next_node = node
            while next_node.parent is not None and next_node.parent.right == next_node:
                next_node = next_node.parent

            return next_node.parent
        prev_node = self.find_node(value)
        return _find_next(prev_node)
    
    def build_from_array(self, array):
        def _build_from_array(left, right):
            if left + 1 == right:
                return Node(array[left], None)
            if left + 1 > right:
                return None

            middle = (left + right - 1) // 2
            node = Node(array[middle], None)
            node.right = _build_from_array(middle + 1, right)
            node.left = _build_from_array(left, middle)
            
            if node.left is not None:
                node.left.parent = node
            if node.right is not None:
                node.right.parent = node

            return node

        self.root = _build_from_array(0, len(array))
    
    def _print_tree(self,node: Node, prefix="", f=False):
        if node == None:
            return
        print(prefix, end="")
        print("└───" if f else "├───", end="")
        print(node.value)

        prefix += "    " if f else "│   "
        child_node = [node.left, node.right]
        child_node = [child for child in child_node if child is not None]

        for i, child in enumerate(child_node):
            is_last = i == len(child_node) - 1
            self._print_tree(child, prefix, is_last)

            
    def print_tree(self):
        print(self.root.value)
        self._print_tree(self.root.left)
        self._print_tree(self.root.right, "", True)

user_string = [int(x) for x in input().split()]
tree = BinaryTree()
tree.build_from_array(user_string)

while True:
    command = input().split() 
    
    if command[0] == "add":
        temp = [int(x) for x in command[1:]]
        for i in temp:
            tree.add_value(i)
        print("Ok")
    
    elif command[0] == "delete":
        tree.delete_value(int(command[1]))
        print("Ok")
        pass
    
    elif command[0] == "find":
        if tree.find_node(int(command[1])) is not None:
            print("Число нашлось")
        else:
            print("Число не нашлось")

    elif command[0] == "next":
        result = tree.find_next_node(int(command[1]))
        print(result.value if result is not None else "Следующего числа нет")
    
    elif command[0] == "print":
        tree.print_tree()
    else:
        break