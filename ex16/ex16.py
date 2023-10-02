from sys import argv
script, filename = argv


print(f"We are going to erase {filename}.")

# Prompt that is asking if user want to truncate/delete the file content or cancle it.
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")
print("Opening the file...")
# Opening a file with the write mode so user can able to write the content inside a file using a file object write() funciton
target = open(filename, 'w')
print("Truncating the file. Goodbye!")
# File object another method called truncate() - which is used to delete the content of the files.
target.truncate()


# now acception the input from the user in three different lines
print("Now I'm goint to ask you for three lines.")
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")


# writing the content inside line1,line2 and line3 variable inside a target file using write method of the file object
print("I'm going to write these to the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
# Close the file after usage.
target.close()