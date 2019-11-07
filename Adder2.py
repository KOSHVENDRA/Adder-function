def adder(*arg):
    sum=arg[0]
    for i in range(len(arg)-1):
        sum=sum+arg[i+1]
    return(sum)
