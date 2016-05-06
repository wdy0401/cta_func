# -*- coding: utf-8 -*-
"""
Created on Thu May  5 20:21:47 2016

@author: NUC
"""
import numpy as np
import matplotlib.pyplot as plt
'''
x = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])
y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])

z1 = np.polyfit(x, y, 1)
z2 = np.polyfit(x, y, 2)
z3 = np.polyfit(x, y, 3)
z4 = np.polyfit(x, y, 4)
z5 = np.polyfit(x, y, 5)
p1= np.poly1d(z1)
p2= np.poly1d(z2)
p3= np.poly1d(z3)
p4= np.poly1d(z4)
p5= np.poly1d(z5)
xp = np.linspace(-4, 10, 100)
plt.plot(x, y,'.', xp, p1(xp),'.', xp, p2(xp),'.', xp, p3(xp), '-', xp, p4(xp), '-', xp, p5(xp), '-')
plt.ylim(-5,5)
plt.savefig("e:\\12.png")
'''
a1=[]
a2=[]
ind1=0
ind2=0
now_a1=True
for i in range(100):
    if now_a1:
        a1.append(i)
        if len(a1)>4:
            a1.pop(0)
    else:
        a2.append(i)
        if len(a2)>4:
            a2.pop(0)
    now_a1=not now_a1
    print(a1)
    print(a2)
#plt.show()
'''
import sys
import math
import numpy
while True:
    line = sys.stdin.readline() # 一次只读一行
    if not line: # 如果是空行(^Z)就停止
        break
#    print(help(line))
    a = line.split() 
#    print(int(a[0]) + int(a[1])) # 否则回显，再回去读下一行
    line_int=[int(x) for x in a]
    cabs=[math.sqrt(x.real**2+x.imag**2) for x in list(numpy.fft.fft(line_int))]
    print(cabs)
    #print(np.fft.fft(line))

    关于使用函数逼近行情的看法
    1   使用fft
        1.1 无法看到趋势项
        1.2 低频项
            1.2.1   非趋势部分
            1.2.2   相位有意义（仅针对第i=1项）
        1.3 高频项
            1.3.1   噪音
            1.3.2   非趋势部分
            1.3.3   相位无意义
        1.4 对于多阶段，可以通过对比得到市场是否发生了变化
     2  使用多项式
        2.1 有趋势项
        2.2 病态矩阵问题
     3  使用正交多项式
        3.1 如何处理数据以便使用正交多项式
        3.2 可在一定程度上得到频域信息
    
    
    关于使用函数对成交量信息进行分析的看法
    1   日内数据
        1.1 通过成交分布判断
        1.2 通过成交量判断
    2   日数据
        2.1 与价格同样的方式
        
    
    通过比例或绝对值方式确定生效条件
    如何定义利用上述指标定义趋势开始与结束

'''