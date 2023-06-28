#!/usr/bin/python3
''' class Node: definition of new type
'''


class Node():
    ''' Defines a node of a singly linked list
    '''

    def __init__(self, data, next_node=None):
        ''' Initialises current instance attributes
        '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        ''' Returns current node data
        '''
        return self.__data

    @data.setter
    def data(self, value):
        ''' Sets current node data
        '''
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        ''' Returns next node data
        '''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        ''' Sets next node data
        '''
        if isinstance(value, type(self)) or value is None:
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


''' class SinglyLinkedList: definition of new type
'''


class SinglyLinkedList:
    ''' Defines a singly linked list
    '''

    def __init__(self):
        ''' Initiates current singly linked list
        '''
        self.__head = []

    def sorted_insert(self, value):
        ''' Add new node
        '''
        node = Node(value, None)
        self.__head.append(node.data)

    def __str__(self):
        ''' Prints list
        '''
        str = ''
        self.__head = sorted(self.__head)
        for i in self.__head:
            str += '{}\n'.format(i)
        return str
