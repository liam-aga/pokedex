"""
@Author Liam Aga | 11/8/22 10:31 pm |
Purpose: Use a binary search tree to replicate and store data just like a pokedex, and compare keys and nodes
to successfully operate the pokedex.

Menu and BST functions are activated within this executive class.
"""


from pokemon import Pokemon
from binarysearchtree import BinarySearchTree


class Executive:
    def __init__(self, file_name):
        self.pokemon_list = []
        self.file_name = file_name
        self.main_list = []
        self.my_tree = BinarySearchTree()

    def txt_clean(self):    # cleans the txt file to properly create pokemon objects
        file = open(self.file_name, "r")
        list1 = []

        for line in file:
            line_strip = line.strip(" ").strip("\n")
            line_split = line_strip.split()
            list1.append(line_split)
            self.main_list = list1

        file.close()

    def create_pokemon(self):  # instantiate all my pokemon here
        for x in self.main_list:
            my_pokemon = Pokemon(x[0], x[1], x[2])
            self.pokemon_list.append(my_pokemon)

    def load_pokemon(self):  # adds the existing pokemon from list into tree
        for x in self.pokemon_list:
            self.my_tree.add(x)

    def menu(self):
        while True:
            print(" POKEDEX  \n"
                  "1) Search[pokedex # id] \n"
                  "2) Add    \n"
                  "3) Print (pre, in, post order) \n"
                  "4) Quit "
                  )

            user_input = int(input(" Select from the menu: "))

            if user_input == 1:
                id_search = int(input("[SEARCH] Enter pokedex number id: "))  # takes in the ID to then search
                pokemon = self.my_tree.search(id_search)
                print(pokemon.american_name, pokemon.id, pokemon.jap_name)

            if user_input == 2:
                # asks for US name, JPN name, & ID #
                x, y, z = input("Enter US name, ID #, then Japanese Name: ").split()
                new_pokemon = Pokemon(x, int(y), z)
                self.my_tree.add(new_pokemon)
                print("Added!")

            if user_input == 3:
                # 3 diff orders for print
                print("1) Pre order: \n"
                      "2) In order \n"
                      "3) Post order ")
                _ = int(input("Enter a traversal option: "))
                if _ == 1:
                    self.my_tree.preorder(self.my_tree._root)
                elif _ == 2:
                    self.my_tree.inorder()
                elif _ == 3:
                    self.my_tree.postorder(self.my_tree._root)

            if user_input == 4:
                print("Exiting...")
                quit()

            elif user_input not in range(1, 5):
                print("Invalid number for function. Pick again.")
                continue
