#!/usr/bin/python3
'''Write a script markdown2html.py that takes an argument 2 strings:
First argument is the name of the Markdown file
Second argument is the output file name'''


import sys
from os.path import exists 

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html\n", file = sys.stderr)
        exit(1)
    if not exists(sys.argv[1]):
        print(f"Missing {sys.argv[1]}\n", file = sys.stderr)
        exit(1)
        
    exit(0)
