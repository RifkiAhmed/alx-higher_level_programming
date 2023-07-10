#!/usr/bin/python3
''' Module defines a class Mylist that inherits from list class
'''


class MyList(list):
    ''' Represents Mylist class inherits from list class
    '''

    def print_sorted(self):
        ''' Prints an ascending sorted list
        '''
        mylist = self.copy()
        mylist.sort()
        print(mylist)
