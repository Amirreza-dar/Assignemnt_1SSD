# Task 4
import sys
import datetime
from inspect import signature
import numpy as np
import inspect
def decorator4(fun):
  def wrapper(*args):
    try:
      Docstring = fun.__doc__
      Type = type(fun)
      Name = fun.__name__
      source = inspect.getsource(fun)
      output = fun(*args)
      key =[]
      value =[]
      signature = inspect.signature(func)
      Keyworded = {
          k: v.default
          for k, v in signature.parameters.items()
          if v.default is not inspect.Parameter.empty
      }
      positional = [
          k
          for k, v in signature.parameters.items()
          if v.default is inspect.Parameter.empty

      ]
      print(Type)
      print(Docstring)
      print(Name)
      print('positional',positional)
      print('key=worded',Keyworded)
      print(signature)
      print(source)
      print(output)

    except:
      with open("Log.txt","w") as file:
        file.write('Error Type: ' + str(sys.exc_info()[0]) + ', Error: ' + str(sys.exc_info()[1]) + '. Timestamp: ' + str(datetime.datetime.now()))
      with open("Log.txt",'r') as file:
        read = file.read()
      print('Ops!!! the error handled the log.txt file contains the following error:', '\n', read)
  
  return wrapper