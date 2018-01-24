'''
给了一个压缩的String
要求实现他的iterator

StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");

iterator.next(); // return 'L'
iterator.next(); // return 'e'
iterator.next(); // return 'e'
iterator.next(); // return 't'
iterator.next(); // return 'C'
iterator.next(); // return 'o'
iterator.next(); // return 'd'
iterator.hasNext(); // return true
iterator.next(); // return 'e'
iterator.hasNext(); // return false
iterator.next(); // return ' '

因为数字可能很大，所以不能提前存储成一个list
'''
class StringIterator(object):
    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.al = []
        self.time = []
        i = 0
        while i < len(compressedString):
            # if compressedString[i].isalpha():
            j = i + 1
            while j < len(compressedString) and compressedString[j].isdigit():
                j += 1

            self.al.append(compressedString[i])
            self.time.append(int(compressedString[i + 1:j]))
            i = j

    def next(self):
        """
        :rtype: str
        """

        if self.al:
            v = self.al[0]
            self.time[0] -= 1
            if not self.time[0]:
                self.al.pop(0)
                self.time.pop(0)
            return v

        else:
            return " "

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.al:
            return True
        return False


        # Your StringIterator object will be instantiated and called as such:
        # obj = StringIterator(compressedString)
        # param_1 = obj.next()
        # param_2 = obj.hasNext()