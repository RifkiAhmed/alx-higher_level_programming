#!/usr/bin/python3
''' class Node: definition of new type
'''


class Node:
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
        if value is not None or not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


''' class SinglyLinkedList: definition of new type
'''


class SinglyLinkedList:
    ''' Defines a singly linked list
    '''

    def __init__(self):
        ''' Initiates current singly linked list
        '''
        self.__head = None

    def sorted_insert(self, value):
        ''' Add new node
        '''
        self.__head = Node(value, None)
