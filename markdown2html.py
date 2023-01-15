"""
    Scripts takes two arguments:
    - Name of markdown file
    - Output file name
    Return
    - Exit with 1 if arguments < 2
    - Exit with 1 if file not found
    - Exit with 0 if success.
"""

import sys
import os

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            'Usage: ./markdown2html.py README.md README.html',
            file=sys.stderr
        )
        exit(1)
    if not os.path.isfile(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]))
        exit(1)
    else:
        exit(0)
