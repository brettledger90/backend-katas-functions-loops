def add(x,y):
  return x+y

def multiply(x,y):
  result=0
  for i in range(1,y+1):
     result=add(result,x)

  return result

def power(x,n):
  result=x
  for i in range(1,n):
    result=multiply(result,x)
  return result

def factorial(x):
  result = 1
  for i in range(1,x+1):
    result = multiply(i,result)
  return result

def fibonacci(n):
  a =0
  b=1
  if n < 0:
    c = "undefined"
  elif n == 0 :
     a = 0 
     c = 0
  elif n ==1:
    b=1
    c=1
  else:
    for i in range(2,n):
      c = add(a,b)
      a=b
      b=c

  return c

print(add(2,4))
print(multiply(6,8))
print(power(2, 8))
print(factorial(4))
print(fibonacci(8))