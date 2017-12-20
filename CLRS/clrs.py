def insertion_sort(lst):
    for idx in range(1, len(lst)):
        position = idx
        value = lst[idx]
        while position > 0 and lst[position-1] > value:
            lst[position] = lst[position-1]
            position -= 1
        lst[position] = value
    return lst

def selection_sort(lst):
    for idx in range(len(lst)-1):
        min = idx
        print (min)
        for j in range(idx+1, len(lst)):
            if lst[j] < lst[min]:
                min = j
        lst[idx], lst[min] = lst[min], lst[idx]
    return lst

import math

def merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L,R = [],[]
    for i in range(n1):
        L.append(A[p+i])
    for j in range(n2):
        R.append(A[q+j+1])
    L.append(float("inf"))
    R.append(float("inf"))
    i, j = 0, 0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A

def merge_sort(A, p, r):
    if p < r:
        q = math.floor((p+r)/2)
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)
    return A

def find_max_crossing_subarray(A, low, mid, high):
    left_sum, right_sum = -float("inf"), -float("inf")
    sum_ = 0
    for i in reversed(range(low, mid+1)):
        sum_ += A[i]
        if sum_ > left_sum:
            left_sum = sum_
            max_left = i
    sum_ = 0
    for j in range(mid+1, high+1):
        sum_ += A[j]
        if sum_ > right_sum:
            right_sum = sum_
            max_right = j
    return (max_left, max_right, left_sum + right_sum)


def find_maximum_subarray(A,low,high):
    if high == low:
        return (low, high, A[low])
    else:
        mid = math.floor((low+high)/2)
        (left_low, left_high, left_sum) = find_maximum_subarray(A, low, mid)
        (right_low, right_high, right_sum) = find_maximum_subarray(A, mid, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(A, low, mid, high)
    if right_sum > left_sum and right_sum > cross_sum:
        return (right_low, right_high, right_sum)
    elif left_sum > right_sum and left_sum > cross_sum:
        return (left_low, left_high, left_sum)
    else:
        return (cross_low, cross_high, cross_sum)

# print (find_max_crossing_subarray([3,-1,2,6,-9,11,-10],0,3,6))

def square_matrix_multiply(A, B):
    n = len(A)
    C = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = 0
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def matrix_add(A, B):
    n = len(A)
    C = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def square_matrix_multiply_recursive(A, B):
    n = len(A)
    C = [[0 for x in range(n)] for y in range(n)]
    if n == 1:
        C[0][0] = A[0][0]*B[0][0]
    else:
        half = len(A/2)
        C[:half][:half] = matrix_add(square_matrix_multiply_recursive(A[:half][:half], B[:half][:half]),
                                     square_matrix_multiply_recursive(A[:half][half:], B[half:][:half]))
        C[:half][half:] = matrix_add(square_matrix_multiply_recursive(A[:half][:half], B[:half][half:]),
                                     square_matrix_multiply_recursive(A[:half][half:], B[half:][half:]))
        C[half:][:half] = matrix_add(square_matrix_multiply_recursive(A[half:][:half], B[:half][:half]),
                                     square_matrix_multiply_recursive(A[half:][half:], B[half:][:half]))
        C[half:][half:] = matrix_add(square_matrix_multiply_recursive(A[half:][:half], B[:half][half:]),
                                     square_matrix_multiply_recursive(A[:half][:half], B[half:][half:]))
    return C

def matrix_add(A, B):
    n = len(A)
    C = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def matrix_sub(A, B):
    n = len(A)
    C = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C


    return

def strassen_algo(A, B):
    n = len(A)
    C = [[0 for x in range(n)] for y in range(n)]
    if n == 1:
        C[0][0] = A[0][0] * B[0][0]
    else:
        half = len(A)/2
        A11 = A[:half][:half]
        A12 = A[:half][half:]
        A21 = A[half:][:half]
        A22 = A[half:][half:]
        B11 = B[:half][:half]
        B12 = B[:half][half:]
        B21 = B[half:][:half]
        B22 = B[half:][half:]

        M1 = strassen_algo(matrix_add(A11, A22), matrix_add(B11, B22))
        M2 = strassen_algo(matrix_add(A21, A22), B11)
        M3 = strassen_algo(A11, matrix_sub(B12, B22))
        M4 = strassen_algo(A22, matrix_sub(B21, B11))
        M5 = strassen_algo(matrix_add(A11, A12), B22)
        M6 = strassen_algo(matrix_sub(A21, A11), matrix_add(B11, B12))
        M7 = strassen_algo(matrix_sub(A12, A22), matrix_add(B21, B22))

        C[:hlf][:half] = matrix_add(matrix_sub(matrix_add(M1, M4), M5), M7)
        C[:half][half:] = matrix_add(M3, M5)
        C[half:][:half] = matrix_add(M2, M4)
        C[half:][half:] = matrix_add(matrix_add(matrix_sub(M1, M2), M3), M6)
    return C

# assume n is a list of numbers, the larger the number the better the people would be
def hire_assistant(n):
    best = -1
    for i in range(len(n)):
        # interview i
        if n[i] > best:
            best = i
            # hire i

import random

def permute_by_sorting(A):
    n = len(A)
    P = [0 for x in range(n)]
    dict = {}
    for i in range(n):
        P[i] = random.randint(i, n**3) # **3 just because its unlikely there are two same P[i]
        dict[str(A[i])] =  P[i]

    return sorted(dict, key=dict.get)

def randomize_in_place(A):
    n = len(A)
    for i in range(n):
        ran = random.randint(i, n)
        A[i], A[ran] = A[ran], A[i]
    return A

def randomized_hire_assistant(n):
    n = randomize_in_place(n)
    # n = permute_by_sorting(n)
    best = -1
    for i in range(len(n)):
        # interview i
        if n[i] > best:
            best = i
            # hire i

# A -> a list of number
# i -> index i
def max_heapify(A, i):
    l = i*2
    r = i*2+1
    if l <= len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= len(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

# A -> list of number
def build_max_heap(A):
    size = len(A)
    for i in range(size//2-1)[::-1]:
        max_heapify(A, i)

# A -> list of number
def heapsort(A):
    build_max_heap(A)
    len = len(A)
    for i in range(1, len-1)[::-1]:
        A[0], A[i] = A[i], A[0]
        len -= 1
        max_heapify(A,0)

def heap_maximum(A):
    return A[0]

def heap_extract_max(A):
    if len(A) < 1:
        return False
    max = A[0]
    A[0] = A[-1]
    A = A[:-1]
    max_heapify(A, 0)
    return max

def heap_increase_key(A,i,key):
    if key < A[i]:
        return False
    A[i] = key
    while i > 0 and A[i//2] < A[i]:
        A[i], A[i//2] = A[i//2], A[i]
        i = i//2

def max_heap_insert(A, key):
    A.append(-float("inf"))
    heap_increase_key(A, len(A)-1, key)

def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1  # A[i] > x before swapping
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def random_partition(A, p, r):
    i = random.randint(p,r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

def random_quicksort(A, p, r):
    if p < r:
        q = random_partition(A, p, r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)


A = [2,8,7,1,3,5,6,4]
p = 0
r = 7
random_quicksort(A,p,r)
print (A)
#
# def quicksort(A,p,r):
