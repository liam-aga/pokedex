"""
@Author Liam Aga | 11/8/22 10:31 pm |
Purpose: Use a binary search tree to replicate and store data just like a pokedex, and compare keys and nodes
to successfully operate the pokedex.

The Pokemon class holds the information of names and id to store into Bnodes then add to BinarySearchTree
"""

class Pokemon:
    def __init__(self, american_name, id_num, jap_name):
        self.american_name = american_name
        self.id = int(id_num)
        self.jap_name = jap_name
    # if new value < then cur node: add to left
    # if new value > than cur node: add to the right

    def __gt__(self, other):   # Operator overloading here to compare keys(in int) within the Tree
        if self.id > other:
            return True
        else:
            return False

    # self.left or right = Node(entry)

    def __eq__(self, other):
        if self.id == other:
            return True
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, int):  # Utilizing isInstance() here

            if int(self.id) < other:
                return True
            else:
                return False

        elif isinstance(other, Pokemon):
            if int(self.id) < other.id:
                return True
            else:
                return False

