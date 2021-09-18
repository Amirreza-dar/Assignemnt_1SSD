# Task3

import time
from inspect import signature
import numpy as np
import inspect

class decorator3:
  def __init__(self,fun):
     self.fun= fun
     decorator3.fun1 = fun
     decorator3.source = inspect.getsource(fun)
     self.arguments= []
     decorator3.count= 0
     self.exe_time = 0

  def __call__(self,*args):
    start_time = 0
    decorator3.count+= 1
    self.output = self.fun(*args)
    start_time = time.time()
    self.fun(*args)
    self.exe_time = time.time() - start_time
    res = ''
    res = ' ' + str(decorator3.fun1.__name__) + ' ' + 'call:' + ' ' + str(self.count) + ' ' + 'executed in' + ' ' + str(format(self.exe_time, '.8f')) + ' ' + 'sec' + '\n'
    self.docstring = decorator3.fun1.__doc__
    self.type1 = type(self.fun)
    self.name = self.fun.__name__
    self.output = self.fun(*args)
    self.key =[]
    self.value =[]
    self.signature = inspect.signature(self.fun)
    self.Keyworded = {
        k: v.default
        for k, v in self.signature.parameters.items()
        if v.default is not inspect.Parameter.empty
    }
    self.positional = [
        k
        for k, v in self.signature.parameters.items()
        if v.default is inspect.Parameter.empty          
    ]

    res += 'Name:' + '\t' + str(self.name) + '\n'
    res += 'Type:' + '\t' + str(self.type1) + '\n'
    res += 'Sign:' + '\t' + str(self.signature) + '\n'
    res += 'Args:'  + '\t' + 'positional' + str(self.positional) + '\n'
    res += '    '  + '\t' + 'Key=worded' + str(self.Keyworded) + '\n'
    res += 'Docs:'  + '\t' + str(self.docstring) + '\n'
    res += 'Source:'+ '\t' + decorator3.source + '\n'
    res += 'Output:' + '\t' + str(self.output)

    with open('Dumped.txt', 'w') as dump:
      dump.write(res)
    with open('Dumped.txt', 'r') as dump1:
      read = dump1.read()
    print(read)
    return self.exe_time