## 微分方程的数值解
* 隐式法：方程两端均有$y_{n+1}$
* 显式法：可直接计算

### Euler法
grid...

### 改进Euler法

$$
\left\{ \begin{array}{ll} \widetilde{y}_{k+1} = y_k + h*f(x_k , y_k) \\y_{k+1} = y_k +\frac{h}{2}[f(x_k,y_k)+f(x_{k+1} , \widetilde{y}_{k+1})] \end{array} \right.
$$

简单来说就是估计+校正

### **Runger-Kutta法(R-K法)**
用Talyor展开的前n项来估计
$$
\left\{ \begin{array}{ll} y_{n+1} = y_n + \frac{h}{6}(K_1+2K_2+2K_3+K_4)\\K_1 =f(x_n,y_n) \\ K_2=f(x_n+\frac{h}{2},y_n+\frac{h}{2}K_1) \\K_3=f(x_n+\frac{h}{2},y_n+\frac{h}{2}K_2)\\K_4=f(x_n+h,y_n+hK_3) \end{array} \right.
$$

### Adams 线性逼近
$$y(x_{n+1})=y(x_n) + \int_{x_{n}}^{x_{n+1}}f(x,y)dx$$
用插值法算出f(x ,y)后计算
同理可以使用改进法






