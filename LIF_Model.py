import numpy as np
import matplotlib.pyplot as plt

#常量引入
C = 0.5
E = -70
G = 0.025

#变量引入
i_e = 10.0
t = 0.0
h = 0.01
length = 50.0
v = -65.0
t_last = -1.0
flag = True
v_list, t_list = [v], [t]

#方程表达
def fun_lif(V):
    return  (i_e - (V - E) * G) / C

#激活
def lif_generator(V, t):
    global t_last
    if t >= t_last:    
        if -30.0 <= V : #threshold
            V = 60.0
            t_last = t +0.2
            

        elif 0.0 <= V:      #reset
            V = -65.0
        else:
            pass
    else:
        V = -65
    return V

#计算部分
while t <= length:
    v += fun_lif(v) * h
    v = lif_generator(v,t)
    t += h
    v_list.append(v)
    t_list.append(t)

plt.plot(t_list, v_list)
plt.show()
    


