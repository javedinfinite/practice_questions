# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import re

def solution(S):

    pattern = '^a*b*$'
    result = re.match(pattern, S)

    if result:
        return True
    else:
        return False	