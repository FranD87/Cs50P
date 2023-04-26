
name = input("What's your name? ")


# Prompt user for a name and store to a list then
# sort the names Alphbeta

# names = []
# for i in range(3):
#     name = input("What's your name? ")
#     names.append(name)
#
# for name in sorted(names):
#     print(f"hello, {name}")


# Open function allows you to open a file, "w" allows
# you to write to the file. When you write to a text file
# eah time it will overwrite the previous text
# file = open("names.txt", "w")
# file.write(name)
# file.close()

# "a" allows you to append the file but also when you
# write to the file use the \n to go to a new line
# whenever you prompt
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

# "with" function allows you to specify within this context
# that you want it to open and automatically close file.
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# "r"(comes default) allows you to read a file.

# Create a list to gather data, then iterate through file
# reading each line one at a time and strip of the new line
# and adding the name to the list, the reason to this
# is so you can sort all those names and print them in order,
# If you add reverse=True it will reverse the ordered list from Z - A

# names = []
#
# with open("names.txt") as file:
#     for line in file:
#        names.append(line.rstrip())
#
# for name in sorted(names, reverse=True):
#     print(f"hello, {name}")

# Shorter result would look like this

# with open("names.txt") as file:
#     for line in sorted(file):
#         print("hello,", line.rstrip())



# "readlines" allows you to read the lines in a file
# and return them as a list read the lines of text

#     lines = file.readlines()
# # Iterate of the lines
# for line in lines:
#     print("hello", line.rstrip())
















