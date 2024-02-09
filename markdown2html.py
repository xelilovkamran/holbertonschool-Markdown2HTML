#!/usr/bin/python3
'''Write a script markdown2html.py that takes an argument 2 strings:
First argument is the name of the Markdown file
Second argument is the output file name'''


import sys
from os.path import exists 

if __name__ == "__main__":
    arguments = sys.argv
    if len(arguments) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)
    if not exists(f"./{arguments[1]}"):
        sys.stderr.write(f"Missing {arguments[1]}")
        sys.exit(1)
        
    sys.exit(0)
