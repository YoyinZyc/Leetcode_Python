def median(A, B):
    # A和B的长度
    m, n = len(A), len(B)
    # 如果 A比B长，交换AB，保证j大于0
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError
    # 中位数左边的长度，可以包括中位数
    imin, imax, half_len = 0, m, (m + n + 1) // 2
    while imin <= imax:
        # 将A砍半
        i = (imin + imax) // 2
        # 获得对应的在B的坐标，是的A的left和B的left长度加起来是一半
        j = half_len - i
        # 如果是B的left的最后一个值大于A的right的第一个值，说明要右移
        if i < m and B[j - 1] > A[i]:
            # i is too small, must increase it
            imin = i + 1
        # 否则左移
        elif i > 0 and A[i - 1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect
            # 找到left的最大值
            if i == 0:
                max_of_left = B[j - 1]
            elif j == 0:
                max_of_left = A[i - 1]
            else:
                max_of_left = max(A[i - 1], B[j - 1])
            # 如果m和n加起来是奇数，返回这个max_of_left
            if (m + n) % 2 == 1:
                return max_of_left
            # 找到right的最小值
            if i == m:
                min_of_right = B[j]
            elif j == n:
                min_of_right = A[i]
            else:
                min_of_right = min(A[i], B[j])
            # 返回
            return (max_of_left + min_of_right) / 2.0