x = {"hello","world","world","x"} #kulaka
y = {"x","y"}


x.add("world")
x.add("World") #hash function use the check the duplicate

x.remove('hello')

z = x.union(y)

t = x-y

print(t)

print(z)

print(t)