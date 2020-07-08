def insertion_sort(A, N):
    for i in range(1, N, 1):
        A_str = [str(x) for x in A]
        print(" ".join(A_str))
        v = int(A[i])
        j = i - 1
        while j >= 0 and int(A[j]) > v:
            A[j + 1] = int(A[j])
            j = j - 1
        A[j + 1] = v
    A_str = [str(x) for x in A]
    print(" ".join(A_str))


_N = int(input())
_A = list(input().split())
_A = [int(x) for x in _A]
insertion_sort(_A, _N)
