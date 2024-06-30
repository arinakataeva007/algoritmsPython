class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self._root is None:
            self._root = Node(data)
            return

        def _insert(node, data):
            if data < node.data:
                if node.left is None:
                    node.left = Node(data, node)
                else:
                    _insert(node.left, data)
            else:
                if node.right is None:
                    node.right = Node(data, node)
                else:
                    _insert(node.right, data)

        _insert(self._root, data)
    
    def build_from_array(self, array):

        def _build_from_array(array, left, right):
            if (left + 1 > right):
                return None
            if (left + 1 == right):
                return Node(array[left], None)

            middle = (left + right - 1) // 2
            node = Node(array[middle])
            node.left = _build_from_array(array, left, middle)
            node.right = _build_from_array(array, middle + 1, right)
            return node

        self.root = _build_from_array(array, 0, len(array))
    
    def print_tree(self):
        def _print_tree(node, prefix="", flag_on_last =False):
            if node is None:
                return

            print(prefix, end="")
            print("└───" if flag_on_last else "├───", end="")
            print(node.value)

            prefix += "    " if flag_on_last else "│   "

            if node.left is not None:
                _print_tree(node.left, prefix)

            if node.right is not None:
                _print_tree(node.right, prefix, True)

        print(self.root.value)
        _print_tree(self.root.left)
        _print_tree(self.root.right, "", True)

user_string = [int(x) for x in input().split(" ")]

tree = BinaryTree()
tree.build_from_array(user_string)

tree.print_tree()