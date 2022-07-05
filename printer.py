def printer(name):
    print("in function printer")
    print(name)
if __name__ == '__main__':
   import sys
   printer(sys.argv[1])