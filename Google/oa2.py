class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.neighbor = []


def solution(A, E):
    # write your code in Python 3.6
    if not A:
        return 0
    nodes = [TreeNode(v) for v in A]

    def same_value_path(node, val):
        if node.val == val:
            same_sub = 0
            for n in node.neighbor:
                same_sub = max(same_sub, same_value_path(n, val))
            return same_sub + 1
        else:
            return 0

    def longest_path(node):
        sub = 0
        for n in node.neighbor:
            sub = max(sub, longest_path(n))
        same_sub = 0
        for n in node.neighbor:
            same_sub += same_value_path(n, node.val)
        return max(same_sub, sub)

    store = [n for n in nodes]
    i = 0
    while i < len(E):
        n1 = nodes[E[i] - 1]
        n2 = nodes[E[i + 1] - 1]
        if n2 not in store:
            n2.neighbor.append(n1)
            store.pop(n1)
        elif n1 not in store:
            n1.neighbor.append(n2)
            store.pop(n2)
        else:
            n1.neighbor.append(n2)
            store.pop(n2)
        i += 2
    return longest_path(store[0])

if __name__ == '__main__':
    solution([1,1,1,2,2],[1,2,3,1,2,4,2,5])