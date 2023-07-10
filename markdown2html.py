#!/usr/bin/python3
"""
    python script to convert markdown to html
    usage: ./markdown2html.py <input_file> <output_file>
"""
import sys
import os.path

if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py <input_file> <output_file>\n")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.exists(input_file):
    sys.stderr.write("Missing {}\n".format(input_file))
    sys.exit(1)

# Perform the Markdown to HTML conversion here
# ...

sys.exit(0)

