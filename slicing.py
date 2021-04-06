x = ['a','b','c','d']

y = []
l = []
y.append(x[0])
y.append(x[1])

print(x)
print(y)

print("---------------")

#slicing ===> axtract the data from list

z = x[2:4]
t = x[:2]
u = x[-1] #access the last element
r= x[:-1] #0 idala -1 wenakan..ekedi last elemant eka ganne ne   [starting index: ending index]

message = "My name is Praneeth"
msg = message[-8:] + " is " + str(message[:7]).lower() + "."
print(msg)


print(z)
print(t)
print(u)
print(r)
print(len(x))

#Summary
# list
x = [1,2,3,4]
# Dictionary
y = {"1":1}
#set
z = {"1","2"}
#tuple
a = {"1",12,True}

# String ekak kiyanneath charachtor set ekak
b = "Hello World"
