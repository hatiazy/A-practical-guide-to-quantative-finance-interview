[TOC]

---

# 3.1 极限与导数 (Limits and Derivatives)

## 题 1：复杂函数的导数 (Derivative of complex function)

### 题目描述
求函数 $y = \ln(x^{\ln x})$ 的导数。

### 解答
这是一道考察基础求导法则（链式法则和乘积法则）的经典题。对于含有指数幂的函数，取对数求导（Logarithmic differentiation）是最稳妥的方法。
具体步骤：
1. 设 $u = \ln y$。将原函数代入并利用对数性质化简：

$$
u = \ln(\ln(x^{\ln x})) = \ln(\ln x \cdot \ln x) = \ln((\ln x)^2) = 2 \ln(\ln x)
$$

2. 两边对 $x$ 求导。左边应用链式法则：

$$
\frac{du}{dx} = \frac{1}{y} \frac{dy}{dx}
$$

3. 右边同样应用链式法则：

$$
\frac{du}{dx} = 2 \cdot \frac{1}{\ln x} \cdot \frac{d(\ln x)}{dx} = \frac{2}{x \ln x}
$$

4. 将左右两边结合，解出 $\frac{dy}{dx}$：

$$
\frac{dy}{dx} = y \cdot \frac{2}{x \ln x} = \frac{2 \ln(x^{\ln x})}{x \ln x}
$$

### 核心知识点与拓展
* **知识点**：链式法则、对数求导技巧。
* **量化拓展**：在量化开发中，遇到形如 $f(x)^{g(x)}$ 的极大或极小数值运算（例如极大似然估计 MLE 中的连乘），将其映射到对数空间（Log-space）不仅是为了方便求导，更是保证工程数值稳定性、防止浮点数溢出 (Overflow) 的标准操作。

---

## 题 2：大小比较 (Maximum and minimum)

### 题目描述
在不计算具体数值的情况下，请问 $e^\pi$ 和 $\pi^e$ 哪个数字更大？

### 解答
**结论：$e^\pi > \pi^e$**

具体步骤：
1. 对两个数同时取自然对数。左边变为 $\pi \ln e$，右边变为 $e \ln \pi$。
2. 要比较 $\pi \ln e$ 和 $e \ln \pi$ 的大小，等价于比较 $\frac{\ln e}{e}$ 和 $\frac{\ln \pi}{\pi}$ 的大小。
3. 构造函数：

$$
f(x) = \frac{\ln x}{x}
$$

4. 对该函数求一阶导数：

$$
f'(x) = \frac{\frac{1}{x} \cdot x - \ln x \cdot 1}{x^2} = \frac{1 - \ln x}{x^2}
$$

5. 令 $f'(x) = 0$，解得唯一极值点 $x = e$。当 $x > e$ 时，$f'(x) < 0$，函数单调递减。
6. 因此，$f(x)$ 在 $x=e$ 处取得全局最大值。因为 $\pi > e$，所以 $f(e) > f(\pi)$，即 $\frac{\ln e}{e} > \frac{\ln \pi}{\pi}$。还原后即得 $e^\pi > \pi^e$。

### 核心知识点与拓展
* **知识点**：一阶导数与函数单调性极值的关系。
* **量化拓展**：这是极高频的笔试题。面试官可能会顺势追问“请用泰勒展开证明”。你可以利用 $e^x > 1+x$ （对于 $\forall x > 0$）的性质，令 $x = \frac{\pi}{e} - 1$，代入即可优雅秒杀。

---

## 题 3：洛必达法则 (L'Hospital's rule)

### 题目描述
请分别求出以下两个极限：当 $x \to \infty$ 时，$\frac{e^x}{x^2}$ 的极限；当 $x \to 0^+$ 时，$x^2 \ln x$ 的极限。

### 解答
具体步骤：
**极限 1：**
由于分子分母都趋于无穷大，直接连续应用两次洛必达法则：

$$
\lim_{x \to \infty} \frac{e^x}{x^2} = \lim_{x \to \infty} \frac{e^x}{2x} = \lim_{x \to \infty} \frac{e^x}{2} = \infty
$$

**极限 2：**
这不是标准的洛必达格式，需要通过代数变形将其转换为 $\frac{\infty}{\infty}$ 型。将 $x^2$ 放到分母的倒数位置：

$$
\lim_{x \to 0^+} x^2 \ln x = \lim_{x \to 0^+} \frac{\ln x}{x^{-2}}
$$

此时应用洛必达法则：

$$
\lim_{x \to 0^+} \frac{\frac{1}{x}}{-2x^{-3}} = \lim_{x \to 0^+} \frac{x^2}{-2} = 0
$$

### 核心知识点与拓展
* **知识点**：洛必达法则、不定型极限的代数转换。
* **量化拓展**：这道题背后隐藏着算法复杂度分析的底层逻辑。极限 1 证明了指数函数的增长速度永远碾压多项式；极限 2 则在推导带权重的对数时间复杂度（如熵或信息增益计算）收敛性时非常关键。

---

# 3.2 积分 (Integration)

## 题 4：基础积分运算 (Basics of integration)

### 题目描述
1. 求 $\ln(x)$ 的不定积分。
2. 求 $\sec(x)$ 在 $x=0$ 到 $x=\pi/6$ 上的定积分。

### 解答
**问题 1（分部积分法）：**
令 $u = \ln x$， $dv = dx$。则 $du = \frac{1}{x} dx$，$v = x$。
根据分部积分公式 $\int u dv = uv - \int v du$：

$$
\int \ln x dx = x \ln x - \int x \cdot \frac{1}{x} dx = x \ln x - x + C
$$

**问题 2（三角函数积分技巧）：**
$\sec x$ 的积分需要一个巧妙的代数技巧，分子分母同乘 $(\sec x + \tan x)$：

$$
\int \frac{\sec x (\sec x + \tan x)}{\sec x + \tan x} dx = \int \frac{\sec^2 x + \sec x \tan x}{\sec x + \tan x} dx
$$

分子的多项式恰好是分母的导数。所以不定积分为 $\ln|\sec x + \tan x| + C$。
代入上下限：

$$
\int_{0}^{\pi/6} \sec x dx = \ln(\sec(\frac{\pi}{6}) + \tan(\frac{\pi}{6})) - \ln(\sec(0) + \tan(0)) = \ln(\sqrt{3})
$$

### 核心知识点与拓展
* **量化拓展**：遇到没有解析解的积分时，作为 Quant 你需要能迅速提出数值积分方案，如梯形法则、辛普森法则，以及蒙特卡洛积分的思想。

---

## 题 5：圆柱体相交体积 (Intersecting cylinders)

### 题目描述
假设有两个半径均为 $r=1$ 的圆柱体，以完美的直角相互相交，并且它们的中心轴也相交。求这两个圆柱体相交部分的总体积。

### 解答
这是一个经典的 3D 几何体积积分问题（牟合方盖问题）。
具体步骤：
1. 观察横切面：用一个垂直于 $Z$ 轴的水平面在高度 $z$ 处横切。该切面在 $X$ 轴和 $Y$ 轴方向上截出的宽度均为 $2\sqrt{r^2 - z^2}$。
2. 因此，这个横切面是一个完美的正方形。切面面积 $A(z)$ 为：

$$
A(z) = (2\sqrt{r^2 - z^2})^2 = 4(r^2 - z^2)
$$

3. 对高度 $z$ 从 $-r$ 到 $r$ 进行积分（利用对称性，取 $0$ 到 $r$ 积分的两倍）：

$$
V = 2 \int_{0}^{r} 4(r^2 - z^2) dz = 8 \left[ r^2 z - \frac{z^3}{3} \right]_{0}^{r} = \frac{16}{3} r^3
$$

代入 $r=1$，总体积为 $16/3$。

---

## 题 6：扫雪车问题 (Snow plow problem)

### 题目描述
正午前的一段时间开始下雪，降雪速率恒定。剑桥市在正午 (12:00) 派出一辆扫雪车，其排雪的体积速率恒定。
下午 1:00，扫雪车前进了 2 英里；下午 2:00，共前进了 3 英里。问：雪具体是几点开始下的？

### 解答
具体步骤：
1. 设 $t=0$ 为正午 12:00，雪在正午前 $T$ 小时开始下。街道上雪的横截面积 $A(t)$ 与累积下雪的时间成正比：$A(t) = c_2 (t + T)$。
2. 扫雪车的推进速度 $v(t)$ 与前方面积成反比：

$$
v(t) = \frac{dx}{dt} = \frac{c_1}{A(t)} = \frac{c}{t+T} \quad (c = c_1/c_2)
$$

3. 积分得到位移方程：

$$
x(t) = \int_{0}^{t} \frac{c}{\tau+T} d\tau = c \ln(\frac{t+T}{T})
$$

4. 代入条件 $x(1) = 2$ 和 $x(2) = 3$：

$$
c \ln(\frac{1+T}{T}) = 2, \quad c \ln(\frac{2+T}{T}) = 3
$$

5. 消去常数 $c$，得到 $(\frac{1+T}{T})^3 = (\frac{2+T}{T})^2$。
化简得到 $T^2 - T - 1 = 0$。解得 $T = \frac{\sqrt{5}-1}{2} \approx 0.618$ 小时。即约 11:23 AM 开始下雪。

### 核心知识点与拓展
* **量化拓展**：常微分方程建模。掌握基于守恒定律（体积守恒、资金流守恒）建立 ODE 是进阶量化研究的核心素质。

---

## 题 7：利用积分求正态分布期望 (Expected value using integration)

### 题目描述
如果 $X$ 服从标准正态分布 $X \sim N(0,1)$，求在给定 $X > 0$ 条件下，$X$ 的条件期望 $E[X | X > 0]$。

### 解答
具体步骤：
1. 求条件期望，根据定义：

$$
E[X | X > 0] = \frac{\int_{0}^{\infty} x f(x) dx}{P(X > 0)}
$$

2. 计算分子（部分期望）：

$$
\int_{0}^{\infty} x \frac{1}{\sqrt{2\pi}} e^{-x^2/2} dx
$$

利用换元法，令 $u = -x^2/2$，则 $du = -x dx$：

$$
\int_{0}^{-\infty} -\frac{1}{\sqrt{2\pi}} e^u du = -\frac{1}{\sqrt{2\pi}} (0 - 1) = \frac{1}{\sqrt{2\pi}}
$$

3. 计算分母，标准正态分布是对称的，$P(X > 0) = \frac{1}{2}$。
4. 得出最终的条件期望：

$$
E[X | X > 0] = \frac{\frac{1}{\sqrt{2\pi}}}{\frac{1}{2}} = \sqrt{\frac{2}{\pi}}
$$

---

# 3.3 偏导数与多重积分 (Partial Derivatives and Multiple Integrals)

## 题 8：高斯积分 (Gaussian Integral)

### 题目描述
计算反常积分 $\int_0^\infty e^{-x^2/2} dx$。

### 解答
不能使用基本初等函数直接求原函数，必须利用极坐标变换 (Polar Coordinates) 求解。
具体步骤：
1. 设该积分的值为 $I$。则 $I^2$ 可以写成两个独立变量 $x$ 和 $y$ 的二维积分：

$$
I^2 = \int_0^\infty e^{-x^2/2} dx \int_0^\infty e^{-y^2/2} dy = \int_0^\infty \int_0^\infty e^{-(x^2+y^2)/2} dx dy
$$

2. 积分区域为第一象限。引入极坐标变换：$x = r \cos\theta$, $y = r \sin\theta$。此时 $x^2 + y^2 = r^2$，且面积微元 $dx dy = r dr d\theta$。
3. 将积分转换为极坐标系：

$$
I^2 = \int_0^{\pi/2} \int_0^\infty e^{-r^2/2} r dr d\theta
$$

4. 内层关于 $r$ 的积分很容易求出：$\int_0^\infty e^{-r^2/2} r dr = 1$。
5. 外层积分变为 $\int_0^{\pi/2} 1 d\theta = \frac{\pi}{2}$。
6. 因此 $I^2 = \frac{\pi}{2}$，解得 $I = \sqrt{\frac{\pi}{2}}$。

---

# 3.4 重要微积分方法 (Important Calculus Methods)

## 题 9：复数的虚数次幂 (Taylor's series)

### 题目描述
求 $i^i$ 的值。

### 解答
这需要用到由泰勒展开推导出的最美公式——欧拉公式 (Euler's formula)。
具体步骤：
1. 欧拉公式指出对于任意实数 $\theta$：$e^{i\theta} = \cos\theta + i\sin\theta$。
2. 当 $\theta = \pi/2$ 时，$e^{i\pi/2} = \cos(\pi/2) + i\sin(\pi/2) = i$。
3. 对两边取自然对数，得到 $\ln i = i\pi/2$。
4. 要求 $i^i$，我们先求它的自然对数：

$$
\ln(i^i) = i \ln i = i \cdot (i\frac{\pi}{2}) = i^2 \frac{\pi}{2} = -\frac{\pi}{2}
$$

5. 两边取指数，还原得到：

$$
i^i = e^{-\pi/2}
$$

可见，一个虚数的虚数次幂竟然是一个纯实数。

---

## 题 10：伯努利不等式 (Bernoulli's Inequality)

### 题目描述
证明对于所有 $x > -1$ 和所有整数 $n \ge 2$，有 $(1+x)^n \ge 1+nx$。

### 解答
可以通过泰勒展开或数学归纳法证明。这里提供归纳法：
具体步骤：
1. **基础情况**：当 $n=2$ 时，$(1+x)^2 = 1+2x+x^2$。因为 $x^2 \ge 0$，所以 $1+2x+x^2 \ge 1+2x$ 成立。
2. **归纳假设**：假设当 $n=k$ 时不等式成立，即 $(1+x)^k \ge 1+kx$。
3. **归纳步**：证明 $n=k+1$ 时也成立。因为 $x > -1$，所以 $(1+x) > 0$，我们可以在假设的两边同乘 $(1+x)$：

$$
(1+x)^{k+1} \ge (1+kx)(1+x) = 1 + x + kx + kx^2 = 1 + (k+1)x + kx^2
$$

4. 因为 $kx^2 \ge 0$，所以 $1 + (k+1)x + kx^2 \ge 1 + (k+1)x$。证明完毕。

---

## 题 11：牛顿迭代法 (Newton's method)

### 题目描述
估算 $\sqrt{37}$ 的值，精确到小数点后第三位。

### 解答
此题考察如何通过数值算法求解方程 $f(x) = x^2 - 37 = 0$ 的根。
具体步骤：
1. 设定初始猜测值：显然 36 的平方根是 6，所以设 $x_0 = 6$。
2. 应用牛顿迭代公式：$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$。
3. 计算一阶导数：$f'(x) = 2x$。
4. 进行第一次迭代：

$$
x_1 = 6 - \frac{6^2 - 37}{2 \times 6} = 6 - \frac{-1}{12} = 6 + 0.0833 = 6.083
$$

$6.083^2 = 37.00289$，已经极度逼近 37。答案为 6.083。

### 核心知识点与拓展
* **量化拓展**：在隐含波动率 (Implied Volatility) 的计算中，由于 Black-Scholes 公式没有解析逆解，通常都是使用牛顿迭代法或割线法通过期权市场价格反推波动率的。

---

## 题 12：点到平面的距离 (Lagrange multipliers)

### 题目描述
求原点 $(0,0,0)$ 到平面 $2x + 3y + 4z = 12$ 的最短距离。

### 解答
这是一个带约束的极值问题，完美契合拉格朗日乘数法。
具体步骤：
1. 目标是最小化原点到平面上点的距离的平方：$f(x,y,z) = x^2 + y^2 + z^2$。
2. 约束条件为：$g(x,y,z) = 2x + 3y + 4z - 12 = 0$。
3. 建立拉格朗日方程的偏导数系统：

$$
\frac{\partial f}{\partial x} + \lambda \frac{\partial g}{\partial x} = 2x + 2\lambda = 0 \Rightarrow x = -\lambda
$$

$$
\frac{\partial f}{\partial y} + \lambda \frac{\partial g}{\partial y} = 2y + 3\lambda = 0 \Rightarrow y = -\frac{3}{2}\lambda
$$

$$
\frac{\partial f}{\partial z} + \lambda \frac{\partial g}{\partial z} = 2z + 4\lambda = 0 \Rightarrow z = -2\lambda
$$

4. 将 $x, y, z$ 代入约束平面方程：

$$
2(-\lambda) + 3(-\frac{3}{2}\lambda) + 4(-2\lambda) = 12 \Rightarrow -\frac{29}{2}\lambda = 12 \Rightarrow \lambda = -\frac{24}{29}
$$

5. 解出坐标 $(x,y,z)$ 分别为 $(24/29, 36/29, 48/29)$。
6. 计算距离 $D = \sqrt{x^2+y^2+z^2} = \frac{12}{\sqrt{29}}$。

---

# 3.5 常微分方程 (Ordinary Differential Equations)

## 题 13：可分离变量的微分方程 I

### 题目描述
求解常微分方程 $y' + 6xy = 0$，初始条件 $y(0)=1$。

### 解答
这是最基础的可分离变量 ODE。
具体步骤：
1. 移项并分离变量：$\frac{dy}{dx} = -6xy \Rightarrow \frac{dy}{y} = -6x dx$。
2. 两边同时积分：$\int \frac{1}{y} dy = \int -6x dx \Rightarrow \ln y = -3x^2 + C$。
3. 取指数：$y = e^{-3x^2+C} = K e^{-3x^2}$。
4. 代入初始条件 $y(0)=1$，得到 $K=1$。最终解为 $y = e^{-3x^2}$。

---

## 题 14：可分离变量的微分方程 II (变量代换)

### 题目描述
求解常微分方程 $y' = \frac{x-y}{x+y}$。

### 解答
方程本身不可直接分离，需要利用变量代换降维。
具体步骤：
1. 引入新变量 $z = x+y$，则 $y = z-x$，求导得 $y' = \frac{dz}{dx} - 1$。
2. 代入原方程：

$$
\frac{dz}{dx} - 1 = \frac{x - (z-x)}{z} = \frac{2x - z}{z} = \frac{2x}{z} - 1
$$

3. 化简得 $\frac{dz}{dx} = \frac{2x}{z}$。此时变量已可分离。
4. 分离变量并积分：$z dz = 2x dx \Rightarrow \int z dz = \int 2x dx \Rightarrow \frac{z^2}{2} = x^2 + C$。
5. 还原变量 $z$：$(x+y)^2 = 2x^2 + 2C$。展开化简即得隐式解 $y^2 + 2xy - x^2 = C'$。

---

## 题 15：一阶线性微分方程 (积分因子法)

### 题目描述
求解微分方程 $y' + \frac{y}{x} = \frac{1}{x^2}$，初始条件 $y(1)=1$，其中 $x>0$。

### 解答
一阶线性 ODE 的标准解法是寻找积分因子 (Integrating Factor) $I(x)$。
具体步骤：
1. 标准形式为 $y' + P(x)y = Q(x)$。此时 $P(x) = 1/x$，$Q(x) = 1/x^2$。
2. 计算积分因子：$I(x) = e^{\int P(x) dx} = e^{\int (1/x) dx} = e^{\ln x} = x$。
3. 将方程两边同乘 $I(x)$：

$$
x y' + y = \frac{1}{x}
$$

4. 左边完美塌陷为乘积的导数：$(xy)' = \frac{1}{x}$。
5. 两边积分：$xy = \ln x + C$。
6. 代入初始条件 $y(1)=1$，得到 $1 \cdot 1 = 0 + C \Rightarrow C=1$。
7. 最终解为 $y = \frac{\ln x + 1}{x}$。

---

## 题 16：二阶齐次常系数线性方程

### 题目描述
求解常微分方程 $y'' + y' + y = 0$。

### 解答
具体步骤：
1. 写出特征方程 (Characteristic equation)：$r^2 + r + 1 = 0$。
2. 求解特征根，由于判别式 $\Delta = 1 - 4 = -3 < 0$，有一对共轭复根：

$$
r = -\frac{1}{2} \pm \frac{\sqrt{3}}{2}i
$$

3. 根据复根的通解公式，通解为：

$$
y = e^{-x/2} \left( c_1 \cos(\frac{\sqrt{3}}{2}x) + c_2 \sin(\frac{\sqrt{3}}{2}x) \right)
$$

---

## 题 17：二阶非齐次常系数线性方程

### 题目描述
求解 ODE $y'' + y' + y = 1$ 和 $y'' + y' + y = x$。

### 解答
非齐次方程的解 = 对应齐次方程的通解 + 自身的特解。齐次通解已在上题求出。我们只需利用待定系数法寻找特解 $y_p$。
**对于 $y'' + y' + y = 1$：**
右边是常数，猜测特解也是常数 $y_p = A$。代入得 $0 + 0 + A = 1 \Rightarrow y_p = 1$。
总解为：$y = y_g + 1$。

**对于 $y'' + y' + y = x$：**
右边是一次多项式，猜测特解 $y_p = mx + n$。求导得 $y_p' = m$, $y_p'' = 0$。
代入得 $0 + m + (mx+n) = x$。对比系数：$m=1$ 且 $m+n=0 \Rightarrow n=-1$。
所以特解 $y_p = x - 1$。
总解为：$y = y_g + x - 1$。

---

# 3.6 线性代数 (Linear Algebra)

## 题 18 & 19：相关性矩阵与边界 (Vectors & Positive Semidefinite Matrix)

*(注：原书在向量和半正定矩阵小节使用同一道题展示了两种解法，这里将其合并)*

### 题目描述
假设有三个随机变量 $x, y, z$。$x$ 与 $y$ 的相关系数为 $0.8$，$x$ 与 $z$ 的相关系数也是 $0.8$。请问 $y$ 与 $z$ 的相关系数的最大值和最小值分别是多少？

### 解答
**方法一：利用向量的几何几何意义 (内积)**
相关系数本质上就是高维空间中两个向量夹角的余弦值 ($\rho = \cos\theta$)。
已知 $\cos\angle(x,y) = 0.8$，$\cos\angle(x,z) = 0.8$。
1. 最大相关系数（最小夹角）：当 $y$ 和 $z$ 向量在 $x$ 的同一侧并重合时夹角为 0，$\cos(0) = 1$。
2. 最小相关系数（最大夹角）：当 $y$ 和 $z$ 分别位于 $x$ 的两侧时，它们的夹角最大为 $2\theta$。

$$
\cos(2\theta) = 2\cos^2\theta - 1 = 2(0.8^2) - 1 = 1.28 - 1 = 0.28
$$

所以范围是 $[0.28, 1]$。

**方法二：利用相关系数矩阵的半正定性 (Positive Semidefinite)**
协方差矩阵和相关系数矩阵必须是半正定的，其充要条件是它的行列式大于等于 0。
设 $y$ 与 $z$ 的相关系数为 $\rho$，构建 $3 \times 3$ 相关系数矩阵：

$$
P = \begin{bmatrix} 1 & 0.8 & 0.8 \\ 0.8 & 1 & \rho \\ 0.8 & \rho & 1 \end{bmatrix}
$$

计算其行列式：

$$
\det(P) = 1(1-\rho^2) - 0.8(0.8-0.8\rho) + 0.8(0.8\rho-0.8) \ge 0
$$

$$
1 - \rho^2 - 0.64 + 0.64\rho + 0.64\rho - 0.64 \ge 0 \Rightarrow -\rho^2 + 1.28\rho - 0.28 \ge 0
$$

解二次不等式 $(\rho-1)(\rho-0.28) \le 0$，得到 $0.28 \le \rho \le 1$。

---

## 题 20：最小二乘法的矩阵推导 (OLS without built-in library)

### 题目描述
如果你的编程语言没有内置的线性最小二乘法回归 (OLS) 函数，你将如何设计一个算法来实现它？

### 解答
这要求你用矩阵语言推导 OLS 解析解，并提出工程上的稳定解法。
具体步骤：
1. 线性回归模型可以写成矩阵形式：$Y = X\beta + \epsilon$。
2. OLS 的目标是最小化残差平方和：

$$
\min_{\beta} f(\beta) = (Y - X\beta)^T (Y - X\beta)
$$

3. 对 $\beta$ 求偏导数并令其等于零向量：

$$
\nabla f(\beta) = -2X^T(Y - X\beta) = 0 \Rightarrow X^TX\beta = X^TY
$$

4. 数学解析解为 $\beta = (X^TX)^{-1}X^TY$。
5. **工程实现细节**：直接求逆矩阵 $(X^TX)^{-1}$ 在特征存在多重共线性时会导致极大的数值不稳定。工业级算法应当利用 **QR 分解** ($X = QR$) 或奇异值分解 (SVD) 来求解超定方程组。

---

## 题 21：特征值与特征向量 (Eigenvalue and Eigenvector)

### 题目描述
求矩阵 $A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$ 的特征值和特征向量。

### 解答
具体步骤：
1. 利用特征方程 $\det(A - \lambda I) = 0$ 求解：

$$
\det \begin{bmatrix} 2-\lambda & 1 \\ 1 & 2-\lambda \end{bmatrix} = (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = 0
$$

解得特征值 $\lambda_1 = 1$, $\lambda_2 = 3$。（*注：其实通过矩阵的迹 $\text{Tr}(A)=4$ 和行列式 $\det(A)=3$ 联立方程也能秒杀*）。
2. 代入 $\lambda_1 = 1$ 求特征向量：

$$
\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \Rightarrow x_1 + x_2 = 0
$$

归一化后的特征向量为 $\begin{bmatrix} 1/\sqrt{2} \\ -1/\sqrt{2} \end{bmatrix}$。
3. 代入 $\lambda_2 = 3$ 求特征向量：

$$
\begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \Rightarrow -x_1 + x_2 = 0
$$

归一化后的特征向量为 $\begin{bmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \end{bmatrix}$。

---

## 题 22：生成相关随机变量 (Cholesky decomposition)

### 题目描述
如果你有一个能生成标准正态分布随机数的发生器，你将如何利用它生成两个相关系数为 $\rho$ 的标准正态分布随机变量？

### 解答
在蒙特卡洛模拟中，生成具有特定相关性结构的资产价格路径是必须掌握的技能，其核心是 **Cholesky 分解**。
具体步骤：
1. 假设已生成两个完全独立的标准正态分布变量 $z_1$ 和 $z_2$。
2. 第一个变量直接使用：$x_1 = z_1$。
3. 第二个变量构造为独立变量的线性组合：$x_2 = \rho z_1 + \sqrt{1-\rho^2} z_2$。
4. **验证**：
    * $var(x_1) = 1$。
    * $var(x_2) = \rho^2 var(z_1) + (1-\rho^2) var(z_2) = \rho^2 + 1 - \rho^2 = 1$。
    * $cov(x_1, x_2) = cov(z_1, \rho z_1 + \dots) = \rho \cdot cov(z_1, z_1) = \rho$。
由于标准正态分布的线性组合依然是正态分布，该方法完美满足要求。

### 核心知识点与拓展
* **量化拓展**：对于高维多元正态分布 $N(\mu, \Sigma)$，通常对正定协方差矩阵 $\Sigma$ 进行 Cholesky 分解 $\Sigma = R^T R$。生成一组独立正态向量 $Z$ 后，通过向量变换 $X = \mu + R^T Z$ 即可生成所需的相关随机路径。
