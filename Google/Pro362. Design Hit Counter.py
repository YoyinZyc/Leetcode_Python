'''
看过去5min内发生过多少hit

思路：
binary search
'''
class HitCounter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.record = []

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.record.append(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        # 找到开始的时间，不包括
        time = timestamp - 300
        # 如果小于0，怎返回record的长度
        if time <= 0:
            return len(self.record)
        # 通过bs找到该时间点是介于哪两个时间之间的，上届肯定比改时间大
        begin = 0
        end = len(self.record) - 1
        while begin <= end:
            mid = (begin + end) // 2
            if self.record[mid] <= time:
                begin = mid + 1
            else:
                end = mid - 1
        # begin是上届，end是下届，减去begin
        return len(self.record) - begin


        # Your HitCounter object will be instantiated and called as such:
        # obj = HitCounter()
        # obj.hit(timestamp)
        # param_2 = obj.getHits(timestamp)