#!/usr/bin/python3
'''Write a script markdown2html.py that takes an argument 2 strings:
First argument is the name of the Markdown file
Second argument is the output file name'''


import sys
import os

def heading(line):
    count = 0
    for character in line:
        if character == "#":
            count += 1
        else:
            break;
    return f"<h{count}>{line[count:]}</h{count}>\n"

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)
    if not os.path.exists(sys.argv[1]):
        sys.stderr.write("Missing " + sys.argv[1] + "\n")
        exit(1)

    with open(sys.argv[1]) as f:
        with open(sys.argv[2]) as html_file:
        lines = f.read().splitlines()
        content = ""

        for line in lines:
            if line.startswith("#"):
                content += heading(line)
        html_file.write(content)
        
    exit(0)
