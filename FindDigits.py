#!/usr/bin/env python3
# 打开并读取文件里的字符串
with open('/tmp/String.txt') as fobj:
        s = fobj.read()
res = ""

# 循环字符串里的每一个字符，判断是否为数字
for char in s:
    if char.isdigit():
        res += char
print(res)
