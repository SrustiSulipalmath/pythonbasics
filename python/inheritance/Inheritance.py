#define a bunch attributes functions inside of a class and we can create another class and we can inherit them
#create one which has all the functionality of another class without having to physically write any of
#the same methods attributes

from chef import chef
from chinesechef import chinesechef
mychef = chef()
mychef.make_special_dish()

mychineseschef = chinesechef()
mychineseschef.make_special_dish()     #override

