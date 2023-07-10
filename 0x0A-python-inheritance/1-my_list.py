#!/usr/bin/python3
''' Module defines a class Mylist that inherits from list class
'''


class MyList(list):
    ''' Represents Mylist class inherits from list class
    '''

    def print_sorted(self):
        ''' Prints an ascending sorted list
        '''
        my_list = self.copy()
        my_list.sort()
        print(my_list)
