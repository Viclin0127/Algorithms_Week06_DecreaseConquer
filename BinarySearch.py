# try again BinarySearch without recursion
def BinarySearch(A, lo, hi, k):
    while lo <= hi:
        m = lo + (hi - lo)//2
        if A[m] == k:
            return m
        if k > A[m]:
            lo = m + 1
        else:
            hi = m - 1
    return -1

def test():
    A = [1,3,4,5,6,7]
    print(BinarySearch(A, 0, len(A)-1, 5))

if __name__ == "__main__":
    test()