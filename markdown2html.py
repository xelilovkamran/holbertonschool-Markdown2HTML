#!/usr/bin/python3
'''Write a script markdown2html.py that takes an argument 2 strings:
First argument is the name of the Markdown file
Second argument is the output file name'''


import sys
import os

def findLines(lines, index, type):
    selected = []

    if type == "p":
        for i in range(index, len(lines)):
            if lines[i] and lines[i][0].isalnum():
                selected.append(lines[i])
            else:
                break
        return selected

    if type == "ul":        
        for i in range(index, len(lines)):
            if lines[i] and lines[i][0] == "-":
                selected.append(lines[i])
            else:
                break
        return selected

    if type == "ol":        
        for i in range(index, len(lines)):
            if lines[i] and lines[i][0] == "*":
                selected.append(lines[i])
            else:
                break
        return selected
                    

def heading(line):
    count = 0
    for character in line:
        if character == "#":
            count += 1
        else:
            break
    return f"<h{count}>{line[count + 1:]}</h{count}>\n"

def listing(lines, type):
    html = ""
    html += f"<{type}>\n"
    for line in lines:
        html += f"<li>{line[2:]}</li>\n"
    html += f"</{type}>\n"
    
    return html

def paragraph(lines):
    html = ""
    html += f"<p>\n"
    for index, line in enumerate(lines):
        html += f"{line}\n"
        if index == len(lines) - 1:
            continue
        html += "<br />\n"
    html += f"</p>\n"
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
                if not line:
                    continue
                if line.startswith("#"):
                    content += heading(line)
                if line.startswith("-"):
                    selected = findLines(lines, index, "ul")
                    del lines[index:index + len(selected)]
                    content += listing(selected, "ul")
                if line.startswith("*"):
                    selected = findLines(lines, index, "ol")
                    del lines[index:index + len(selected)]
                    content += listing(selected, "ol")
                if line[0].isalnum():
                    selected = findLines(lines, index, "p")
                    del lines[index:index + len(selected)]
                    content += paragraph(selected)
                    
            html_file.write(content)
       
    exit(0)
