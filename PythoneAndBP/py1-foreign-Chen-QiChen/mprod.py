'''
Write a program mprod.py that returns the matrix product of the given matrices. 
Any number of matrices may be given as input, 
which are passed as lines of the form '-1 2 3, 4 -5 6, 7 8 -9'.

% python3 mprod.py

    Error: invalid input

% python3 mprod.py '1 2 3,4 5 6'

    [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]

% python3 mprod.py '1 2 3,4 5 6' '1 0,0 1'                                      

    Error: incompatible sizes of matrices

% python3 mprod.py '1 2 3,4 5 6' '1 0 0,0 1 0,0 0 1'

    [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]

% python3 mprod.py '1 2 3,4 5 6' '1 0 0 1,0 1 0 2,0 0 1 3' '1 -1,1 -1,1 -1,1 -1'

    [[20.0, -20.0], [47.0, -47.0]]
'''

import sys
import numpy as np
import math
# 从输入行中解析矩阵
def parse_matrix(line):
    matrix = []
    rows = line.strip().split(',')
    for row in rows:
        try:
            matrix.append([int(num) for num in row.split()])
        except ValueError:
            return None
    return np.array(matrix)

# 计算矩阵乘积
def matrix_product(matrices):
    if len(matrices) == 0:
        print('Error: invalid input')
        return None

    result = matrices[0]
    for i in range(1, len(matrices)):
        if result.shape[1] != matrices[i].shape[0]:
            print('Error: incompatible sizes of matrices')
            return None
        result = np.dot(result, matrices[i])
    return result

if __name__ == "__main__":
    # 预定义两个矩阵数据
    matrix_data = sys.argv

    matrices = [parse_matrix(line) for line in matrix_data if parse_matrix(line) is not None]

    result = matrix_product(matrices)
    if result is not None:
        print(result)

    
