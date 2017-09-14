'''
Greedy_Medium
9.12 11:16am
'''


class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        record = []
        nums.insert(0,float('nan') )
        j = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:

                if nums[i]-nums[i-1] > 1:
                    print (record)
                    if all(not c < 3 for c in record):
                        record = []
                    else:
                        return False
                else:
                    temp = j
                    while j < len(record):
                        if record[j] < 3:
                            return  False
                        j+=1
                    record = record[:temp]
                j = 0
                if record:
                    record[j] += 1
                else:
                    record.append(1)
                j+=1
            else:
                if j >= len(record):
                    record.insert(0, 1)
                else:
                    record[j] += 1
                j+=1

        return all(not c < 3 for c in record)