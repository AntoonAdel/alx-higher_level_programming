#!/usr/bin/env python3
def islower(c):
    char = ord(c)
    if char in range(97, 123):
        return True
    else:
        return False
