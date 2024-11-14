#import pick_food into our program

#first way of importing will be not aliasing
# import pick_food
# place = pick_food.pick()

#second way is to give it an alias.  All we are doing is changing the name of the module locally to set it apart

# import pick_food as mypick
# place = mypick.pick()

#final (and preferred to me) importing specific functions/methods from a module you want to use

from pick_food import pick
place = pick()



print(place)