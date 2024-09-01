#list to store a bunch of related values
#store multiple values
friends = ["kevin","karen","jim",2,False]
print(friends)
print(friends[0])
print(friends[-1])

#portion of the list
print(friends[1:])
print(friends[1:3]) #range  upto 3rd

friends[1] = "mike"  #modify

#functions
lucky_numbers =[45,83,15,12,23,42]
Friends = ["kevin","karen","jim","oscar","oscar","toby"]
print(Friends)
Friends.append("creed")
Friends.extend(lucky_numbers)
print(Friends)
Friends.insert(1,"kelly")
print(Friends)
Friends.remove("jim")
Friends.pop() #removes last element
print(Friends.index("kevin"))
print(Friends.count("oscar"))
lucky_numbers.sort() #sorts the list in ascending order
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

Friends2 = Friends.copy()
print(Friends2)

Friends.clear()
