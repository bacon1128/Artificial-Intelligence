# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 14:19:04 2022

@author: 林培瑋
"""
import numpy as np

NUM1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9]])
NUM2 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9]])
i = 1

print("點名作業2 408440450 林培瑋")

# 使用np.multiply以及For & while將兩個陣列中的元素相乘，並得到99乘法表。
while i <= 9:
    for j in range(1, 10):
        # NUM1陣列的第i-1個元素與NUM2陣列的第j-1個元素相乘。
        print("%d x %d = %02d " % (j, i, np.multiply(NUM1[:,i-1], NUM2[:,j-1])), end = (" "))
    print()
    i = i + 1

