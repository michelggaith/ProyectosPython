def Fibonacci(i):
    if i == 0:
        return 0
    elif i==1:
        return 1
    else:
        return(Fibonacci(i-1)+Fibonacci(i-2))
    
##COMIENZO##
print(Fibonacci(15))