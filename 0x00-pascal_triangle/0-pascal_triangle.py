#!/usr/bin/python3
"""
Module for generating Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list of lists: Pascal's Triangle represented as a list of lists.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # Each row starts with 1
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)  # Each row ends with 1
        triangle.append(row)

    return triangle
