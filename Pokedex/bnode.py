"""
@Author Liam Aga | 11/8/22 10:31 pm |
Purpose: Use a binary search tree to replicate and store data just like a pokedex, and compare keys and nodes
to successfully operate the pokedex.

The Bnode class
"""

class Bnode:
    def __init__(self, entry):
        self.entry = entry
        self.left = None
        self.right = None
