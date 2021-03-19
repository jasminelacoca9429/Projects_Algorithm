import numpy as np


def heartless_array(n, m):
    '''Creates an array with shape(m,n) that is
    filled with zeros and edged by ones'''
    a = np.ones((n, m))
    a[1:n - 1, 1:m - 1] = 0
    return a


def find_closest_value(a, v):
    '''Gets the closest-to-v number in array a'''
    a = np.asarray(a)
    return a[(np.abs(a - v)).argmin()]


def row_sum_to_one(M):
    '''Normalized the matrix to the sum of each row is 1'''
    M = np.asarray(M)
    return M / M.sum(axis=1, keepdims=1)


def find_local_maxima(a):
    '''Find all the local maximas in a 1-D array'''
    a = np.asarray(a)
    peaks = np.where((a[1:-1] > a[:-2]) & (a[1:-1] > a[2:]))
    return a[1:-1][peaks]


a = heartless_array(4, 6)
print('The heartless array is','\n',a)

b = find_closest_value([10, 3, 7, 8, 15], 4)
print('The closest-to-v number in this array is', '\n',b)

c = row_sum_to_one([[3, 6, 6, 4], [0, 5, 7, 5], [4, 6, 0, 4], [8, 7, 4, 9]])
print('The normalized matrix is','\n', c)

d = find_local_maxima([5, 8, 3, 1, 10, 9, 12])
print('The local maxima values are', '\n',d)
