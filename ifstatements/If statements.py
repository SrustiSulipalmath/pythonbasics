is_male = False
is_tall = True
if is_male:
    print("you are a male")
else:
    print("you are not a male ")

#and
if is_male or is_tall:
    print("you are a male or tall or both")
else:
    print("you are neither a male nor tall")

if is_male and is_tall:
    print("you are a tall male ")
else:
    print("you are either not male or tall or both")

if is_male and is_tall:
    print("you are a tall male ")
elif is_male and not(is_tall):
    print("you are a short male ")
elif is_tall and not(is_male):
    print("you are not a male but are tall ")
else:
    print("you are either not male or tall or both")


