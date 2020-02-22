import sys


def func_a():
    a = 3
    f = sys._getframe()
    func_b()  # 第一次调用
    func_b()  # 第二次调用

def func_b():
    f = sys._getframe()  # 获得调用栈
    f_back = f.f_back    # 获取上一帧的信息，这里存储的就是调用func_b 的函数的信息
    print(f_back.f_locals)


def func_c():
    func_b()

func_a()