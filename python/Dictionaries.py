#special structure in python which allows us to store information key value pairs
from idlelib.editor import keynames

#create bunch of different key value pairs in dictionary and acces specific information inside of the dictionary can refer to it by key
# "keys" : "values"
#keys must be unique
month = {
    "jan" : "january",
    "feb" : "febraury",
    "mar" : "march",
    "apr" : "april",
    "may" : "may",
    "jun" : "june",
    "jul" : "july",
    8 :"august"
}

print(month["jun"])
print(month.get("jan","not a valid key")) #default value
