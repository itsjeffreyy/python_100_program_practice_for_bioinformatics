# author: Jeffreyy C.H. Yu
# Note: Calculate the length of the string user entered.
import sys
if len(sys.argv) >1:
    string = sys.argv[1]
else:
    string = str(input("Please enter the string: "))


print(len(string), string)
