
def fibonacci(n):

    f = [0,1]

    while len(f) <= n:
        f.append(0)

    if n <= 1:
        return n
    else: 
        if f[n - 1] == 0:  
            f[n - 1] = fibonacci(n - 1)  
  
        if f[n - 2] == 0:  
            f[n - 2] = fibonacci(n - 2)  
              
    f[n] = f[n - 2] + f[n - 1]  
    
    return f[n]    


if __name__=='__main__':
    print(fibonacci(9))