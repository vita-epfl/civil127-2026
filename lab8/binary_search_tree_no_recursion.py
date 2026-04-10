# Binary search tree implementation without using recursion
#
# Is this version simpler/easier to read than the recursive version?


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
        c = self.root
        if c is None:
            # Case where the tree was empty
            self.root = Node(value)
            return

        # Notice how the type of c from here onwards is no longer Node | None
        # and it's just Node. This is called type narrowing.

        while True:
            if value < c.getValue():
                next_c = c.getLeft()
                if next_c is None:
                    # Value goes in a new left child
                    c.setLeft(Node(value))
                    return
                c = next_c
            elif value > c.getValue():
                next_c = c.getRight()
                if next_c is None:
                    # Value goes in a new right child
                    c.setRight(Node(value))
                    return
                c = next_c
            else:
                # value == c.getValue() is implied
                # We are done, the value was already in the tree
                return

    def contains(self, value: int) -> bool:
        c = self.root
        while c is not None:
            if value < c.getValue():
                c = c.getLeft()
            elif value > c.getValue():
                c = c.getRight()
            else:
                # value == c.getValue() is implied
                return True
        return False

    def remove(self, value: int) -> None:
        # Remove is tricky since there are a few cases, including moving nodes around.
        previous = self.root
        if previous is None:
            # the tree is empty, we have nothing to do
            return
        if value == previous.getValue():
            # Remove the root node
            left = previous.getLeft()
            right = previous.getRight()
            if left is None:
                # There's no left node, promote the right subtree to root
                self.root = right
                return
            if left.getRight() is None:
                # Promote the left node and give it a right subtree
                self.root = left
                left.setRight(right)
                return
            # Remove largest value in the left subtree and promote it to root
            promote = self.remove_largest(left)
            promote.setLeft(left)
            promote.setRight(right)
            self.root = promote
            return

        while True:
            # Search for value by keeping track of the previous node
            # so that we can update the nodes correctly
            if value < previous.getValue():
                c = previous.getLeft()
                if c is None:
                    # the node was not found
                    return
                if value == c.getValue():
                    # remove c and update previous.left
                    left = c.getLeft()
                    right = c.getRight()
                    if left is None:
                        # There's no further left node, promote the right subtree
                        previous.setLeft(right)
                        return
                    if left.getRight() is None:
                        # Promote the left node and give it a right subtree
                        previous.setLeft(left)
                        left.setRight(right)
                        return
                    # Remove largest value in the left subtree and promote it
                    promote = self.remove_largest(left)
                    promote.setLeft(left)
                    promote.setRight(right)
                    previous.setLeft(promote)
                    return
                previous = c
                continue
            elif value > previous.getValue():
                c = previous.getRight()
                if c is None:
                    # the node was not found
                    return
                if value == c.getValue():
                    # remove c and update previous.right
                    left = c.getLeft()
                    right = c.getRight()

                    if left is None:
                        # There's no further left node, promote the right subtree
                        previous.setRight(right)
                        return
                    if left.getRight() is None:
                        # Promote the left node and give it a right subtree
                        previous.setRight(left)
                        left.setRight(right)
                        return
                    # Remove largest value in the left subtree and promote it
                    promote = self.remove_largest(left)
                    promote.setLeft(left)
                    promote.setRight(right)
                    previous.setRight(promote)
                    return
                previous = c
                continue

            # if we get here, that means our code is seriously broken. We failed to
            # both find and not find the value.
            assert False

    def remove_largest(self, node: Node) -> Node:
        """Removes the right most leaf and return it"""

        c = node
        while True:
            right = c.getRight()
            assert right is not None
            if right.getRight() is None:
                c.setRight(None)
                return right
            c = right

    def smallest(self) -> int:
        # Compare the implementation of smallest with largest, they are two different
        # approaches to have code which type checks correctly.
        c = self.root
        if c is None:
            raise IndexError("tree is empty")
        while True:
            next_c = c.getLeft()
            if next_c is None:
                return c.getValue()
            c = next_c

    def largest(self) -> int:
        c = self.root
        if c is None:
            raise IndexError("tree is empty")

        # if we don't use a `while True` loop, we have to deal with a potentially None value for c
        while c is not None and c.getRight() is not None:
            c = c.getRight()

        # And the type system isn't smart enough to know that c can't be None here so we
        # need to deal with a potential None again.
        assert c is not None
        return c.getValue()


class Node:
    def __init__(self, value: int):
        self._value = value
        self.left = None
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
