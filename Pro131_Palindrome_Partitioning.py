'''
Backtracking_Medium
9.11 10:04pm
'''
import copy
class Solution(object):
    def partition(self, s):
    	lists=[]
    	l=[]
    	self.helper(lists,l,s)
    	return lists

    def helper(self, lists, l, remainString):
    	if remainString == "":
    		lists.append(l)
    		return 1
    	for i in range(1,len(remainString)+1):
    		if self.isPalindrome(remainString[0:i]):
    			lc = copy.deepcopy(l)
    			lc.append(remainString[0:i])
    			self.helper(lists, lc, remainString[i:])


    def isPalindrome(self, s):
    	i = 0
    	j = len(s)-1
    	while i <= j:
    		if s[i] != s[j]:
    			return False
    		i+=1
    		j-=1
    	return True
