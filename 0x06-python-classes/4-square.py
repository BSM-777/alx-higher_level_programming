#!/usr/bin/python3

class Square:
    def __init__(self, value ):
        if type(value) is int:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
        else:
            raise TypeError('size must be an integer')
        
    def area(self):
        return (self.__size) ** 2

    def size(self):
        return self.__size
    
    def __init__(self, size = 0):
        self.__size = size
