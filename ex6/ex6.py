# defining a variable and assigning the integer value 10 to it
types_of_people = 10
# assigning a fstring to a variable x in which types_of_people variable value 10 is present.
x = f"There are {types_of_people} types of people"

# Defining 2 variables with string values in it.
binary = "binary"
do_not = "don't"

# assigning F string to variable y created using above two binary and do_not string type variables
y = f"Those who know {binary} and those who {do_not}"
# Printing x and y string variables
print(x)
print(y)

# Printing fString modified with above x and y string variables
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Assigning a boolean False to a variable name hilarious
hilarious = False
# creating a format string with empty {} curly braces.
joke_evaluation = "Isn't that joke so funny?! {}"
# use the string.format() function to attach the variable hilarious into the string and print it.
print(joke_evaluation.format(hilarious))

# Creating 2 string Variables 
w = "This is the left side of ..."
e = "a string with a right side."

# Concatenate the above 2 string pariables and print it
print(w + e)