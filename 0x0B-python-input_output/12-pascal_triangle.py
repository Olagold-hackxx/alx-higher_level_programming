#!/usr/bin/python3


def pascal_triangle(n):
    """
    Print out pascal triangle
    
    Args: 
        n (int): must be a number 

    Return: a list of list of integers that forms pascal triangle's of n 

    """

    if n <= 0:
        return []
    pascalTriangle = [[1]]
    for currentRow in range(1, n):
        row = [1]
        prevRow = pascalTriangle[currentRow - 1]
        for column in range(1, currentRow):
            row.append(prevRow[column - 1] + prevRow[column])
        row.append(1)
        pascalTriangle.append(row)

    return (pascalTriangle)

pascal_triangle = __import__('12-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
