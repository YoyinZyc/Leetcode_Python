'''
Facebook_Medium
11.06 8:19pm
'''
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.helper('', s, ans, 0)
        return ans

    def helper(self, ip, s, ans, section_no):

        if section_no == 4:
            if not s:
                ans.append(ip[1:])
            return
        if len(s) > 0:
            self.helper(ip + '.' + s[0], s[1:], ans, section_no + 1)
        if len(s) > 1 and int(s[:2]) >= 10:
            self.helper(ip + '.' + s[:2], s[2:], ans, section_no + 1)
        if len(s) > 2 and int(s[:3]) <= 255 and int(s[:3]) >= 100:
            self.helper(ip + '.' + s[:3], s[3:], ans, section_no + 1)
