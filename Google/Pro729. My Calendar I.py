'''
题意：
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation:
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.

思路：
可以用bst；省时间
'''
class MyCalendar(object):
    def __init__(self):
        self.record = [[0, 10 ** 9]]

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i in range(len(self.record)):
            v = self.record[i]
            if start >= v[0] and start <= v[1]:
                if end - 1 <= v[1]:
                    self.record.pop(i)
                    if start != v[0] and end - 1 != v[1]:
                        self.record.insert(i, [v[0], start - 1])
                        self.record.insert(i + 1, [end, v[1]])
                    elif start != v[0]:
                        self.record.insert(i, [v[0], start - 1])
                    elif end - 1 != v[1]:
                        self.record.insert(i, [end, v[1]])
                    return True
        return False



        # Your MyCalendar object will be instantiated and called as such:
        # obj = MyCalendar()
        # param_1 = obj.book(start,end)