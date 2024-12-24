# 0

$$
F_{25}\subset\!\!\!\!\!^? \ \ \ F_{125}\\ F_{25}=F_{5^2},F_{125}=F_{5^3}\\2\nmid3\implies F_{25}\not\subset F_{125}\\\\
F_{25}\subset\!\!\!\!\!^? \ \ \ F_{625}\\F_{25}=F_{5^2},F_{625}=F_{5^4}\\2\mid4\implies yes\\\\
F_{19^2}\subset\!\!\!\!\!^? \ \ \ F_{2^{19}}\\19=char(F_{19^2})\not=char(F_{2^{19}})=2\implies no\\\\ \left[F_4:F_2 \right]=2\ (4=2^2)\\\left[F_{64}:F_4 \right]=3\ (64=4^3)\\
F_2\subset\!\!\!\!\!^{2} \ \ \ F_4\subset\!\!\!\!\!^3\ \ \ F_{64} (64=2^6)\\\\
扩展域F_{25}中3次域的元素数量?\\F_{25}\subset K,\left[K:F_{25} \right]=3\implies |K|=25^3\\\\
扩展域F_{81}中25次域的特征?\\F_{81}\subset K,F_{81}=F_{3^4}\subset F_{3}\implies char(K)=3\\\\
在F_3中找到次数为2的不可约多项式\\x^2+ax+b\ \ a,b\in F_3, b\not=0\\
\begin{array}{c|c}
    \mathrm{a,b} & x^2+ax+b & root(0,1,2) \\
    \hline \\
    0,1 & x^2+1 & no\\
    0,2 & x^2+2 & x=1,f(x)=0 mod 3\\
    1,1 & x^2+x+1 & x=1,f(x)=0 mod 3\\
    1,2 & x^2+x+2 & no\\
    2,1 & x^2+2x+1 & x=2,f(x)=0 mod 3\\
    2,2 & x^2+2x+2 & no \\
\end{array}\\\\
在F_2中找到次数为2，3的不可约多项式\\
x^2+ax+1\ \ a\in F_2\\
\begin{array}{c|c}
    \mathrm{a} & x^2+ax+1 & root(0,1) \\
    \hline \\
    0 & x^2+1 & x=1,f(x)=0 mod 2\\
    1 & x^2+x+1 & no\\
\end{array}\\\\
x^3+ax^2+bx+1\ \ a,b\in F_2\\
\begin{array}{c|c}
    \mathrm{a,b} & x^3+ax^2+bx+1 & root(0,1) \\
    \hline \\
    0,0 & x^3+1 & x=1,f(x)=0 mod 2\\
    0,1 & x^3+x+1 & no\\
    1,1 & x^3+x^2+x+1 & x=1,f(x)=0 mod 2\\
    1,0 & x^2+x^2+1 & no\\
\end{array}\\\\
$$

# 1

$$
F_{27}\sub \!\!\!\!\!^? \ \ F_{81}\\3^3=F_{27}\not\sub F_{81}=3^4\\\\
F_{7^5}\sub \!\!\!\!\!^? \ \ F_{3^{75}}\\char(F_{7^5})\not=char(F_{3^{75}})\implies F_{7^5}\not\sub F_{3^{75}}\\\\
F_{27}\sub K,\left[K:F_{27} \right]=5,char(K)=?\\
F_3\sub F_{27}\sub K \implies char(K)=3\\\\
\left[F_{81}:F_{9} \right]=?\\
81=9^2\implies  \left[F_{81}:F_{9} \right]=2\\\\
F_{25}\sub K,\left[K:F_{25} \right]=100,|K|=?\\|K|=25^{100}
$$

# 2

$$
\text{find an irreducible polynomial of degree 2 in }F_5(x)\\
$$


$$
\\\begin{array}{c|c}
    \mathrm{a,b} & x^2+ax+b & root(0,1,2,3,4) \\
    \hline \\
    0,1 & x^2+1 & x=2,3,f(x)=0 mod 5\\
    0,2 & x^2+2 & no\\
    0,3 & x^2+3 & no\\
    0,4 & x^2+4 & x=4,f(x)=0 mod 5\\
    1,1 & x^2+x+1 & no\\
    1,2 & x^2+x+2 & no\\
    1,3 & x^2+x+3 & x=1,3,f(x)=0 mod 5\\
    1,4 & x^2+x+4 & x=2,f(x)=0 mod 5\\
    2,1 & x^2+2x+1 & x=4,f(x)=0 mod 5\\
    2,2 & x^2+2x+2 & x=1,f(x)=0 mod 5 \\
    2,3 & x^2+2x+3 & no \\
    2,4 & x^2+2x+4 & x=2,f(x)=0 mod 5 \\
    3,1 & x^2+3x+1 & no\\
    3,2 & x^2+3x+2 & x=3,4,f(x)=0 mod 5 \\
    3,3 & x^2+3x+4 & no \\
    3,4 & x^2+3x+4 & no \\
    4,1 & x^2+4x+1 & no\\
    4,2 & x^2+4x+2 & no \\
    4,3 & x^2+4x+3 & x=2,4,f(x)=0 mod 5 \\
    4,4 & x^2+4x+4 & x=3,f(x)=0 mod 5 \\
\end{array}\\\\ \text{find has no root in}F_5 \implies f(x) \text{is irreducible in}F_5(x)
$$

# 3

$$
\text{How many roots does the polynomial $f(x)=x^3+2x+1 $ have, in the fields $F_{125},F_{625},F_{5^9}$ }
$$

$$
\left[F_{5^a}:F_5\right]=deg(f(x))=3 \\\implies |F_{5^a}|=5^3=125\\\implies F_{5^a}=F_{125}\\let \ F_5\sub K\\a\in K\iff F_{5^a}\sub K\iff F_{125}\sub K\\
F_{125}\sub F_{125}\implies\text{there 3 roots in $F_{125}$}\\
F_{125}\not\sub F_{625}\implies\text{there no roots in $F_{625}$}\\
F_{125}\sub F_{5^9}\implies\text{there 3 roots in $F_{5^9}$}\\
$$

$$
\text{How many roots does the polynomial $f(x)=x^3+3x^2+x+2 $ have, in the fields $F_{7^4},F_{7^4}$ }
$$

$$
\text{Find roots of f(x) in $F_7$}\\
\begin{array}{c|c}
    \mathrm{root} & \text{res} \\
    \hline \\
    0 &  f(x)=x^3+3x^2+x+2=2\\
    1 & f(x)=x^3+3x^2+x+2=7=0mod7 \\
    2 & f(x)=x^3+3x^2+x+2=24 \\
    3 & f(x)=x^3+3x^2+x+2=59 \\
    4 & f(x)=x^3+3x^2+x+2=118 \\
    5 & f(x)=x^3+3x^2+x+2=207 \\
    6 & f(x)=x^3+3x^2+x+2=362 \\
\end{array}\\
f(x)=(x-1)g(x)=(x-1)(x^2+4x+5)\implies \text{$g(x)$ is irreducible in $F_7(x)$}\\
\text{let $x_a$ be a root of g(x) in some bigger field }\\
\left[F_{7^a}:F_7\right]=deg(g(x))=2\implies F_{7^a}=F_{49}\\
F_7\sub K,a\in K\iff F_{49}\sub K\\
F_{49}\sub F_{7^4}\implies \text{g(x) has 2 roots in}\implies \text{f(x) has 3 roots in}\\
F_{49}\not\sub F_{7^5}\implies \text{g(x) has no roots in}\implies \text{f(x) has 1 roots in}
$$

 

# 4

$$
\text{Does the equation $y^2=x^3+2x+1$ define an elliptic curve over $F_5$}\\
y^2=f(x),deg(f)=3,defines \ an \ EC\iff f(x)\text{has no multiple rools}\\
\text{f(x) has no multiple rools}\iff GCD(f(x),f'(x))=1
\\\text{if f(x) is irreducile ,f(x) has no multiple roots}\\
\text{find roots of f(x) in $F_5$}\\
\begin{array}{c|c}
    \mathrm{root} & \text{res} \\
    \hline \\
    0 & f(x)= 1\\
    1 & f(x)= 3\\
    2 & f(x)= 13\\
    3 & f(x)= 34\\
    4 & f(x)= 73\\
\end{array}\implies\text{f(x) is irreducile}\implies\text{ f(x) has no multiple roots}
$$

$$
\text{Does the equation $y^2=x^3+3x^2+x+2$ define an elliptic curve over $F_7$}\\
y^2=f(x),deg(f)=3,defines \ an \ EC\iff f(x)\text{has no multiple rools}\\
\text{f(x) has no multiple rools}\iff GCD(f(x),f'(x))=1
\\\text{if f(x) is irreducile ,f(x) has no multiple roots}\\
\text{find roots of f(x) in $F_7$}\\
\begin{array}{c|c}
    \mathrm{root} & \text{res} \\
    \hline \\
    0 &  f(x)=x^3+3x^2+x+2=2\\
    1 & f(x)=x^3+3x^2+x+2=7=0mod7 \\
    2 & f(x)=x^3+3x^2+x+2=24 \\
    3 & f(x)=x^3+3x^2+x+2=59 \\
    4 & f(x)=x^3+3x^2+x+2=118 \\
    5 & f(x)=x^3+3x^2+x+2=207 \\
    6 & f(x)=x^3+3x^2+x+2=362 \\
\end{array}\\
f(x)=(x-1)g(x)=(x-1)(x^2+4x+5)\implies g(x)\text{not have root x=1}\\\implies \text{$g(x)$ is irreducible in $F_7(x)$}\\
\implies\text{f(x) is irreducile}\implies\text{ f(x) has no multiple roots}
$$

# 5

$$
EC \  E:y^2=f(x), deg(f)=3\\
\text{find point in $E(K)$ of order 2 ,$char(K)\not=2$}\\
P+P=O,P\not=O\iff P=-P\\
P=(x_0,y_0),-P=(x_0,-y_o)\\
P=-P\implies \begin{cases}
          x_0=x_0 \\
             y_0=-y_0 \implies y_0=0 \\
        \end{cases}\\
        \implies x_0\text{ is a root of f(x)}\\
        \text{that to find point of order 2 in E(K), we need to find roots of f(x) in K}\\
        \text{then points of order 2 have the following form}(x_0,0)
$$

$$
EC \  E:y^2=x^3+x ,\ over\ F_5\\
\text{find point in $E(F_5)$ of order 2}\\
\begin{array}{c|c}
    \mathrm{root} & \text{res} \\
    \hline \\
    0 &  f(x)=x^3+x=0 mod 5\\
    1 & f(x)=x^3+x=2 \\
    2 & f(x)=x^3+x=10= 0 mod 5\\
    3 & f(x)=x^3+x=30=0 mod 5 \\
    4 & f(x)=x^3+x=68 \\
\end{array}\\
\text{point of order 2 in $E(F_5)$ is(0,0)(2,0)(3,0)}
$$

$$
EC \  E:y^2=x^3+3x^2 +x+2,\ over\ F_7\\
\text{find point in $E(F_7)$ of order 2}\\
\begin{array}{c|c}
    \mathrm{root} & \text{res} \\
    \hline \\
    0 &  f(x)=x^3+3x^2+x+2=2\\
    1 & f(x)=x^3+3x^2+x+2=7=0mod7 \\
    2 & f(x)=x^3+3x^2+x+2=24 \\
    3 & f(x)=x^3+3x^2+x+2=59 \\
    4 & f(x)=x^3+3x^2+x+2=118 \\
    5 & f(x)=x^3+3x^2+x+2=207 \\
    6 & f(x)=x^3+3x^2+x+2=362 \\
\end{array}\\
\text{point of order 2 in $E(F_5)$ is(1,0)}
$$

