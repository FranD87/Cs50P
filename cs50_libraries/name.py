#Gives access to command line arguments
import sys

# sys.argv is and arguement vector that gives all the words
#that where typed at the prompt including the programs file name
# sys.exit can take different types of inputs, if you pass a string
# it will print that string and exit from the program
# try:
# Check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguements")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguements")
#Slices the list from element 1 to end of list
for arg in sys.argv[1:]:
    print("hello, my name is", arg)

# Print name tags
print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguements")

