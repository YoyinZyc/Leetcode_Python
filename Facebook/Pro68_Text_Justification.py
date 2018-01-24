class Solution(object):
    def fullJustify(self, words, maxWidth):
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                # 对于每一个需要添加的空格
                for i in range(maxWidth - num_of_letters):
                    # 利用余数决定需要添加到那个单词后面
                    cur[i%(len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]
if __name__ == '__main__':
    s = Solution()
    print(s.fullJustify(["This", "is", "an", "example", "of", "text", "justif.", 'qwe'], 16))
    if node:
        l.append(node.val)
        if flag:
            # left->right
            q2.append(node.left)
            q1.append(node,right)
            flag = False
        else:
            # right->left
            q2.insert(0, node.left)
            q2.in
            flag = True