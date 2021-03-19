def path_number(m, n):
    """Count path number"""
    if m == 1 and n == 1:
        return 0
    if m == 1:
        return 1
    if n == 1:
        return 1
    else:
        return path_number(m - 1, n) + path_number(m, n - 1)


def printallpathsuntil(mat, i, j, m, n, path, pi):
    """mat: Coordinates in tuples of all the points in the path matrix
    i,j: Current position
    pi: Next index to be filed in path array
    path: The path traversed so far
    """
    if i == m - 1:
        for k in range(j, n):
            path[pi + k - j] = mat[i][k]

        for l in range(pi + n - j):
            print(path[l], end=' ')

        print()
        return

    if j == n - 1:
        for k in range(i, m):
            path[pi + k - i] = mat[k][j]

        for l in range(pi + m - i):
            print(path[l], end=' ')
        print()
        return

    path[pi] = mat[i][j]
    printallpathsuntil(mat, i + 1, j, m, n, path, pi + 1)
    printallpathsuntil(mat, i, j + 1, m, n, path, pi + 1)


def printallpaths(mat, m, n):
    path = [(0, 0) for i in range(m + n)]
    printallpathsuntil(mat, 0, 0, m, n, path, 0)


def print_path_amount_and_details(m, n):
    """Function to call all functions above for one-time solutions"""
    print(path_number(m, n))
    mat = []
    # [i][j]
    for i in range(m):
        line = []
        for j in range(n):
            line.append((j,i))
        mat.append(line)

    printallpaths(mat, m, n)


print_path_amount_and_details(4, 3)
