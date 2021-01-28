import numpy as np
import json
import datetime


A = np.array([[0,0,0,0,0,0,0],
             [0.0449,0,0.9,0.202,0,0,0],
             [0.0456,0.1,0,0.78,0,0,0],
             [0.2083,0,0,0,0,0,0],
             [0.0291,0,0,0,0,0,0],
             [0.0461,0,0,0,0,0,0],
             [0,0.9,0.1,0,0,0,0]])     #所有边的矩阵

I = np.identity(len(A)) #单位矩阵
print(I)

# A = np.array(data)
B = np.linalg.inv(I-A)  #求逆矩阵
# print(B[:,0])   #取出第一列
C= A.dot(B)  #矩阵乘法，针对中心结点的所有权

print(C)