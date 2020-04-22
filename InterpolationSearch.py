# perform a linear interpolation "mid" between lo and hi
def InterpolationSearch(A,k):
    lo = 0
    hi = len(A)-1
    while lo < hi:
        if A[lo] > k or A[hi] < k:
            break
        if lo == hi:
            if A[lo] == k:
                return lo
            else:
                break
        mid = lo + (k - A[lo])*(hi - lo) // (A[hi] - A[lo])
        if A[mid] == k:
            return mid
        if A[mid] > k:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

def test():
    A = [1,3,4,5,7,8,11]
    print(InterpolationSearch(A, 11))
if __name__ =="__main__" :
    test()