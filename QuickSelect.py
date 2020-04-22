from LomutoPartitioning import LomutoPartition

def QuickSelect(A, lo, hi, k):
    s = LomutoPartition(A, lo, hi)
    if s - lo == k - 1:
        return A[s]
    else:
        if s - lo > k - 1:
            return QuickSelect(A, lo, s-1, k)
        else:
            return QuickSelect(A, s+1, hi, (k-1) - (s-lo))
def test():
    A = [3,1,4,5,9,2,6,8]
    print(QuickSelect(A, 0, len(A)-1, 7))
if __name__ =="__main__":
    test()