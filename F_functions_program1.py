# functions in python

def say_hi(name, age):
    print('Hi ' + name + ", you are " + str(age))
    print('exiting function sayhi')

say_hi("Mickey", 49)
say_hi("Lena", 19)
print("The end!")

def cube(num):
    return num*num*num

result = cube(4)
print(result)