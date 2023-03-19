# python3
from threading import Thread

def parallel_processing(n, m, data):
    output = []
    print(data)
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    cnt=0
    time = 0
    joblist = {}
    for i in range(n):
        output.append((i, 0))
        joblist[i]= data[cnt]
        cnt=cnt+1
    while(cnt<len(data)):
        ind, minn = getmin(joblist)
        time = minn
        output.append((ind, time))
        joblist[ind]= data[cnt]+time
        cnt=cnt+1
    return output

def getmin(ddict):
    minn=ddict[0]
    ind = 0
    for (key, value) in ddict.items():
        if(value<minn):
            minn=value
            ind = key
    return [ind, minn]
    
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
    for key, value in result:
        print(str(key)+" "+str(value)
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
