# 理论物理基础I（二）：经典电动力学 随想

## 电磁场的基本规律

### 电磁场与麦克斯韦方程组

从三维形式的Maxwell方程组过渡到四维协变形式的方程，引入四维矢势 $F_{\mu\nu}=\partial^\mu A^\nu - \partial^\nu A^\mu$ ，将表达式进行一定的化简。

$$
\partial_{\mu}F^{\mu\nu}=\mu_0J^\nu
$$

注意，这一方式等式左边只能含有场量 $\overrightarrow E$ 和 $\overrightarrow B$ ，所以要通过后续的在各种介质中各种线性假设才能得到含有 $\overrightarrow D$ 与 $\overrightarrow H$ 之间的关系。

同时，还有时域-频域傅里叶变换的表达式：

虽然人为规定，但是（似乎？）是约定的时域到频域的变换没有系数
$$
F(\omega)=\int_{-\infty}^{\infty}f(t)\mathrm{e}^{\mathrm{i}\omega t}\mathrm{d}t
$$

$$
f(t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}F(\omega)\mathrm{e}^{-\mathrm{i}\omega t}\mathrm{d}\omega
$$

这也说明，介质的色散是由于响应的弛豫造成的。

### 电磁场的能量、动量、角动量守恒律

#### 能量与动量守恒

电磁场的能量密度与能流密度：<mark>（前提：线性介质）</mark>

$$
u=\frac{1}{2}\vec D\cdot \vec E+\frac{1}{2}\vec B \cdot \vec H
$$

$$
\vec S = \vec E \times \vec H
$$

电磁场的动量密度与动量流密度：<mark>（前提：线性无色散损耗介质）</mark>

$$
\vec g = \vec E\times \vec B
$$

$$
\overset{\leftrightarrow}{\sigma}= \frac{1}{2}(\vec D\cdot \vec E)\overset{\leftrightarrow}{I}-\vec D\vec E + \frac{1}{2}(\vec B\cdot \vec H)\overset{\leftrightarrow}{I}-\vec H \vec B
$$

注意相应量之间的对应。

#### 能动张量

个人感觉直接推导还是比较复杂的，但是结论还是比较容易掌握的。

电磁场能动张量 $T^{\mu \nu}$ :

$$
T^{00} = u, ~T^{0i}=T^{i0}=\vec S/c = \vec g \cdot c ,~T^{ij}=\overset{\leftrightarrow}{\sigma}^{ij}
$$

<mark>0分量：守恒荷</mark>

#### 角动量守恒定律

注意到可以通过能动张量构建角动量守恒的表达式，可以先不关注“叉乘”带来的Levi-Civita符号，直接用 $M^{\alpha \mu\nu}=T^{\alpha \mu}x^{\nu}-T^{\alpha \nu}x^{\mu}$ 构建表达式。

### 电磁势与规范的选取

选取规范将电磁场方程化简，进而得到简化的表达式。

#### Coulomb规范

保证 $\varphi$ 的形式简单： $\nabla \cdot \vec A = 0$ ， $\nabla^2 \varphi = \frac{\rho}{\varepsilon_0}$ 。

静态电磁场就会更加简单，相当于直接电势管电场，矢势管磁场。

采用格林函数可以将表达式直接解出来

#### Lorenz-Lorentz规范

考虑含时的情形，得到

$$
\partial_\mu A^\mu = \frac{1}{c^2}\partial_t\varphi+\nabla\cdot A= 0
$$

直接将标势与矢势的方程同时直接化为波动方程。

## 静电场

## 静磁场

## 电磁波的传播

### 简谐平面电磁波

### 色散介质中的电磁波

### 导体中的电磁波

### 波导与谐振腔

其实讲义中的推导感觉不是非常适合于直接计算，显然比较麻烦，直接记忆公式由非常困难。直接考虑矩形波导中的电磁波，容易发现只能传递 $\mathrm{TE_{mn}}$ 波与 $\mathrm{TM_{mn}}$ 波，由对称性，可以仅仅研究 $\mathrm{TE}$ 波的情形。

电场只有横向分量+边界条件：

$$
E_x = E_{x0}\cos\left(\frac{\pi x}{a}\right)\sin\left(\frac{\pi y}{b}\right)
$$

$$
E_y = E_{y0}\sin\left(\frac{\pi x}{a}\right)\cos\left(\frac{\pi y}{b}\right)
$$

然后根据 $\nabla\cdot E = 0$ 可以直接得到 $E_{x0}$与$E_{y0}$ 之间的关系（ $k_x E_{x0} + k_y E_{y0} = 0$ ），实现变量的统一。
