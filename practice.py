# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as ptl
# class demo:
#     def __init__(self,size):
#         print('Enter elements: ')
#         self.list = []
#         for i in range(size):
#             a = int(input())
#             self.list.append(a)
#
#     def func(self):
#         a = np.array(self.list)
#         print(pd.Series(a))
#         ptl.plot(a)
#         ptl.show()
#
# obj = demo(int(input('Enter the size of the array: ')))
# obj.func()

import random as r
name = 'hendry'
class example:
    def match(self,size):
        students = []
        num = []
        for i in range(size):
            rand = r.randrange(10)
            students.append(['hendry',rand])
            num.append(rand)
        print(students)
        print(num)
        a = list(set(num))
        a.sort()
        students.sort()
        for i,j in students:
            if j == a[1]:
                print(j)



    def list(self):
        list1 = []
        list2 = []
        for i in range(10):
            list1.append([i])
            list2 += [i]
        print(f'{list1} And {list2}')

    def changefunc(self):
        print('This function is created from github')

        


obj = example()
#obj.match(int(input('Enter the size: ')))
#obj.list()
obj.changefunc()


