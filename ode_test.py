


import ode_solver as os
import matplotlib.pyplot as plt

def test_func(x,y = 0):
    return x ** 2

result_e = os.euler(test_func,h=10)
result_r = os.RK4(test_func,h=10)  
plt.plot(result_e[0], result_e[1],color = "red")
plt.plot(result_r[0], result_r[1],color = "blue")
plt.show()






