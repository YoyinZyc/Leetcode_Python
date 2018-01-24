'''
题意：
给了一堆string，由256种ascii组成的，要求把这些str encode后返回一个string
同时要有decode的方法

思路：
存str们的长度，三部分
1. 有多少个str
2. 每个str多长，用，隔开
3. 把所有str组成一个str

每个部分之间也用逗号隔开
'''
class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        # 空
        if not strs:
            return ''
        ret = []
        # 第一部分，多少个str，注意int要转为str存
        ret.append(str(len(strs)))
        # 第二部分，每个str的长度
        for v in strs:
            ret.append(str(len(v)))
        # 第三部分，string
        s = ''.join(strs)
        ret.append(s)
        # 用，连起来
        return ','.join(ret)

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        # 空
        if not s:
            return []
        # 先split
        l = s.split(',')
        # 第一部分
        length = int(l[0])
        # 因为strs本身可能含有'，'，所以先把第三部分组合回来
        s = ','.join(l[length + 1:])
        ret = []
        j = 0
        # 按照第二部分的长度找每个str
        for i in range(1, length + 1):
            ret.append(s[j:j+int(l[i])])
            j += int(l[i])
        return ret
if __name__ == '__main__':
    c = Codec()
    c.decode(c.encode(["","123",",,,"]))
