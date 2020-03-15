
def fibonacci(n):

    f = [0,1]
    i = 2

    while i <= n:
        f.append(f[i - 1] + f[i - 2])
        i = i + 1
    
    return f[n]    


if __name__=='__main__':

    print(fibonacci(12))