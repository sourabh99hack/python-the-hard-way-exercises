# This one is like your scrits with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# Ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
    
# this just takes one argumet
def print_one(arg1):
    print(f"arg1: {arg1}")
    
# this one takes no arguments
def print_none():
    print("I got nothin'.")
    
   
print_two("Sourabh", "Nahatkar")
print_two_again("Sourabh", "Nahatkar")
print_one("First!")
print_none()