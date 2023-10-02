# importing argv from sys module
from sys import argv
# assign the argv values in script and filename
script, filename = argv

# Open the file using open(filename) and assign the file object 
txt = open(filename)
# Print the file name passed as a second argument which assigned to variable filename
print(f"Here's your file {filename}:")
# file object read method/function to read the content of the file
print(txt.read())
# close the open file object
txt.close()

print("Type the filename again:")
# Now take the file name as a input 
file_again = input("> ")
# open the file again with the input value stored in file_again variable
txt_again = open(file_again)
# print the file content again
print(txt_again.read())
txt_again.close()