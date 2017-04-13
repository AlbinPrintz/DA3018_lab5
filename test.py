from DA3018_lab5 import binarysearchtree as bst

credit = bst.BinarySearchTree()
credit.insert('DA3018', 7.5)
credit.insert('DA2004', 7.5)
credit.insert('DA2006', 3)
credit.insert('DA2009', 2)
credit.insert('DA2003', 1)
credit.insert('DA2022', 5)
credit.insert('DA2013', 6)
credit.insert('DA2002', 8)

print(credit)
n = credit.size()           # n = 3
hp = credit.find('DA3018')  # set hp to 7.5
credit.remove('DA2003')
m = credit.size()           # m = 2
print(n, hp, m)

try:
    credit.find('DA2005')
except KeyError:
    print('Got the expected error')
try:
    credit.remove('DA2005')
except KeyError:
    print('Got the expected error')

for course, hp in credit:
    print(course)
