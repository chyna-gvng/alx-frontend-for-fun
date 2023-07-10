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
html_content = re.sub(r'^# (.+)$', r'<h1>\g<1></h1>', markdown_content, flags=re.MULTILINE)

# Parse unordered lists and generate HTML
html_content = re.sub(r'^- (.+)$', r'<li>\g<1></li>', html_content, flags=re.MULTILINE)
html_content = re.sub(r'(<li>.+</li>)', r'<ul>\n\g<1>\n</ul>', html_content)

# Parse ordered lists and generate HTML
html_content = re.sub(r'^\* (.+)$', r'<li>\g<1></li>', html_content, flags=re.MULTILINE)
html_content = re.sub(r'(<li>.+</li>)', r'<ol>\n\g<1>\n</ol>', html_content)

# Parse paragraphs and generate HTML
html_content = re.sub(r'^(.+)$', r'<p>\g<1></p>', html_content, flags=re.MULTILINE)
html_content = re.sub(r'</(ul|ol)>\n<p>', r'</\g<1>>\n', html_content)
html_content = re.sub(r'</p>\n<(ul|ol)>', r'\n</\g<1>>\n', html_content)

with open(output_file, 'w') as file:
    file.write(html_content)

sys.exit(0)
