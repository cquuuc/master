# Problem 1

给定数据集：
$$
\{3, 0, 4, 5, 3, 2, 1, 3, 2, 3, 2, 3, 4, 1, 4, 3, 2, 5, 3, 1, 3, 4, 3, 0, 1\}
$$

#### 1. 计算均值

$$
\bar{x} = \frac{65}{25} = 2.6
$$

#### 2. 计算样本方差

$$
s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2
$$

$$
s^2 = \frac{38.4}{24} = 1.6
$$

#### 3. 计算样本标准差 \(s\)

$$
s = \sqrt{s^2} = \sqrt{1.6} \approx 1.2649
$$

#### 4. 计算中位数 \(\tilde{x}\)

$$
\{0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5\}
$$


中位数为第 \(n/2\) 和第 \(n/2 + 1\) 个数的平均：
$$
\tilde{x} = \frac{3 + 3}{2} = 3
$$

#### 5. 计算四分位数 \(Q_1, Q_2, Q_3\)

- \(Q_1\) 是第 \(n/4\) 个数：
  $$
  Q_1 = 2
  $$
- \(Q_2\) 是中位数：
  $$
  Q_2 = 3
  $$
- \(Q_3\) 是第 \(3n/4\) 个数：
  $$
  Q_3 = 4
  $$
  

#### 6. 计算四分位距 \(IQR\)

$$
IQR = Q_3 - Q_1 = 4 - 2 = 2
$$

#### 7. 绘制箱线图和直方图

- **箱线图**：可以使用统计软件（如Python的matplotlib库）绘制。
- **直方图**：同样可以使用统计软件绘制。

# Problem 2

给定数据集：
$$
\{0.21, 0.73, 0.35, 0.91, 0.43, 1.26, 2.42, 0.87, 1.31, 0.18, 0.42, 0.85, 1.27, 0.39, 0.95, 0.52\}
$$

#### 1. 绘制箱线图和直方图

同样可以使用统计软件绘制。

# Problem 3

给定概率密度函数：
$$
f(x; \theta) = 0.5 \cdot (1 + \theta x), \quad -1 \leq x \leq 1, \quad -1 \leq \theta \leq 1
$$

#### a. 最大似然估计

似然函数为：
$$
L(\theta) = \prod_{i=1}^{n} f(x_i; \theta)=0.5^n\cdot\prod_{i=1}^{n}(1+\theta x)

\\对数似然函数为：

\ln L(\theta) = \sum_{i=1}^{n} \ln f(x_i; \theta)=\ln L(\theta) = n \ln(0.5) + \sum_{i=1}^{n} \ln(1 + \theta x_i)\\
\ln L(\theta) \approx \sum_{i=1}^{n} \ln(1 + \theta x_i)\\
\frac{d}{d\theta} \ln L(\theta) = \sum_{i=1}^{n} \frac{x_i}{1 + \theta x_i}\\
\sum_{i=1}^{n} \frac{x_i}{1 + \theta x_i} = 0
$$
求导并设为零，解出 \(\theta\)。

#### b. 矩估计

$$
\mu_1=E(x)=\int x  f(x; \theta)dx =\int^1_{-1} x 0.5 \cdot (1 + \theta x)=\theta/3
$$

#### c. 检查无偏性

计算期望值，检查是否等于真实值。
$$
E[\hat{\mu}] = \mu
$$

# Problem 4

给定均匀分布 \(U([a, b])\)。

#### a. 最大似然估计

> 对于均匀分布 \( U([a, b]) \)，我们需要找到参数 \( a \) 和 \( b \) 的最大似然估计（MLE）。假设我们有 \( n \) 个独立同分布的样本 \( x_1, x_2, \ldots, x_n \) 来自于这个均匀分布。
>
> ### 1. 似然函数
>
> 均匀分布的概率密度函数为：
>
> $$
> f(x; a, b) = 
> \begin{cases} 
> \frac{1}{b - a} & \text{if } a \leq x \leq b \\
> 0 & \text{otherwise}
> \end{cases}
> $$
> 因此，似然函数 \( L(a, b) \) 可以表示为：
>
> $$
> L(a, b) = \prod_{i=1}^{n} f(x_i; a, b) = \prod_{i=1}^{n} \frac{1}{b - a} = \left( \frac{1}{b - a} \right)^n
> $$
> 前提是 \( a \leq x_i \leq b \) 对于所有的 \( i \)。
>
> ### 2. 对数似然函数
>
> 为了简化计算，我们取对数似然函数：
>
> $$
> \ln L(a, b) = n \ln \left( \frac{1}{b - a} \right) = -n \ln(b - a)
> $$
>
> ### 3. 约束条件
>
> 为了使似然函数有效，必须满足以下条件：
>
> $$
> a \leq \min(x_1, x_2, \ldots, x_n) \quad \text{和} \quad b \geq \max(x_1, x_2, \ldots, x_n)
> $$
>
> ### 4. 最大化对数似然函数
>
> 为了最大化对数似然函数，我们需要最小化 \( b - a \)。根据约束条件，最优的选择是：
>
> - $$
>   - 选择 \( a \) 为样本的最小值： \( a = \min(x_1, x_2, \ldots, x_n) \)\\
>   - 选择 \( b \) 为样本的最大值： \( b = \max(x_1, x_2, \ldots, x_n) \)
>   $$
>
>   
>
> ### 5. 最终结果
>
> 因此，均匀分布 \( U([a, b]) \) 的最大似然估计为：
>
> $$
> \hat{a} = \min(x_1, x_2, \ldots, x_n)
> $$
>
> $$
> \hat{b} = \max(x_1, x_2, \ldots, x_n)
> $$
>
> 这意味着我们通过样本的最小值和最大值来估计均匀分布的参数 \( a \) 和 \( b \)。

#### b. 矩估计

对于均匀分布 \( U([a, b]) \)，我们可以通过矩估计法来估计参数 \( a \) 和 \( b \)。矩估计法的基本思想是利用样本的矩来估计总体的矩。

### 1. 确定总体的矩

对于均匀分布 \( U([a, b]) \)，我们可以计算其期望值（第一矩）和方差（第二矩）：

- **期望值**：

$$
E[X] = \frac{a + b}{2}
$$

- **方差**：

$$
Var(X) = \frac{(b - a)^2}{12}
$$

### 2. 计算样本矩

假设我们有 \( n \) 个独立同分布的样本 \( x_1, x_2, \ldots, x_n \)，我们可以计算样本的第一矩和第二矩：

- **样本均值**（第一矩）：

$$
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
$$

- **样本方差**（第二矩）：

$$
S^2 = \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2
$$

### 3. 建立方程

我们将样本矩与总体矩相等，建立方程：

1. 将样本均值与总体期望值相等：

$$
\bar{x} = \frac{a + b}{2}
$$

2. 将样本方差与总体方差相等：

$$
E[X] = \frac{1}{b - a} \left[ \frac{x^2}{2} \right]_{a}^{b} = \frac{1}{b - a} \left( \frac{b^2}{2} - \frac{a^2}{2} \right) = \frac{b^2 - a^2}{2(b - a)}= \frac{b + a}{2}\\
E[X^2] = \int_{a}^{b} x^2 f(x) \, dx = \int_{a}^{b} x^2 \cdot \frac{1}{b - a} \, dx= \frac{b^2 + ab + a^2}{3}\\
D(X) = E[X^2] - (E[X])^2= \frac{b^2 + ab + a^2}{3} - \left( \frac{b + a}{2} \right)^2==\frac{(b - a)^2}{12}
$$

### 4. 解方程

从第一个方程中，我们可以得到：

$$
a + b = 2\bar{x} \quad (1)
$$
从第二个方程中，我们可以得到：

$$
b - a = 2\sqrt{3S^2} \quad (2)
$$
现在我们有两个方程（1）和（2），可以通过求解这两个方程来找到 \( a \) 和 \( b \)。

### 5. 求解 \( a \) 和 \( b \)

将方程（1）和方程（2）相加和相减：

- **相加**：

$$
(a + b) + (b - a) = 2\bar{x} + 2\sqrt{3S^2}
$$

得到：

$$
2b = 2\bar{x} + 2\sqrt{3S^2} \implies b = \bar{x} + \sqrt{3S^2}
$$

- **相减**：

$$
(a + b) - (b - a) = 2\bar{x} - 2\sqrt{3S^2}
$$

得到：

$$
2a = 2\bar{x} - 2\sqrt{3S^2} \implies a = \bar{x} - \sqrt{3S^2}
$$

### 6. 最终结果

因此，均匀分布 \( U([a, b]) \) 的矩估计为：

$$
\hat{a} = \bar{x} - \sqrt{3S^2}
$$

$$
\hat{b} = \bar{x} + \sqrt{3S^2}
$$

### 注意

在进行矩估计时，确实不需要计算积分，因为我们直接利用样本的均值和方差来估计参数。

#### c. 检查无偏性

计算期望值，检查是否等于真实值。

#### d. 从数据中计算 \(a\) 和 \(b\) 的估计。[0.3, 1.5, 2.4, 0.8]

# Problem 5

### a. 计算样本均值

给定的两个置信区间分别为：

1. \( (114.4, 115.6) \)
2. \( (114.1, 115.9) \)

样本均值可以通过计算每个区间的中点来得到。中点的计算公式为：

$$
\text{中点} = \frac{\text{下限} + \text{上限}}{2}
$$

#### 计算第一个区间的样本均值：

$$
\text{均值}_1 = \frac{114.4 + 115.6}{2} = \frac{230}{2} = 115.0
$$

#### 计算第二个区间的样本均值：

$$
\text{均值}_2 = \frac{114.1 + 115.9}{2} = \frac{230}{2} = 115.0
$$

#### 总结样本均值：

两个置信区间的样本均值均为：

$$
\text{样本均值} = 115.0
$$

### b. 判断置信水平

置信区间的宽度与置信水平之间存在反比关系。较窄的置信区间对应较低的置信水平，较宽的置信区间对应较高的置信水平。以下是详细的解释：

1. **置信区间的定义**：
   置信区间是基于样本数据计算出的一个区间，目的是估计总体参数（如均值）所在的范围。置信水平表示我们对这个区间包含真实参数的信心程度，通常用百分比表示（如 95%、99% 等）。

2. **置信水平与区间宽度的关系**：
   - 较高的置信水平（例如 99%）意味着我们希望更高的概率包含真实参数，因此需要一个更宽的区间。这是因为我们希望覆盖更多的可能性，以确保真实参数在这个区间内。
   - 较低的置信水平（例如 90%）则允许我们接受更小的覆盖概率，因此可以使用较窄的区间。

3. **具体分析**：
   - 第一个区间 \( (114.4, 115.6) \) 的宽度为 \( 115.6 - 114.4 = 1.2 \)。
   - 第二个区间 \( (114.1, 115.9) \) 的宽度为 \( 115.9 - 114.1 = 1.8 \)。

   由于第一个区间的宽度较窄，意味着它对应的置信水平较低；而第二个区间的宽度较宽，意味着它对应的置信水平较高。
   
   

### 总结

$$
length=E(\theta_L,\theta_U)=1.2\\
E(\theta_L,\theta_U)=2\cdot Z_{\frac{\alpha}{2}}\frac{\sigma}{\sqrt n}
\\
( z = 1.96 ) 对应约 95\% 的置信水平。\\
( z = 1.64 ) 对应约 90\% 的置信水平。\\
( z = 2.576 ) 对应约 99\% 的置信水平。\\
如果我们假设 ( s = 0.5 ) 且 ( n = 30 )\\
z = \frac{1.2}{2 \cdot \frac{0.5}{\sqrt{30}}} = \frac{1.2}{2 \cdot 0.0913} \approx 6.57\\
这个 ( z ) 值显然超出了常见的置信水平范围，说明我们的假设不合理。
$$



- **样本均值**：两个置信区间的样本均值均为 \( 115.0 \)。
- **置信水平判断**：第一个区间 \( (114.4, 115.6) \) 较窄，因而对应较低的置信水平；第二个区间 \( (114.1, 115.9) \) 较宽，因而对应较高的置信水平。

# Problem 6

给定数据：
11.5, 13.4, 4.9, 3.6, 8.2, 5.2, 12.1, 17.1, 10.7, 3.4, 10.7, 4.8, 9.9, 9.3, 15.2, 20.6, 14.2, 4.1, 9.3, 5.6, 8.5, 25.5, 7.6, 3.8, 7.8, 5.7, 4.2, 13.8, 5.2, 3.7, 6.2, 5.4, 4.0, 12.6, 5.5, 3.6, 6.6, 5.2, 3.9, 13.1, 5.1, 3.6, 7.0, 5.1, 3.8, 8.9, 5.0, 3.6

计算95%置信区间。

要计算给定数据的 95% 置信区间，我们需要以下步骤：

1. **计算样本均值** \( \bar{x} \)
2. **计算样本标准差** \( s \)
3. **确定样本大小** \( n \)
4. **计算标准误差** \( SE \)
5. **查找 z 值**（对于 95% 置信水平，通常为 1.96）
6. **计算置信区间**

### 1. 计算样本均值 \( \bar{x} \)

样本均值为：
$$
\bar{x} = \frac{288.3}{50} = 5.766
$$

### 2. 计算样本标准差 \( s \)

$$
样本标准差的计算公式为：
s = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n - 1}}\\

计算每个数据点与均值的差的平方和：
\sum (x_i - \bar{x})^2\\

计算结果为：
\sum (x_i - 5.766)^2 \approx  132.4\\
然后计算标准差：s = \sqrt{\frac{132.4}{50 - 1}} \approx 1.65
$$

### 3. 计算标准误差 \( SE \)

标准误差的计算公式为：
$$
SE = \frac{s}{\sqrt{n}} = \frac{1.65}{\sqrt{50}} \approx 0.233
$$

### 4. 查找 z 值

对于 95% 的置信水平，z 值为 1.96。

### 5. 计算置信区间

$$
置信区间的计算公式为：
\text{置信区间} = \left( \bar{x} - z \cdot SE, \bar{x} + z \cdot SE \right)\\

代入数值：
\text{置信区间} = \left( 5.766 - 1.96 \cdot 0.233, 5.766 + 1.96 \cdot 0.233 \right)\\

计算结果为：
\text{置信区间} = \left( 5.766 - 0.456, 5.766 + 0.456 \right) = (5.310, 6.222)\\
$$

### 最终结果

因此，给定数据的 95% 置信区间为：
$$
(5.310, 6.222)
$$


# Problem 7

给定样本：
$$
n = 50, \bar{x} = 3.05, s = 0.34
$$
进行假设检验。

要检验样本数据是否强烈表明眼镜镜片的真实平均厚度与期望值（3.20 mm）不同，我们可以进行假设检验。以下是详细的步骤：

### 1. 确定假设

- $$
  - **原假设 ( H_0 )**：真实平均厚度等于期望值，即 ( \mu = 3.20 ) mm。\\
  - **备择假设 ( H_1 )**：真实平均厚度不等于期望值，即 ( \mu \neq 3.20 ) mm。
  $$

  

### 2. 选择显著性水平

$$
我们选择显著性水平 ( \alpha = 0.05 )。
$$



### 3. 计算检验统计量

使用样本均值、样本标准差和样本大小来计算检验统计量。我们使用 t 检验，因为样本量较小且我们不知道总体标准差。

检验统计量的计算公式为：
$$
t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}
$$
其中：
- $$
  - ( \bar{x} = 3.05 ) mm（样本均值）\\
  - ( \mu_0 = 3.20 ) mm（期望值）\\
  - ( s = 0.34 ) mm（样本标准差）\\
  - ( n = 50 )（样本大小）\\
  $$

  

代入数值：
$$
t = \frac{3.05 - 3.20}{0.34 / \sqrt{50}} = \frac{-0.15}{0.048} \approx -3.125
$$


### 4. 确定临界值

$$
由于这是一个双尾检验，我们需要查找 t 分布的临界值。自由度 ( df = n - 1 = 50 - 1 = 49 )。\\

查找 t 分布表，找到 ( \alpha/2 = 0.025 ) 的临界值。对于 49 自由度，临界值大约为 ( \pm 2.009 )。
$$



### 5. 进行决策

- $$
  - 如果 ( |t| > t_{\text{临界}} )，则拒绝原假设 ( H_0 )。\\
  - 如果 ( |t| \leq t_{\text{临界}} )，则不拒绝原假设 ( H_0 )。
  $$

  

在本例中：
$$
|-3.125| > 2.009
$$
因此，我们拒绝原假设 \( H_0 \)。

### 6. 结论

根据样本数据，检验结果表明，真实平均厚度与期望值（3.20 mm）存在显著差异。我们可以得出结论，数据强烈表明眼镜镜片的真实平均厚度与期望值不同。

### 总结

通过 t 检验，我们发现样本均值（3.05 mm）与期望值（3.20 mm）之间的差异是显著的，因此可以认为真实平均厚度与期望值存在显著差异。

# Problem 8

要判断样本大小 50 是否过大，我们需要计算在真实平均厚度 \( \mu = 3.00 \) mm 的情况下，样本大小为 50 时的 β（第二类错误概率）。我们将使用以下步骤进行计算：

### 1. 确定假设

- $$
  - **原假设 ( H_0 )**：真实平均厚度 ( \mu = 3.20 ) mm。\\
  - **备择假设 ( H_1 )**：真实平均厚度 ( \mu \neq 3.20 ) mm。
  $$

  

### 2. 设定参数

- $$
  - 期望值 ( \mu_0 = 3.20 ) mm（原假设下的均值）。\\
  - 真实均值 ( \mu = 3.00 ) mm（备择假设下的均值）。\\
  - 样本标准差 ( s = 0.30 ) mm（实验者的先验信念）。\\
  - 样本大小 ( n = 50 )。
  $$

  

### 3. 计算检验统计量的临界值

$$
我们需要计算在原假设下的临界值。\\对于双尾检验，显著性水平 ( \alpha = 0.05 )，因此每尾的显著性水平为 ( \alpha/2 = 0.025 )。\\

查找 t 分布表，找到自由度 ( df = n - 1 = 49 ) 时的临界值\\对于 ( \alpha/2 = 0.025 )，临界值大约为 ( t_{\text{临界}} \approx \pm 2.009 )。
$$



### 4. 计算临界值对应的样本均值

根据临界值，我们可以计算出拒绝域的边界。拒绝原假设的条件为：
$$
\bar{x} < \mu_0 - t_{\text{临界}} \cdot \frac{s}{\sqrt{n}} \quad \text{或} \quad \bar{x} > \mu_0 + t_{\text{临界}} \cdot \frac{s}{\sqrt{n}}
$$
代入数值：
$$
\bar{x} < 3.20 - 2.009 \cdot \frac{0.30}{\sqrt{50}} \quad \text{或} \quad \bar{x} > 3.20 + 2.009 \cdot \frac{0.30}{\sqrt{50}}
$$
计算标准误差：
$$
SE = \frac{s}{\sqrt{n}} = \frac{0.30}{\sqrt{50}} \approx 0.0424
$$
计算临界值：

$$
\bar{x} < 3.20 - 2.009 \cdot 0.0424 \approx 3.20 - 0.0852 \approx 3.1148\\

\bar{x} > 3.20 + 2.009 \cdot 0.0424 \approx 3.20 + 0.0852 \approx 3.2852
$$

5. 计算 β（第二类错误概率）

$$
第二类错误概率 ( \beta ) 是指在真实均值 ( \mu = 3.00 ) mm 的情况下，未能拒绝原假设的概率。\\我们需要计算在 ( \mu = 3.00 ) mm 时，样本均值落在 ( (3.1148, 3.2852) ) 区间内的概率。
$$

计算样本均值的标准误差：
$$
SE = \frac{0.30}{\sqrt{50}} \approx 0.0424
$$
计算 z 值：
$$
z_1 = \frac{3.1148 - 3.00}{0.0424} \approx \frac{0.1148}{0.0424} \approx 2.71\\
z_2 = \frac{3.2852 - 3.00}{0.0424} \approx \frac{0.2852}{0.0424} \approx 6.73
$$


### 6. 查找 z 值对应的概率

查找标准正态分布表：

- $$
  - ( P(Z < 2.71) \approx 0.9966 )\\
  - ( P(Z < 6.73) \approx 1.0000 )
  $$

  

因此，第二类错误概率 \( \beta \) 为：
$$
\beta = P(3.1148 < \bar{x} < 3.2852) = P(Z < 6.73) - P(Z < 2.71) \approx 1.0000 - 0.9966 = 0.0034
$$


### 7. 结论

$$
在真实均值 ( \mu = 3.00 ) mm 的情况下，样本大小 50 使得第二类错误概率 ( \beta \approx 0.0034 )，远低于 0.05。\\因此，样本大小 50 并不是过大的，因为它能够有效地控制第二类错误概率在 0.05 以下。
$$

综上所述，样本大小 50 是合理的，并且并不算过大。

