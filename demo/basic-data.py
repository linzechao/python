#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第一行加上一个特殊的注释，可以直接运行 .py 文件
# 第二行为字符编码

# 1024
print('2 ** 10 =', 2 **10)

# string
# 空格连接字符串
print('Hello', 'Super', '!!!')

# 输入
name = input('please enter your name: ')
print('Hello', name)

# 全转码
print(r'\\\\t\\')

# 多行，自动带上 \n
print('''line1
line2
line3''')


# 整型
# 4、86
# 整除 10 // 3 === 3


# 浮点型
# 3.14 1.2e4 4.8e-8


# 布尔值
# True、False
# 运算符
# and、or、not


# 空值
# None


# 格式化
# %s 是万能的，将自动转换
# %% 表示 %
print('亲爱的 ' + name + '，您好！您%s月份的话费是 %f，余额是 %f' % ('四', 25.4, 4734.13))
# format()：可设置精度
print('亲爱的 ' + name + '，您好！您{0}月份的话费是 {1:.2f}，余额是 {2:.2f}'.format('四', 25.4, 4734.13))


# 列表（list）
classmates = ['Michael', 'Bob', 'Tracy']
# 最后一个元素
classmates.append('Adam')
classmates.insert(2, 'Jack')
# 删除
classmates.pop()
classmates.pop(0)
print(len(classmates))
print(classmates[-1])
print(classmates)


# 元组（tuple）
# 初始化之后不能修改
classmates = ('Michael', 'Bob', 'Tracy')


# 字典（dict）
dictionary = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
dictionary.pop('Bob')
print(dictionary)
print('Bob' in dictionary)


# 集合（set）
# key 集合，不保存 value
# 不重复
s = set(list(range(4)))
s.add(4)
s.remove(2)
print(s)
