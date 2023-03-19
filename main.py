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
    next = getmin(output)
    print(next)
    return output

def getmin(llist):
    minn=999999
    for (key, value) in llist:
        if(value<minn):
            minn=value
    return value
    
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
    for val in data:
        val=int(val)
    # TODO: create the function
    result = parallel_processing(int(n),int(m),data)
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
