#relative path of the file
#absolute path of the file
#just file name

employee_file = open("employees.txt","r")
# write -  w can modify existing and also can add new data
#append - a can"tmodify but can add data at the end
#r+ reading and writing
#store opened file inside a variable

    #print(employee_file.readable())
print(employee_file.read())
print(employee_file.readline())
#readline : reading individual line reading first line and move cursor to next line
#print(employee_file.readlines())
#readlines take all of the lines inside a file and put them in a single list
print(employee_file.readlines()[1])
#specific line inside of the list


for employee in employee_file.readlines():
    print(employee)

employee_file.close()