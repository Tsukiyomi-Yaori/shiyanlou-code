#!/usr/bin/env python3
import sys
# 转换时间
def Hours(minute):
    # 如果负数，则 raise 异常
    if minute < 0:
        raise ValueError("Parameter Error")
    else:
        print("{} H, {} M".format(int(minute / 60),minute % 60))

# 函数调用及异常处理
try:
    Hours(int(sys.argv[1]))
except:
    print("Parameter Error")
