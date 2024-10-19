"""
@Author Liam Aga | 11/8/22 10:31 pm
Purpose: Use a binary search tree to replicate and store data just like a pokedex, and compare keys and nodes
to successfully operate the pokedex.

This BST is a data structure to hold all pokemon objects and sort information within itself
"""

from bnode import Bnode


class BinarySearchTree:
    def __init__(self):
        self._root = None

    def search(self, key):
        return self.rec_search(key, self._root)

    def rec_search(self, key, cur_node):
        if cur_node is None:
            print("not found")
            raise ValueError("Root was none")
        if cur_node.entry == key:
            print("found!")
            return cur_node.entry
        if cur_node.entry < key:  # go right
            return self.rec_search(key, cur_node.right)
        if cur_node.entry > key:
            return self.rec_search(key, cur_node.left)

    def rec_add(self, new_node, cur_node):  # stop duplicates/ throw exception (runtime)
        if cur_node is None:
            return new_node
        else:
            if cur_node.entry == new_node.entry:
                raise RuntimeError  # Duplicate Error

            if new_node.entry < cur_node.entry:  # if new value less, add to the left
                cur_node.left = self.rec_add(new_node, cur_node.left)

            if new_node.entry > cur_node.entry:
                cur_node.right = self.rec_add(new_node, cur_node.right)

        return cur_node

    def add(self, new_node):
        new_node = Bnode(new_node)
        self._root = self.rec_add(new_node, self._root)

    """
    def inorder(self, key, cur_node):

        if cur_node.left is not None:
            cur_node.left.inorder(key)
        if key is not None:
            key.append(key)
        if cur_node.right is not None:
            cur_node.right.inorder(key)
        return key

    """

    def inorder(self):  # left, visit root, then right
        temp = self._root
        my_list = []
        while temp is not None or not len(my_list) == 0:
            if temp is not None:
                my_list.append(temp)
                temp = temp.left
            else:
                temp = my_list.pop()
                yo = Bnode(temp)
                hi = yo.entry
                print(f'American Name: {hi.entry.american_name} | '
                      f'Japanese Name: {hi.entry.jap_name} ')
                temp = temp.right

    def preorder(self, root):  # visit, left, right

        if root:
            # First print the data of node
            print(f" American Name: {root.entry.american_name}, Japanese Name: {root.entry.jap_name}")

            self.preorder(root.left)

            self.preorder(root.right)

    def postorder(self, root):  # left, right, visit

        if root:
            # First print the data of node

            self.preorder(root.left)

            self.preorder(root.right)

            print(f" American Name: {root.entry.american_name}, Japanese Name: {root.entry.jap_name}")
