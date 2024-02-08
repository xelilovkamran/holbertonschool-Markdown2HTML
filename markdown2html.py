#!/usr/bin/python3

import sys
from os.path import exists 

if __name__ == "__main__":
    arguments = sys.argv
    if len(arguments) < 2:
        print("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)
    elif not exists(f"./{arguments[1]}"):
        print(f"Missing {arguments[1]}")
        sys.exit(1)
    else:
        sys.exit(0)
