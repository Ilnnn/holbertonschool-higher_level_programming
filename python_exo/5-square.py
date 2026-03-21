#!/usr/bin/python3

class Square:
    def __init__(self, taille_constructeur_carre=0): ## constructeur
        self.size = taille_constructeur_carre


    def area(self): 
        return self.__size ** 2
    
    @property
    def size(self): ## getter
        return self.__size

    @size.setter
    def size(self, taille_setter_carre): ## setter
        print("setter appeler avec taille:",taille_setter_carre) 
        if not isinstance(taille_setter_carre, int):
            raise TypeError ("size must be an integer")
        if taille_setter_carre < 0: 
            raise ValueError ("size must be >= 0")
        self.__size = taille_setter_carre

    def my_print(self):
        c = self.__size
        for i in range(c):
            for col in range(c):
                print('#', end='')
            print()
        if c == 0:
            print()