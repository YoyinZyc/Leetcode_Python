'''
题意：
这道题需要理解题意
1) [“dog”]; isUnique(“dig”);
//False, because “dig” has the same abbreviation with “dog" and “dog” is already in the dictionary. It’s not unique.

2) [“dog”, “dog"]; isUnique(“dog”);
//True, because “dog” is the only word that has “d1g” abbreviation.
注意输入的重复

3) [“dog”, “dig”]; isUnique(“dog”);
//False, because if we have more than one word match to the same abbreviation, this abbreviation will never be unique.

思路：
构造一个dict
key：abbr
value：相对应的word，防止重复用set存储

'''
class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        # 构造dict
        self.d = dict()
        for i in range(len(dictionary)):
            if len(dictionary[i]) > 2:
                abbr = dictionary[i][0] + str(len(dictionary[i]) - 2) + dictionary[i][-1]
            else:
                abbr = dictionary[i]
            self.d[abbr] = self.d.get(abbr, set())
            self.d[abbr].add(dictionary[i])

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # 找到输入word的abbr
        if len(word) > 2:
            abbr = word[0] + str(len(word) - 2) + word[-1]
        else:
            abbr = word
        # 如果不存在这个key，直接返回True
        if self.d.get(abbr, []):
            l = list(self.d[abbr])
            # 如果value的个数大于1，返回False
            if len(self.d[abbr]) > 1:
                return False
            # 如果value有一个但不是word，返回False
            elif l[0] != word:
                return False
        return True


        # Your ValidWordAbbr object will be instantiated and called as such:
        # obj = ValidWordAbbr(dictionary)
        # param_1 = obj.isUnique(word)