class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        ret = 1
        for v in b:
            ret = ((ret ** 10) % 1337 * (a ** v) % 1337) % 1337
        return ret
