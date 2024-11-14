#using a more functional style vs oop
#functional - separate data and functions/methods
#oop/classes - bundle action and data together

#true functional lanaguage (haskell and kind of rust) have some of the following characteristics:

#they use recursion - don't loop
#no classes - they may have objects/dicts/structures but no methods
#variables are immutable or contants by default - they instead are replaced or overwritten (state)
#they can use map and reduce to filter out a list

#recursion - function that calls itself over and over until a condition is met.  Kind of the function version of loop (but not really)

def countdown(number):
  if number <= 0:
    return
  else:
    print(number)
    countdown(number - 1)


countdown(5)