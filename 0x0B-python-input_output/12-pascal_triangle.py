#!/usr/bin/python3
""" Function to print pascal's triangle up to level <n> """


def pascal_triangle(n):
    """
    Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """

    if n <= 0:
        return []

    pascl_triangle = [[1]]
    while len(pascl_triangle) != n:
        triangle = pascl_triangle[-1]
        tmp = [1]
        for test in range(len(triangle) - 1):
            tmp.append(triangle[test] + triangle[test + 1])
        tmp.append(1)
        pascl_triangle.append(tmp)
    return pascl_triangle
