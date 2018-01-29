'''
题意：
需要思考这个题

给了一个rows*cols的屏幕和一个句子，要求找到如果把这个屏幕填满需要几个句子，要求句子每个词之间要空格，句子之间也要空格
思路：
3种case
Case 1:
“AB-CDE-F-….-YZ” (‘-’ denotes a space)
reach to the space before F

Case 2:
“AB-CDE-F-…._YZ” (‘-’ denotes a space)
reach to exactly E

Case 3:
“AB-CDE-F-….-YZ” (‘-’ denotes a space)
reach to D
case 1, I can count one more bit and go to next line
case 2, I can count two more bits and go to next line
case 3, I have to move the cursor back until it reach to some space, and go to next line
'''
class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        # 把sentence用' '连起来
        s = ' '.join(sentence) + ' '
        start = 0
        for i in range(rows):
            # 加上一行的长度
            start += cols - 1
            # 如果这一行最后一列对应的是' ': start+1 case1
            if s[start % len(s)] == ' ':
                start += 1
            # 如果这一行最后一列的下一个对应的是' ':start+2  case2
            elif s[(start + 1) % len(s)] == ' ':
                start += 2
            # 如果都不是，则说明最后一列对应的是在一个单词的中间，需要go back找到前一个空格    case3
            else:
                while start > 0 and s[ (start - 1) % len(s) ] != ' ':
                    start -= 1
        return start/ len(s)
if __name__ == '__main__':
    s = Solution()
    s.wordsTyping(["hello","world"],2,8)