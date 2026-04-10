import unittest

# from lab8.binary_search_tree_no_recursion import BinarySearchTree
from lab8.binary_search_tree_with_recursion import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):
    def tree(self) -> BinarySearchTree:
        bst = BinarySearchTree()
        self.assertTrue(bst.is_valid_bst())
        bst.add(8)
        self.assertTrue(bst.is_valid_bst())
        bst.add(10)
        self.assertTrue(bst.is_valid_bst())
        bst.add(14)
        self.assertTrue(bst.is_valid_bst())
        bst.add(13)
        self.assertTrue(bst.is_valid_bst())
        bst.add(3)
        self.assertTrue(bst.is_valid_bst())
        bst.add(6)
        self.assertTrue(bst.is_valid_bst())
        bst.add(7)
        self.assertTrue(bst.is_valid_bst())
        bst.add(4)
        self.assertTrue(bst.is_valid_bst())
        bst.add(1)
        self.assertTrue(bst.is_valid_bst())
        return bst

    def testAdd(self):
        bst = self.tree()
        self.assertEqual(bst.serialize(), "<<<1>:3:<<4>:6:<7>>>:8:<10:<<13>:14>>>")

    def testContains(self):
        bst = self.tree()
        values = (1, 3, 4, 6, 7, 8, 10, 13, 14)
        for i in range(0, 15):
            if i in values:
                self.assertTrue(bst.contains(i))
            else:
                self.assertFalse(bst.contains(i))

    def testRemove(self):
        # Remove has a lot of different cases, so we need to write extensive tests

        bst = self.tree()
        bst.remove(1)
        self.assertEqual(bst.serialize(), "<<3:<<4>:6:<7>>>:8:<10:<<13>:14>>>")
        self.assertFalse(bst.contains(1))
        self.assertTrue(bst.is_valid_bst())

        bst = self.tree()
        bst.remove(10)
        self.assertEqual(bst.serialize(), "<<<1>:3:<<4>:6:<7>>>:8:<<13>:14>>")
        self.assertFalse(bst.contains(10))
        self.assertTrue(bst.is_valid_bst())

        bst = self.tree()
        bst.remove(14)
        self.assertEqual(bst.serialize(), "<<<1>:3:<<4>:6:<7>>>:8:<10:<13>>>")
        self.assertFalse(bst.contains(14))
        self.assertTrue(bst.is_valid_bst())

        bst = self.tree()
        bst.remove(8)
        self.assertEqual(bst.serialize(), "<<<1>:3:<<4>:6>>:7:<10:<<13>:14>>>")
        self.assertFalse(bst.contains(8))
        self.assertTrue(bst.is_valid_bst())

        bst = self.tree()
        bst.remove(5)
        self.assertEqual(bst.serialize(), "<<<1>:3:<<4>:6:<7>>>:8:<10:<<13>:14>>>")
        bst.remove(0)
        self.assertEqual(bst.serialize(), "<<<1>:3:<<4>:6:<7>>>:8:<10:<<13>:14>>>")
        self.assertTrue(bst.is_valid_bst())

        bst = BinarySearchTree()
        bst.add(8)
        bst.add(10)
        bst.add(14)
        bst.add(13)
        bst.remove(8)
        self.assertEqual(bst.serialize(), "<10:<<13>:14>>")
        self.assertFalse(bst.contains(8))
        self.assertTrue(bst.is_valid_bst())

        bst = BinarySearchTree()
        bst.add(8)
        bst.add(10)
        bst.add(14)
        bst.add(13)
        bst.add(3)
        bst.remove(8)
        self.assertEqual(bst.serialize(), "<3:<10:<<13>:14>>>")
        self.assertFalse(bst.contains(8))
        self.assertTrue(bst.is_valid_bst())

        bst = BinarySearchTree()
        bst.add(8)
        bst.add(3)
        bst.add(1)
        bst.add(10)
        bst.remove(3)
        self.assertEqual(bst.serialize(), "<<1>:8:<10>>")
        self.assertFalse(bst.contains(3))
        self.assertTrue(bst.is_valid_bst())

        bst = BinarySearchTree()
        bst.add(8)
        bst.add(12)
        bst.add(9)
        bst.add(10)
        bst.add(14)
        bst.remove(12)
        self.assertEqual(bst.serialize(), "<8:<<9>:10:<14>>>")
        self.assertFalse(bst.contains(12))
        self.assertTrue(bst.is_valid_bst())

        bst = BinarySearchTree()
        bst.remove(1)
        self.assertEqual(bst.serialize(), "<>")
        self.assertTrue(bst.is_valid_bst())

    def testSmallest(self):
        bst = self.tree()
        self.assertTrue(bst.smallest(), 1)

        bst.remove(1)
        self.assertTrue(bst.smallest(), 3)
        self.assertTrue(bst.is_valid_bst())

    def testLargest(self):
        bst = self.tree()
        self.assertTrue(bst.largest(), 14)

        bst.remove(14)
        self.assertTrue(bst.smallest(), 13)
        self.assertTrue(bst.is_valid_bst())


if __name__ == "__main__":
    unittest.main()
