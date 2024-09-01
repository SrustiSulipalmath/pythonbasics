def say_hi():
   print("hello user")                    #intended

print("top")
say_hi()
print("bottom")

#parameter a piece of information that we give to function

def sayhi(name,age):
   print("hello "+name+" you are "+age)       #str(age)

sayhi("srusti","22")
sayhi("gsm","22")

def cube(num):
    return num*num*num  #break

print(cube(3))

result = cube(4)
print(result)


employee_file = open("employees.txt")
print(employee_file.readlines()[1])