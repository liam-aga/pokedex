"""
@Author Liam Aga | 11/8/22 10:31 pm |
Purpose: Use a binary search tree to replicate and store data just like a pokedex, and compare keys and nodes
to successfully operate the pokedex.

This driver files runs the entire program with executive class.
"""

from Executive import Executive


def main():
    file = str(input("Type in file name: "))
    my_exec = Executive(file)
    my_exec.txt_clean()
    my_exec.create_pokemon()
    my_exec.load_pokemon()  # instantiate pokemon into tree

    my_exec.menu()


if __name__ == "__main__":
    main()
