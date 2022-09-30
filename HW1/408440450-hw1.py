# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 09:15:15 2022

@author: 林培瑋
"""

# 隨機產生15個亂數並放到陣列裡(不重複)
import random
randomlist = random.sample(range(99), 15)

'''----------------------------------------------------------------------------
# 隨機產生15個亂數並放到陣列裡(可能重複)
randomlist = []
for i in range(0,15):
    n = random.randint(1,99)
    randomlist.append(n)
----------------------------------------------------------------------------'''

'''-------------------------------------------------------------------------'''
# Quicksort函式    
def quicksort(data, start, end): # 輸入資料，起始位置，結束位置
    if start >= end :            # 如果起始位置大於結束位置，跳出函式
        return

    i = start                      # 左邊的起始點
    j = end                        # 右邊的起始點
    key = data[start]              # 基準值

    while i != j:                  
        while data[j] > key and i < j:   # 從右起始點開始比較，找比基準值小的值
            j -= 1
        while data[i] <= key and i < j:  # 從左起始點開始比較，找比基準值大的值
            i += 1
        if i < j:                        # 當左右起始點不相同時，左右起始點互換值
            data[i], data[j] = data[j], data[i] 

    # 將基準值歸換至左右起始點相同的地方
    data[start] = data[i] 
    data[i] = key

    quicksort(data, start, i-1)   # 繼續處理基準值左方quicksort
    quicksort(data, i+1, end)     # 繼續處理基準值右方quicksort
'''-------------------------------------------------------------------------'''

# Main function
quicksort(randomlist, 0, len(randomlist)-1)
print("HW1 408440450 林培瑋 ")
print(randomlist)