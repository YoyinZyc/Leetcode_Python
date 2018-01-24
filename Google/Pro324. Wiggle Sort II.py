'''
1.  找到中位数 k-th element  (nums.length + 1) / 2
2.  比中位数大的放在 last even
    比中位数小的放在 first odd
    和中卫数相等的放在剩下的位置
3.  map的公式  （1 + 2*index) % (n | 1)
'''