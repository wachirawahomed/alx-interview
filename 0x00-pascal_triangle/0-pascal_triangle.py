def pascal_triangle(n):
    """Returns a list of lists representing Pascal's Triangle of n."""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        # Start with a row of 1s
        row = [1] * (i + 1)
        # Fill in the middle elements
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    
    return triangle
