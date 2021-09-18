# Task 1
import time
def decorator1(fun):
  count = 0
  def wrapper(*args):
   exec_time = 0 
   nonlocal count 
   count += 1
   start_time = 0
   start_time = time.time()
   fun(*args)
   exec_time = time.time() - start_time
   print(fun.__name__ ,'call:', count, 'executed in', format(exec_time, '.8f'), 'sec')
  return wrapper