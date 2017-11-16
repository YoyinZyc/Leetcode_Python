def sort(l):
    digL = len(str(max(l)))
    # bucket = [[] for _ in range(10)]
    for i in range(digL):
        bucket = [[] for _ in range(10)]
        for v in l:
            bucket[int ((v / (10 ** i)) % 10)].append(v)
        l = []
        for v in bucket:
            l += v
    print(l)
    return l
# def sort(l, N):
#     for i in range(3,-1,-1):
#         bucket = [[] for _ in range(N)]
#         for v in l:
#             bucket[int (v[i])].append(v)
#         l = []
#         for v in bucket:
#             l+=v
#     return l
