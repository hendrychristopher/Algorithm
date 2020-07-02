from array import array
from numpy import *


def selectivesort(list):
    for i in range(len(list)-1):
        min = i
        for j in range(i,len(list)):
            if list[min] > list[j]:
                min = j
        temp = list[i]
        list[i] = list[min]
        list[min] = temp

def bubblesort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp


def linearsearch(list):
    value = int(input('Enter the number you want to search: '))
    lowerbound = 0
    upperbound = len(list)-1

    while lowerbound <= upperbound:
        mid = (lowerbound+upperbound) // 2
        if list[mid] == value:
            globals()['position'] = mid + 1
            return True
        elif value > list[mid]:
            lowerbound = mid + 1
        else:
            upperbound = mid - 1
    return False
position = -1




list = [10,3,1,2,9,12,6,7,55,21,31,66,92,5]
linearlist = [2,3,5,6,7,9,11,23,45,55,67,76,89,99,200]

#selectivesort(list)
#print(list)

#bubblesort(list)
#print(list)


# if linearsearch(linearlist):
#     print(f'found at {position}')
# else:
#     print('not found')





a = array([[1,2,3,4,1,5,0,6],[1,2,3,4,5,5,6,1]])
b = array([[2,4,1,9,1,6,3,1],[8,7,3,1,9,2,6,5]])
c = a*b
print(c)
m = asmatrix(a)
print(m)

d = zeros(10)
e = ones(10)
print(d,' ',e)








#vals = int(input('Enter the size of the value: '))
# a = 0
# b = 1
# c = a + b
# res = [a,b,c]
# for i in range(vals):
#     a = b
#     b = c
#     c = a + b
#     res.append(c)
# print(res)




# data = open('MyPersonalInfo.txt','w')
# a = int(input('how many words u want to write'))
# print('now you can enter your words')
# s = ''
# for i in range(a):
#     s += input()
# print(s)


# a = open('MyPersonalInfo.txt','w')
# for i in range(10):
#     a.write(input())
