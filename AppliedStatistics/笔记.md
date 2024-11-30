# CDF:累计分布函数

$$
已知\ \begin{array}{c|lcr}
    y & \text{0} & \text{1} \\
    \hline
    P & \frac{1}{2} & \frac{1}{2}\\
\end{array},
\ n=1000,X=y_1+……+y_{1000}
\\求E(X),D(X),\sigma(X)
\\解:已知E(y)=\frac{1}{2}\\D(y)=E(y^2)-(E(y)^2)=\frac{1}{2} \cdot0^2+\frac{1}{2}\cdot1^2-(\frac{1}{2})^2=\frac{1}{4}\\
所以E(X)=1000\cdot\frac{1}{2}=500\\D(X)=1000\cdot\frac{1}{4}=250
\\\sigma(X)=\sqrt{D(X)}=\sqrt{250}\approx\sqrt{256}=16\\
且一般情况下满足标准正态分布\implies\frac{X-E(X)}{\sigma(X)}\backsim N(0,1)
\\同理普通正态分布为X \backsim N(\mu,\sigma^2),P(X)=\frac{1}{\sqrt{2\pi}\cdot\sigma}\cdot e^{-\frac{(x-\mu)^2}{2\cdot\sigma^2}}
\\若令Z=\frac{X-E(X)}{\sigma(X)}\implies Z \backsim N(0,1),P(Z)=\frac{1}{\sqrt{2\pi}}\cdot e^{-\frac{x^2}{2}}\\
那么P(Z\leq0.7)=\int_0^{0.7}P(Z)=\int_0^{0.7}\frac{1}{\sqrt{2\pi}}\cdot e^{-\frac{x^2}{2}}\cdot dx 
\\这样计算过于麻烦，于是引入了标准正态的一个累计分布函数CDF\\
\phi(a)=P(Z\leq a)
\\ \phi(a)=\int_{-\infty}^{a}\frac{1}{\sqrt{2\pi}}\cdot e^{-\frac{x^2}{2}}\cdot dx 
\\ \phi_0(a)=\int_{0}^{a}\frac{1}{\sqrt{2\pi}}\cdot e^{-\frac{x^2}{2}}\cdot dx 
\\
例如：要求P(x>\xi)=P(\frac{x-500}{16}>\frac{\xi-500}{16})
\\P(x>500)=P(\frac{x-500}{16}>\frac{500-500}{16})=P(Z>0)=1-\phi(0)
\\P(x>530)=P(\frac{x-530}{16}>\frac{530-500}{16})=P(Z>\frac{30}{16})=1-\phi(\frac{30}{16})
\\P(x>550)=P(\frac{x-550}{16}>\frac{550-500}{16})=P(Z>\frac{50}{16})=1-\phi(\frac{50}{16})
$$

# CLT:中心极限定理

$$
当n及其大的时候，E(X)=\mu，D(X)=\sigma^2\\
若X收敛则有X_1+……+X_n\backsim N(n\cdot\mu,n\cdot\sigma^2)\ or \ N(n\cdot\mu,(\sqrt{n}\cdot\sigma)^2)
\\三\sigma原则：\\还是上面的例子 \sigma=16，n=1000\\
\\P(\mu-\sigma<x<\mu+\sigma)=P(500-16<x<500+16)\approx0.68
\\P(\mu-2\sigma<x<\mu+2\sigma)=P(468<x<532)\approx0.96
\\P(\mu-3\sigma<x<\mu+3\sigma)=P(453<x<548)\approx0.999

\\ \color{yellow}{例题}\\
n=100求P(40\leq X\leq 60);n=1000求P(400\leq X\leq 600)
\\E(X)=\frac{1}{2},D(X)=\frac{1}{4}
\\E(X_{100})=\frac{1}{2}\cdot100=50,D(X_{100})=\frac{1}{4}\cdot100=25,\sigma(X_{100})=5
\\E(X_{1000})=\frac{1}{2}\cdot1000=500,D(X_{1000})=\frac{1}{4}\cdot1000=250,\sigma(X_{1000})=16
\\Z=\frac{X-E(X)}{\sigma(X)}
\\P(40\leq X\leq 60)=P(\frac{40-50}{5}\leq Z\leq \frac{60-50}{5})=P(-2\leq Z\leq 2)=\phi(2)-\phi(-2)
\\P(400\leq X\leq 600)=P(\frac{400-500}{16}\leq Z\leq \frac{600-500}{16})=P(-6.25\leq Z\leq 6.25)=\phi(6.25)-\phi(-6.25)
$$

# 联合概率分布随机变量的独立性

$$
x与y独立吗？\\

\\ \color{yellow}{例题1}\\ P_{x,y}=        \begin{cases}
            x+y,  & x,y\in[0,1] \\
            0, & other \\
        \end{cases}\\
        P_{x}=        \begin{cases}
            \int_0^1 (x+y)\cdot dy=x+\frac{1}{2} \\
            \int_0^1 0\cdot dy=0 \\
        \end{cases} \ \ \
          P_{y}=        \begin{cases}
            \int_0^1 (x+y)\cdot dx=y+\frac{1}{2} \\
            \int_0^1 0\cdot dx=0 \\
        \end{cases}\\
         P_{x,y}=        \begin{cases}
            (x+\frac{1}{2})\cdot (y+\frac{1}{2}) \\
            0 \\
        \end{cases}\neq \begin{cases}
            x+y \\
            0 \\
        \end{cases}\\不独立\\
\\ \color{yellow}{例题2}\\ P_{x,y}=        \begin{cases}
            4xy,  & x,y\in[0,1] \\
            0, & other \\
        \end{cases}\\
        P_{x}=        \begin{cases}
            \int_0^1 4xy\cdot dy=2x \\
            \int_0^1 0\cdot dy=0 \\
        \end{cases} \ \ \
          P_{y}=        \begin{cases}
            \int_0^1 4xy\cdot dx=2y \\
            \int_0^1 0\cdot dx=0 \\
        \end{cases}\\
         P_{x,y}=        \begin{cases}
            2x\cdot 2y \\
            0 \\
        \end{cases}= \begin{cases}
            x+y \\
            0 \\
        \end{cases}\\独立
$$

# 极大似然估计与矩估计

$$
对于离散的X\backsim p(x;\theta),\{x_1,...,x_n\}是一次观察值,那么事件\{X_1=x_1,...,X_n=x_n \}发生的概率为\\L(\theta)=\prod_{i=1}^np(x;\theta)\\
似然函数L(\theta)、极大然估计值\hat\theta\{x_1,...,x_n\}、极大然估计量(MLE) \ \hat\theta\{X_1,...,X_n \}
\\为了求L(\theta)最大值可以求\ 对数似然函数:lnL(\theta)最大
\\lnL(\theta)=\sum_{i=1}^{n} x_i\cdot lnp+(n-\sum_{i=1}^{n}x_i)\cdot ln(1-p)
\\\frac{\partial lnL(\theta)}{\partial\theta}=\frac{\sum x_i}{\theta}-\frac{n-\sum x_i}{1-\theta}\\
\hat\theta_{MLE}=\frac{1}{n}\sum x_i\\
\color{yellow}{例题，若X\backsim(\mu,\sigma^2),求\mu,\sigma^2的极大似然估计}\\
$$

