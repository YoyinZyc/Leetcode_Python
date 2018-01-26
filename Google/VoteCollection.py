'''
实现一个票数统计器。String getLeader(Collection<Vote> votes, Long timeStamp) 方法。
其中Vote类有两个方法(String getLeader() 和 Long getTimeStamp())表示某一票是投给谁的，什么时候投的。
你要做的method是统计timeStamp之前所有的有效投票，把票数最高的参选人名字返回。

follow ups: 1.写一个 List<String> getTopKLeaders(Collections<Vote> votes, Long timeStamp, int k)
方法，返回某个时间点前统计出来的前k名最强领导人。

2.优化新函数时间复杂度。
这个再加一个priorityQueue<Map.Entry<>>就可以了, o(nlogn), o(n) ,
优化的话, 用buckets, 因为加入map时已经知道最大投票数,和最小投票数,
那么只要buckets[] = new buckets[max-min], 然后放入value-min对应的bucket. 这样可以减少到o(n)的时间复杂度

'''
class Vote(object):
    def __init__(self,leader, time):
        self.leader = leader
        self.time = time
    def getLeader(self):
        return self.leader
    def getTime(self):
        return self.time

def getTopKLeaders(votes, time):
    d = dict()
    for v in votes:
        if v.time <time:
            d[v.leader] = d.get(v.leader) + 1
    max_v = max(d.items())
    min_v = min(d.items())

    # 建bucket
    bucket = [[] for _ in range(max_v-min_v+1)]
    for k in d:
        v = d[k]
        bucket[v-min_v].append(k)
    ret = []
    for i in range(len(bucket)-1, -1, -1):
        v = bucket[i]
        if len(v)-k < 0:
            return ret+v
        else:
            k-=len(v)
            ret += v
    return ret