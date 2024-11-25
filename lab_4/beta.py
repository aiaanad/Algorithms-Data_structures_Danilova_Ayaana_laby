class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Tree:
    def __init__(self, arr):
        self.ans = []
        self.root = None
        for elem in arr:
            self.append(elem)
        self.show_tree(self.root)

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False

        node = Node(node)
        if value == node.data:
            return node, parent, True

        if value < node.data:
            return self.__find(node.left, node, value)

        if value > node.data:
            return self.__find(node.right, node, value)

        return node, parent, False

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        obj = Node(obj)
        p, s, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj

    def show_tree(self, node):
        if node is None:
            return

        self.show_tree(node.left)
        self.ans += [node.data]
        self.show_tree(node.right)

        return self.ans

    # def __del_leaf(self, s, p):
    #     if p.left == s:
    #         p.left = None
    #     elif p.right == s:
    #         p.right = None
    #
    # def del_node(self, key):
    #     s, p, fl_find = self.__find(self.root, None, key)
    #
    #     if not fl_find:
    #         return None
    #
    #     if s.left is None and s.right is None:
    #         self.__del_leaf(s, p)
    #
    #     if


Tree([1, 3, 4, 2, 5])


