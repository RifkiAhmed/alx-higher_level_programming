#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    products = divide = 0
    for item in my_list:
        products += item[0] * item[1]
        divide += item[1]
    return products / divide
