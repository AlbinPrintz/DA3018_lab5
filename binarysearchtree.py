# Lab 5
class Node:
    def __init__(self, key: str, val: float):
        self._key = key
        self._val = val
        self._left = None
        self._right = None
        self._parent = None

    def __str__(self):
        return str(self._key) + ", " + str(self._val)

    def set_children(self, r, l):
        self._left = l
        self._right = r

    def set_left_child(self, l: object):
        self._left = l

    def set_right_child(self, r: object):
        self._right = r

    def set_parent(self, par):
        self._parent = par

    def data(self) -> tuple:
        return self._key, self._val

    def parent(self):
        return self._parent

    def left_child(self):
        return self._left

    def right_child(self):
        return self._right

    def set_val(self, new_val: float):
        self._val = new_val


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self._size = 0

    def __str__(self):
        return str(self.root)

    def __iter__(self):
        yield from self.next(self.root)

    def __getitem__(self, item: str) -> int:
        return self.find(item)

    def __setitem__(self, key: str, value: int):
        self.insert(key ,value)

    def next(self, v: Node):
        left = v.left_child()
        right = v.right_child()
        if v:
            if left:
                yield from self.next(left)
            yield v.data()
            if right:
                yield from self.next(right)

    def __tree_minimum(self):
        x = self.root
        while x.left_child():
            x = x.left_child()
        return x

    def insert(self, key: str, val: float):
        """
        Public interface method to insert a key and value to the search tree.
        """
        self._size += 1
        self.root = self.__insert(self.root, key, val)

    def __insert(self, v: Node, key: str, val: float) -> Node:
        """
        Internal method to recursively decide where to insert a new node.
        """
        if v:
            v_key, x = v.data()  # Ignoring x actually
            left = v.left_child()
            right = v.right_child()
            if key < v_key:  # If key less than v_key, go to left
                left = self.__insert(left, key, val)
                v.set_left_child(left)
                left.set_parent(v)

            elif key == v_key:  # If key equal v_key, update val
                v.set_val(val)
            else:  # If key greater than v_key, go to right
                right = self.__insert(right, key, val)
                v.set_right_child(right)
                right.set_parent(v)
            return v
        else:
            return Node(key, val)

    def find(self, key: str) -> float:
        """
        Public interface method to find a node with a specific key.
        """
        x, val = self.__find(self.root, key).data()  # Ignore x, we already have the key
        return val

    def __find(self, v: Node, key: str) -> Node:
        """
        Internal method to recursively look for a node. 
        """
        try:
            v_key, v_val = v.data()
            left = v.left_child()
            right = v.right_child()
        except:
            raise KeyError("Could not find a node with the desired key")
        if key == v_key:
            return v
        elif key < v_key:
            return self.__find(left, key)
        else:
            return self.__find(right, key)

    def __transplant(self, x: Node, y: Node):
        """
        Replace x and its subtree with y and its subtree.
        :param x: Node
        :param y: Node
        :return: None
        """
        xparent = x.parent()
        if not x:
            self.root = y
        elif x == xparent.left_child():
            xparent.set_left_child(y)
        elif x == xparent.right_child():
            xparent.set_right_child(y)
        if y:
            y.set_parent(xparent)
        self.__update_size()

    def remove(self, key: str):
        """
        Public method for removing node "key" from the tree.
        """
        v = self.__find(self.root, key)
        left = v.left_child()
        right = v.right_child()
        if left and right:  # Has two children
            y = self.__tree_minimum()
            if y.parent() != v:
                self.__transplant(y, y.right_child())
                y.set_right_child(v.right_child())
                y.right_child().set_parent(y)
            self.__transplant(v, y)
            y.set_left_child(v.left_child)
            y.left_child.set_parent(y)
        elif not left:  # Doesn't have left child
            self.__transplant(v, right)
        elif not right:  # Doesn't have right child
            self.__transplant(v, left)

    def size(self) -> int:
        return self._size

    def __update_size(self):
        self._size = self.__get_size(self.root, 0)

    def __get_size(self, v: Node, counter: int) -> int:
        i = counter
        if v:
            i += 1  # Count v
            left = v.left_child()
            right = v.right_child()
            if left:
                i = self.__get_size(left, i) # Count left tree
            if right:
                i = self.__get_size(right, i)  # Count right tree
        return i

def main():
    credit = BinarySearchTree()
    credit.insert('DA3018', 7.5)
    credit.insert('DA2004', 7.5)
    credit.insert('DA2003', 6)
    print(credit)
    n = credit.size()           # n = 3
    hp = credit.find('DA3018')  # set hp to 7.5
    credit.remove('DA2003')
    m = credit.size()           # m = 2
    print(n, hp, m)


if __name__ == '__main__':
    main()
