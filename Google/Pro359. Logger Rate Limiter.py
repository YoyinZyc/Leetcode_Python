'''
思路：
用map，
key是message
value是上一次打印的time

检查是不是>=10

'''
class Logger:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dict()

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """

        if message in self.d and timestamp - self.d[message] < 10:
            return False
        self.d[message] = timestamp
        return True



        # Your Logger object will be instantiated and called as such:
        # obj = Logger()
        # param_1 = obj.shouldPrintMessage(timestamp,message)