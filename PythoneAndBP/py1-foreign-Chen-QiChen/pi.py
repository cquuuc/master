import sys
# import numpy as np
import math

def fuctionAll(eps,mode):
    res = 0
    k = 0
    # if(mode=='leibniz'):
    #     eps=eps/2
    formula={
        'leibniz':
            lambda k:4 *((-1) ** k / (2 * k + 1)),
        'pairwise': 
            lambda k:4/(4*k+1) - 4/(4*k+3) ,
        'bbp':
            lambda k: 1 / 16 ** k * (4 / (8 * k + 1) - 2 / (8 * k + 4) - 1 / (8 * k + 5) - 1 / (8 * k + 6))}
    while 1:
        term =formula[mode](k)
        res=res+term
        k = k + 1
        if abs(res - math.pi) < eps:
            break
    return k, res


# 设置精度
eps = 0.0001
mode='bbp'


if __name__ == "__main__":
    if sys.argv[1:]:
        eps = float(sys.argv[1])
        mode = sys.argv[2]
            
    
    print(fuctionAll(eps,mode))




