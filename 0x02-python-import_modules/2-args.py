#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    result = len(sys.argv) - 1
    if result == 0:
        print("0 arguments.")
    elif result == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(result))
    for x in range(result):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
