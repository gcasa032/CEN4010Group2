# # AUTHOR: Guillermo Casal

from classes.book import Book

class BookList:

    def __init__(self, booklist: list):

        self.booklist = booklist

    def returnxbooks(self, x: int):
        
        result = []

        for q in range(x):
            result.append(self.booklist.pop(0))

        return result


"""
    Feature: Retreive list of x books at a time where X is an integer

    Every search will return a booklist

    Booklist.returnxbooks will return a list containing x books. 
"""