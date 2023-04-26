def main():
    hello("World")
    goodbye("World")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

#Value set by python when you run a file from the command line
#If the name been called in another module is main then and
#only then should you call main
if __name__ == '__main__':
    main()

