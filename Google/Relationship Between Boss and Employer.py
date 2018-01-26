'''
通过函数构建层级图。第一个函数是set（雇员a，雇员b）意思是令ab为同一直接manager的下属。
第二个函数是set（雇员a 经理m）意思是令m成为a的直接上属。
还有一个get（a）是要求你返回从a往上所有的管理关系链直到顶层。
沟通了输入输出，刚开始有点误解，小哥说没有input，后来搞了半天input是一堆构建图的query，
就是set函数。相当于你一般构建图 一边根据已有的图返回管理链。自己定义了类，开始实现。

复杂的地方在：如果ab同级 bc同级 cd同级，这时候get a没有一个链可以返回。但是这时候设置d的直接经理是m 那么abc都要更新。

思路:
相当于构件图
用一个employee的类存储员工的经理和同事
'''
class Employee(object):
    def __init__(self,num):
        self.manager = None
        self.colleague = []
        self.number = num
class Relationship(object):
    def __init__(self):
        self.record = dict()
    def setM(self, e, m):
        if e not in self.record:
            self.record[e] = Employee(e)
        if m not in self.record:
            self.record[m] = Employee(m)
        self.record[e].manager = self.record[m]
        for v in self.record[e].colleague:
            self.record[v].manager = self.record[m]
    def setC(self,e1,e2):
        if e1 not in self.record:
            self.record[e1] = Employee(e1)
        if e2 not in self.record:
            self.record[e2] = Employee(e2)
        self.record[e1].colleague.append(self.record[e2])
        self.record[e2].colleague.append(self.record[e1])
    def get(self, e):
        ret = []
        if e in self.record:
            m = self.record[e]
            while m:
                ret.append(m.number)
                e,m = m,m.manager
            return ret
        else:
            return [e]