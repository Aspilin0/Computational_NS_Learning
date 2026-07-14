def euler(func, h=0.01, times=1000, x_n=0, y_n=0 ):
    terminal = x_n + h * times
    x_list, y_list = [], []    
    while x_n <= terminal:
        y_n += func(x_n, y_n) * h
        x_n += h
        x_list.append(x_n)
        y_list.append(y_n)
    return [x_list, y_list]

def RK4(func, h=0.01, times=1000, x_n=0, y_n=0 ):
    terminal = x_n + h * times
    x_list, y_list = [], []    
    while x_n <= terminal:
        k1 = func(x_n, y_n)
        k2 = func(x_n + h/2, y_n + k1 * h/2)
        k3 = func(x_n + h/2, y_n + k2 * h/2)
        k4 = func(x_n + h, y_n + h * k3)
        y_n += (k1 + 2*k2 + 2*k3 +k4) * h/6
        x_n += h
        x_list.append(x_n)
        y_list.append(y_n)
    return [x_list, y_list]

