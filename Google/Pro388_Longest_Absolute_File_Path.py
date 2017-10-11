'''
Google_Medium
10.9 7:34pm
'''
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        input_l = input.split('\n')
        record = [0]
        self.helper(0, 0, input_l, 0, record)
        return record[0]

    def helper(self, length, i, input_l, level, record):

        while i < len(input_l):
            v = input_l[i]
            level_v = v.count('\t')
            len_v = len(v) - level_v + 1
            if level_v == level:
                if '.' in v:
                    record[0] = max(record[0], length + len_v - 1)
                    i += 1
                else:
                    i = self.helper(len_v + length, i + 1, input_l, level_v + 1, record)
            else:
                break
        return i