'''
Top_Interview_Medium
10.15 2:15pm
'''
import random
class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        if not self.origin:
            return []
        return self._shuffle_list(self.origin)

    def _shuffle_list(self, l):
        if len(l) == 1:
            return l
        ret = []
        random_i = random.randint(0, len(l) - 1)
        ret.append(l[random_i])
        if random_i == 0:
            ret += self._shuffle_list(l[1:])
        elif random_i == len(l) - 1:
            ret += self._shuffle_list(l[:len(l) - 1])
        else:
            ret += self._shuffle_list(l[0:random_i] + l[random_i + 1:])

        return ret


        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.reset()
        # param_2 = obj.shuffle()