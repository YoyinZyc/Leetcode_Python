from queue import PriorityQueue


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
        i = 0
        j = 0
        m = 0
        ret = []
        q = PriorityQueue()
        s = set()
        s.add((i, j))
        q.put((nums1[i] + nums2[j], (i, j)))
        while q and m < k:
            # print(q.get())
            (_, (i, j)) = q.get()
            ret.append([nums1[i], nums2[j]])
            m += 1
            if i + 1 == len(nums1) and j + 1 == len(nums2):
                break
            elif i + 1 == len(nums1):
                if (i, j + 1) not in s:
                    q.put((nums1[i] + nums2[j + 1], (i, j + 1)))
                    s.add((i, j + 1))
            elif j + 1 == len(nums2):
                if (i + 1, j) not in s:
                    q.put((nums1[i + 1] + nums2[j], (i + 1, j)))
                    s.add((i + 1, j))
            else:
                if (i, j + 1) not in s:
                    q.put((nums1[i] + nums2[j + 1], (i, j + 1)))
                    s.add((i, j + 1))
                if (i + 1, j) not in s:
                    q.put((nums1[i + 1] + nums2[j], (i + 1, j)))
                    s.add((i + 1, j))
                if (i + 1, j + 1) not in s:
                    q.put((nums1[i + 1] + nums2[j + 1], (i + 1, j + 1)))
                    s.add((i + 1, j + 1))

        return ret

