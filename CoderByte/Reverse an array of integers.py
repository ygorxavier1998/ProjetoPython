#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    print(a[::-1])

arr = [0, 1, 2, 3, 4, 5, 6, 7]
print(reverseArray(arr))