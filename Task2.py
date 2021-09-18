# Task 2

from inspect import signature
import numpy as np
import inspect
def decorator2(fun):
  def wrapper(*args):
    Docstring = fun.__doc__
    Type = type(fun)
    Name = fun.__name__
    source = inspect.getsource(fun)
    print(type(source))
    output = fun(*args)
    key =[]
    value =[]
    print(args)
    signature = inspect.signature(fun)
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
    
  return wrapper