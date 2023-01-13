import sys
import os

currentDirectory = os.path.dirname(os.path.abspath(__file__))

def test():
    f = open(currentDirectory+"\\NewBookList.txt", "a")
    for i in range(len(sys.argv)):
        f.write(sys.argv[i]+" ")
    f.close()
test()