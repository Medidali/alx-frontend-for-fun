#!/usr/bin/python3
import sys
import os
import re

def usage():
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    exit(1)

def missing_file(filename):
    print(f"Missing {filename}", file=sys.stderr)
    exit(1)

def parse_markdown_to_html(markdown_file, html_file):
    # Implement parsing markdown to html here
    pass

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()

    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    if not os.path.exists(markdown_file):
        missing_file(markdown_file)

    parse_markdown_to_html(markdown_file, html_file)
