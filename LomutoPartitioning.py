def LomutoPartition(A, lo, hi):
    p = A[lo]
    s = lo
    for i in range(lo+1, hi+1) :
        if (A[i] < p) :
            s += 1
            A[s], A[i] = A[i], A[s]
    #         temp1 = A[s]
    #         A[s] = A[i]
    #         A[i] = temp1
    A[lo], A[s] = A[s], A[lo]
    # temp2 = A[0]
    # A[0] = A[s]
    # A[s] = temp2
    return s

def test():
    A = [4,7,9,3,5]
    print(LomutoPartition(A, 2, 3))
if __name__ == "__main__" :
    test()

