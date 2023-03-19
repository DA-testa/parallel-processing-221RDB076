# python3
from threading import Thread

def parallel_processing(n, m, data):
    output = []
    print(data)
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    cnt=0
    for i in range(n):
        output.append((i, data[cnt]))
        cnt=cnt+1
    while(cnt+1<len(data)):
        next = getmin(output)
        output.append((next, data[cnt]))
        cnt=cnt+1
    print(output)
    return output

def getmin(llist):
    minn=llist[0][0]
    ind = 0
    for (key, value) in llist:
        if(value<minn):
            minn=value
            ind = key
    return ind
    
def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    ln = input()
    
    n = 0
    m = 0
    n,m = ln.split(" ")
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = input().split()
    for  i in range(len(data)):
        data[i]=int(data[i])
    # TODO: create the function
    result = parallel_processing(int(n),int(m),data)
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
