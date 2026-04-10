# Binary search tree implementation with recursion.
#
# Is this version simpler/easier to read than the non-recursive version? It seems
# shorter. Most of the logic moves to the Node class


class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Node | None = None

    def serialize(self) -> str:
        """
        Useful for debugging and unittesting!
        """
        if self.root is None:
            return "<>"
        return self.root.serialize()

    def is_valid_bst(self) -> bool:
        """
        Helper method to check that the tree is a valid bst
        """
        if self.root is not None:
            return self.root.is_valid_bst(None, None)
        return True

    def add(self, value: int) -> None:
        if self.root is None:
            # Case where the tree was empty
            self.root = Node(value)
        else:
            # Notice how the type of self.root from here onwards is no longer Node | None
            # and it's just Node. This is called type narrowing.
            self.root.add(value)

    def contains(self, value: int) -> bool:
        if self.root is None:
            # Empty tree doesn't contain any values
            return False
        return self.root.contains(value)

    def remove(self, value: int) -> None:
        if self.root is not None:
            self.root = self.root.remove(value)

    def smallest(self) -> int:
        if self.root is None:
            raise IndexError("tree is empty")
        return self.root.smallest()

    def largest(self) -> int:
        if self.root is None:
            raise IndexError("tree is empty")
        return self.root.largest()


class Node:
    def __init__(self, value: int):
        self._value = value
        self.left: Node | None = None
        self.right = None

    def serialize(self) -> str:
        r = "<"
        if self.left is not None:
            r += self.left.serialize() + ":"
        r += str(self._value)
        if self.right is not None:
            r += ":" + self.right.serialize()
        r += ">"
        return r

    def is_valid_bst(self, min: int | None, max: int | None) -> bool:
        if min is not None and self._value <= min:
            return False
        if max is not None and self._value >= max:
            return False

        ok = True
        if self.left is not None:
            ok = ok and self.left.is_valid_bst(min, self._value)
        if self.right is not None:
            ok = ok and self.right.is_valid_bst(self._value, max)
        return ok

    def getValue(self) -> int:
        return self._value

    def setLeft(self, child: Node | None) -> None:
        self.left = child

    def getLeft(self) -> Node | None:
        return self.left

    def setRight(self, child: Node | None) -> None:
        self.right = child

    def getRight(self) -> Node | None:
        return self.right

    def add(self, value: int) -> None:
        if value == self._value:
            # we already have this value, no need to do anything
            return
        elif value < self._value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.add(value)
        elif value > self._value:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.add(value)

    def contains(self, value: int) -> bool:
        if value < self._value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif value > self._value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            # value == self._value is implied
            return True

    def remove(self, value: int) -> Node | None:
        """
        Finds the node with value and removes it. Returns the node which gets
        promoted in its place.
        """
        if value < self._value:
            if self.left is not None:
                self.left = self.left.remove(value)
            return self
        elif value > self._value:
            if self.right is not None:
                self.right = self.right.remove(value)
            return self
        else:
            # value == self._value is implied
            if self.left is None:
                # There's no left subtree, so the right subtree is promoted
                return self.right
            promote = self.left.remove_largest(self)
            promote.setLeft(self.left)
            promote.setRight(self.right)
            return promote

    def remove_largest(self, parent: Node, first: bool = True) -> Node:
        """
        Find the largest value (node without a right child) and removes it from its parent.
        The first time remove_largest is called, we remove parent.left but as the code recurses,
        we remove parent.right (hence the first bool flag)
        """
        if self.right is not None:
            return self.right.remove_largest(self, False)
        if first:
            parent.left = None
        else:
            parent.right = None
        return self

    def smallest(self) -> int:
        if self.left is None:
            return self._value
        return self.left.smallest()

    def largest(self) -> int:
        if self.right is None:
            return self._value
        return self.right.largest()
