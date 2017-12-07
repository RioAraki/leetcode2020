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

def square_matrix_multiply_recursive(A, B):
    n = len(A)
    C = [[0 for x in range(n)] for y in range(n)]
    if n == 1:
        C[0][0] = A[0][0]*B[0][0]
    else:
        C[0][0] = square_matrix_multiply_recursive(A[:len(A)/2][:len(A)/2], B[:len(A)/2][:len(A)/2]) + \
                  square_matrix_multiply_recursive(A[:len(A)/2][len(A)/2:], B[len(A)/2:][:len(A)/2])
        C[0][1] = square_matrix_multiply_recursive(A[:len(A)/2][:len(A)/2], B[:len(A)/2][len(A)/2:]) + \
                  square_matrix_multiply_recursive(A[:len(A)/2][len(A)/2:], B[len(A)/2:][len(A)/2:])
        C[1][0] = square_matrix_multiply_recursive(A[len(A)/2:][:len(A)/2], B[:len(A)/2][:len(A)/2]) + \
                  square_matrix_multiply_recursive(A[len(A)/2:][len(A)/2:], B[len(A)/2:][:len(A)/2])
        C[1][1] = square_matrix_multiply_recursive(A[len(A)/2:][:len(A)/2], B[:len(A)/2][len(A)/2:]) + \
                  square_matrix_multiply_recursive(A[:len(A)/2][:len(A)/2], B[len(A)/2:][len(A)/2:])
    return C

def strassen_algo(A, B):
    


# print (merge_sort([8,2,4,1,7,6,0,9,3],0,7))
# print(selection_sort([3,4,2,5,1]))


