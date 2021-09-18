#main.py
import math
from Task1 import decorator1
from Task2 import decorator2
from Task3 import decorator3
from Task4 import decorator4

@decorator1
def Quadratic(a,b,c):
  delta = b**2 - 4*a*c
  if delta > 0:
    return((-b + sqrt(delta))/2*a , (-b - sqrt(delta))/2*a)
  elif delta < 0:
    return "No root in real numbers"
  elif delta == 0:
    return -b/2*a
@decorator1
def String_converter(*item):
    string = ""
    return lamda for itmes in item : string += str(item)
@decorator2
def Random(bar1, bar2=""):
    """
    This function does something useful 
    :param bar1: description
    :param bar2: description
    """ 
    print("some\nmultiline\noutput")

@decorator3
def pascal_triangle(n = 5):
  Triangle = ''
  for line in range(1, n + 1):
      C = 1
      for i in range(1, line + 1):
          Triangle += str(C) + ' '
          C = int(C * (line - i) / i)
      Triangle += '\n'
  return Triangle

@decorator4
def Least_common_multiple(a,b):
  return lambda a,b : a*b/math.gcd(a,b)
# n = 10
# pascal_triangle(n)

Quadratic(2,4,5)
Random(None, "")
pascal_triangle(10)
Least_common_multiple(12,18)