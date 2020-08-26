def fib_rec(n):
  """
  param: n - the number of digits to go to
  return: returns a list of fibonacci digits to n
  """
  if n == 1:
    return [0]
  elif n == 2:
    return [0,1]
  else:
    x = fib_rec(n-1)
    # the new element the sum of the last two elements
    x.append(sum(x[:-3:-1]))
    return x
        
  
n = 10
print(fib_rec(n))
