# import cowsay
import sys
#Main will not get called because we specified
# if __name__ == '__main__': in sayings.py
from sayings import hello


#If the user obliges by giving 2 command line arguements
if len(sys.argv) == 2:
    hello(sys.argv[1])

# if len(sys.argv) == 2:
#     cowsay.cow("hello, " + sys.argv[1])
#
# if len(sys.argv) == 2:
#     cowsay.trex("hello, " + sys.argv[1])


