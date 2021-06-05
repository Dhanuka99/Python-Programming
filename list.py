# basic data strucure---->List

from typing import Sized


x = [12,32,43,54,76,87]

y = [22,33,44,555,66]

z = [77,88]
z = x+y

print(x[0])

x.append(50) #list eke agata values danna
x.insert(2,500)# adala index ekata values danna

x.remove(12)# remove the elemant

x.pop(5)

print(12 in y) #12 y kiyana list eke thiyanawda blanna

print(not 12 in y) # 12 nedda y wala in ---> return bool