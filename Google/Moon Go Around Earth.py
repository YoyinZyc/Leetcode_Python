'''
题意：
第一轮是设计题，给你函数 int timerID = startTimer(int millseconds, Runnable run); cancelTimer(int timerID);
还有一个class sprite 有draw(int x, int y) function，功能是在一个画板上让你在x y这个坐标画出这个sprite
要求让你实现一个单线程animation画板，画板大小1024x1024，要求你在（512，512）处画一个地球，然后画一个月球，月球每五秒绕着地球转一圈，轨道半径是125。
要实现的function有
start(){}
stop(){}
draw(){}

http://www.1point3acres.com/bbs/thread-312677-1-1.html
'''
import threading
import time
import math
exitFlag = 0


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print("Starting " + self.name)
        start(self.name, self.counter, (512,512+125))
        print("Exiting " + self.name)

loc = (512,512+125)
def start(threadName, delay, loc):
    start_time = time.time()
    while True:
        # 打印点
        print(loc)
        # delay的时间，每隔多久打印一个点
        time.sleep(delay)
        now = time.time()
        # 计算路径
        x = 512 + math.cos((now-start_time)/5 * 2 * math.pi)*125
        y = 512+125 + math.sin((now-start_time)/5 * 2 * math.pi)*125
        loc = (y,x)
    # print(loc)



# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)

# 开启线程
thread1.start()
# thread2.start()

print
"Exiting Main Thread"