'''
设计一个类
class EncodingChecker {
   EncodingChecker(String pattern) { ... } // constructor
   boolean isEncoded(String s) { ... } // for any string s, check whether s is encoded from pattern, see below
}.
pattern = 'abcabc'
s          = '123123'  -> True
           = 'cbzabc'   -> False
           = 'xyzxyz'    -> True

二问：如果pattern不是一个而是一百万个，怎么写isEncoded?

思路：
把所有pattern都encode，放进set里面，对于一个新的s，先encode，然后检查是不是在set里面
'''
class EncodingChecker(object):
    def __init__(self, pattern):
        self.p = set()
        for v in pattern:
            self.p.add(self.encode(v))
    def encode(self, s):
        l = [chr(ord('a')+i) for i in range(26)]
        d = dict()
        ret = ''
        for v in s:
            if v not in d:
                d[v] = l.pop(0)
            ret += d[v]
        return ret
    def isEncode(self,s):
        return self.encode(s) in self.p
if __name__ == '__main__':
    e = EncodingChecker(pattern=['acd','aae','ioo','ppee'])
    print(e.isEncode('1121'))