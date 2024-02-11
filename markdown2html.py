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
            break
    return f"<h{count}>{line[count + 1:]}</h{count}>\n"

def listing(index, line, lines, type):
    html = ""
    # to prevent -1 index
    if index == 0:
        html += f"<{type}>\n"

    # to prevent "string index out of range" error
    if not lines[index - 1]:
        html += f"<{type}>\n"
    elif line[0] != lines[index - 1][0]:
        html += f"<{type}>\n"
        
    html += f"<li>{line[2:]}</li>\n"

    # if last line, close the list
    if index == len(lines) - 1:
        html += f"</{type}>\n"
        return html

    # to prevent "string index out of range" error
    if not lines[index + 1]:
        html += f"</{type}>\n"
    elif line[0] != lines[index + 1][0]:
        html += f"</{type}>\n"

    return html

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)
    if not os.path.exists(sys.argv[1]):
        sys.stderr.write("Missing " + sys.argv[1] + "\n")
        exit(1)

    with open(sys.argv[1]) as f:
        with open(sys.argv[2], "w") as html_file:
            lines = f.read().splitlines()
            content = ""

            for index, line in enumerate(lines):
                if line.startswith("#"):
                    content += heading(line)
                if line.startswith("-"):
                    content += listing(index, line, lines, "ul")
                if line.startswith("*"):
                    content += listing(index, line, lines, "ol")
                    
            html_file.write(content)
       
    exit(0)
