# O(n^2)
# in-place
# stable
def InsertionSort(A):
    for i in range(1, len(A)):
        v = A[i]
        j = i - 1
        while j >= 0 and v < A[j]:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = v

def test():
    A = [25, 14, 6, 7, 5, 1]
    InsertionSort(A)
    print(A)

if __name__ == "__main__":
    test()