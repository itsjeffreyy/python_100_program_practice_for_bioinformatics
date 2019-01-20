#!/usr/bin/env python
# author: Jeffreyy C.H. Yu
# Note: Calculate the length of the string user entered.
# usage: `python count_string_length.py` or `python count_string_length.py your_string`.
#        The result shows the length of your string and your real string.

import sys
if len(sys.argv) >1:
    string = sys.argv[1]
else:
    string = str(input("Please enter your string: "))


print(len(string), string)
