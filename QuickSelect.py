# using Partition method to find kth element in unsorted array
# first, find the A[lo] as pivot to find the partition position
# if that position is larger, go left, otherwise, go right
from LomutoPartitioning import LomutoPartition

def QuickSelect(A, lo, hi, k):
    s = LomutoPartition(A, lo, hi)
    if s - lo == k - 1:

        # we can find that the order of array A has already been modified due to Lomuto method
        print(A)
        return A[s]
    else:
        if s - lo > k - 1:
            return QuickSelect(A, lo, s-1, k)
        else:
            return QuickSelect(A, s+1, hi, (k-1) - (s-lo))
def test():
    A = [7,3,4,8,10,9]
    print(QuickSelect(A, 0, len(A)-1, 1))
if __name__ =="__main__":
    test()