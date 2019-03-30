#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 条件判断
age = input('your age is：')
# 转换类型
age = int(age)

if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')


# 循环
# for in
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# 0~3
print(list(range(4)))

# while
index = 0
len = len(names)
while index < len:
    if index > 1:
        # 终止循环
        break

    if index > 1:
        # 跳出当前循环
        continue

    print(names[index])
    index = index + 1


# 函数
print(abs(-4), abs(8), abs(-0.38), abs(3.8e-6))
# max、min
# str、bool

def myAbs (x):
    # 参数检查
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x

print(myAbs(-4), myAbs(8), myAbs(-0.38), myAbs(3.8e-6))

# 空函数
# 或者条件判断过后加上 pass
def nop ():
    pass

import math
# 返回多个值
def move (x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    # 返回 tuple
    return nx, ny

# 类似解构
nx, ny = move(100, 100, 60, math.pi / 6)
print(nx, ny)
