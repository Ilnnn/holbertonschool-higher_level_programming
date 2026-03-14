#!/usr/bin/python3

class Square:
    def __init__(self, taille_constructeur_carre=0): ## constructeur
        self.size(taille_constructeur_carre)


    def area(self): 
        return self.__size ** 2
    
    def size(self): ## getter
        return self.__size

    def size(self, taille_setter_carre): ## setter
        if not isinstance(taille_setter_carre, int):
            raise TypeError ("size must be an integer")
        if taille_setter_carre < 0: 
            raise ValueError ("size must be >= 0")
        self.__size = taille_setter_carre
