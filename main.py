# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    for i in range(m):
        print("thread"+str(i))
        th = Thread(target=dojob, args=data[i])
    return output

def dojob(i):
    print(i)
    
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
    data = []

    # TODO: create the function
    result = parallel_processing(int(n),int(m),data)
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
