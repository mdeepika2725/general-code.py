def fib(n,a=0,b=1):
    if n:print(a,end=" ");fib(n-1,b,a+b)
fib(7)
