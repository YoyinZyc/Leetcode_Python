'''
一个奇怪的list，push的时候是push到头上，pop的时候按概率从头尾pop一个。
问如果push了一个sorted list进去，怎么pop一个sorted出来。
二问如果pop是从头出来，而push是概率到头尾，怎么pop一个sorted。
'''

'''
思路：
本质是一样的两问
都需要去对比当前pop出来的值和前一个pop出来的值
如果当前比前一个大：
    说明前一个是从左边来的，放进返回list；否则压到临时栈里面
最后当list遍历完了
按照顺序把栈里面的值pop出

'''