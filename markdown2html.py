#!/usr/bin/python3
"""
    python script to convert markdown to html
    usage: ./markdown2html.py <input_file> <output_file>
"""
import sys
import os.path
import re

if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py <input_file> <output_file>\n")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.exists(input_file):
    sys.stderr.write("Missing {}\n".format(input_file))
    sys.exit(1)

with open(input_file, 'r') as file:
    markdown_content = file.read()

# Parse headings and generate HTML
html_content = re.sub(r'^-\s+(.+)$', r'<ul>\n<li>\g<1></li>\n</ul>', markdown_content, flags=re.MULTILINE)

with open(output_file, 'w') as file:
    file.write(html_content)

sys.exit(0)
