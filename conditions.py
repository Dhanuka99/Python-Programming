#conditions

x = 10

if x>=150:
    print("Your selected..")
else:
    print("your not selected..")


marks = 50

if marks>=75 and marks<=100:
    print("passe")
else:
    print("Fail")


# mark = 45
# result = ""

# if mark>= 0 and mark<35:
#     print("S")
# else:
#     if mark>=35 and mark<55:
#         print("C")
#     else:
#         if mark<=55 and mark<65:
#             print("B")
#         else:
#             if mark<65 and mark<= 100:
#                 print("A")
#             else:
#                 print("Invalied Number")



# mark = 74

# if mark<=0 or mark>100:
#     print("Invalied")
#     exit() 
# elif mark>=0 and mark <35:
#     print("W")
# elif  mark <55:
#     print("S")
# elif  mark<65:
#     print("C")
# elif  mark <75:
#     print("B")
# elif  mark  <=100:
#     print("A")
# else:
#     print("Invalied number")


height = 176


# if height > 150:
#     job = "Security"
# else:
#     job = "Labor"
# print(job)


#Ternary Operator
job = "Security" if height > 150 else "Labor"
print(job)

age = 21
print("Student" if age < 20 else "Not Student")
