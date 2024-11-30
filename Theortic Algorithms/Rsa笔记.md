$$
g(p^m)=p^m - p^{m-1}
$$

$$
1)GCD(a,b)=1 \ \ \ g(ab)=g(a)*g(b)\\

2)g(99)=g(33)g(3)=g(11)g(9)=10 * 6\\

3)g(318509)=g(431)*g(739)\\
$$






$$
A^{g(x)}=1(mod\ n )=A^{g(x)} -1 \\   A^{p-1}=1(mod\ p )
$$

$$
1)GCD(2,5)\\=1 \\ =>  2^{g(x)}=1(mod \ 5) \\ => 2^4=16=1(mod \ 5)\\

2)52^1205\\ => 找到一个x使得 \ \ \   52^1205 = x(mod 9)\ \ \  x 属于 [0,8] \\

52^g(9) =1(mod\ 9 )  => 52^6=1(mod 9)\\

1205=200*6+5  => 52^{1205} = 52^5 * (52^6)^{200} \\

其中52=7(mod\ 9)=-2(mod \ 9)   \\ => 52^5=(-2)^5 =-32=4(mod \ 9)\\

or \\ => 52^5 = 7^5 = 49* 49 * 7=4* 4 * 7 =16 * 7 =7 * 7=4(mod 9) \\

所以 x = 4
$$


$$
3)352^{169}=?(mod\ 17) \\

352^{g(17)}=12(mod\ 17) \\ => 12^{169}=?(mod\ 17) \\=> 12^{g(17)}=1(mod\ 17) \\=> 12^{16}=1(mod\ 17) \\

12^{169} = 12^{(13 *13 )} = 12 ^{( -3 * -3)} = 12^9 \\= (-5)^9 = (-5)(-5) (-5)(-5) (-5)(-5) (-5)(-5)    (-5)  \\= 8 * 8 * 8 * 8 *(-5) \\

= 64 * 64 *(-5)* \\ =  (-4) (-4) (-5)\\=  (-1) (-5)\\ = 5
$$

$$
N=q * p  \\ GCD(L_1 , (q-1)(p-1))=1 

\\find  \ d  \\ L_d= 1(mod \ (q-1)(p-1))\\
x^{L_d} = x(mod\ N) <=> \ \ x^{L_d}=x(mod\ p)  \ \ \ \  x^{L_d}=x(mod \ q)
\\ GCD(x,N)=1\ \  =>\ \ \ x∈ Z_n^*
$$

$$
g(f(X))=X=X(mod \ N)\\
x => x^l≡y=>y^d≡x(mod\ N)\\

\\if\ h(x_1)=h(x_2) \ \ \ \ \ so\ \ x_1=x_2
\\
\\f: Z_n^* =>Z_n^* \ and \ \ \ a=> a^l
\\g: Z_n^* =>Z_N^* \ and \ \ \ b=> b^d
\\g(f(X))=f(g(X))
\\证明:由于\ x∈[0，N] \ \ \ \ \ GCD(x,N)=1\ \  \ \ y≡x^l(mod\ N)\\
可以找到一个x∈[x_i,y_i] \ 当x∈[0，N] \ y_i=x_i^l(mod \ N)\\
(x_1,y_1),……,(x_s,y_s) => y_s=x_s^l(mod \ N)\\
y≡y_1^{t_1},……,y_s^{t_s}(mod\ N) \ \ \ (t_1,……,t_s≥0) \\
x≡y^d(mod\ N)\\
x≡y^d≡(y_1^{t_1},……,y_s^{t_s})^d(mod\ N)\\
not \ end
$$

$$
GCD(x,N)=1\ \ ,
y≡x^l(mod\ N)\ , y∈(0，N)\\
let\ y₁≡y\\
let\ y₂≡y₁^l(mod\ N)\\
let\ y₃≡y₂^l(mod\ N)\\
y_i≡y_{i-1}^l(mod\ N)\\
y_i≡y^{l^{i-1}}(mod\ N)\\
y_i≡y(mod\ N)\\
y^{l^{i-1}}≡y(mod\ N)\\
(y^{l^{i-2}})^l≡x^l(mod\ N)\\
so \ x=y^{l^{i-2}}(mod\ N)
$$

$$
g^n=1 \ \ \ \ n不存在, ord(g)=∞ \\
Examples\ 1) \\ord(1)=1 \\
ord(-1)=2
\\ (-1)^1=-1≠1 ,(-1)^2=1
\\ord(5)=∞
\\5^n=1
\\Examples\ 2)
\\Z_5^*=[_1^-,_2^-,_3^-,_4^-]
\\ord(_1^-)=1
\\ord(_2^-)=4
\\【(_2^-)^1 ≠_1^-】
\\【(_2^-)^2=_4^- ≠_1^-】
\\【(_2^-)^3=_8^- =_3^-】
\\【(_2^-)^4=_{16}^- =_1^-】
\\ord(_3^-)=4
\\ord(_4^-)=2
\\这里指的是Z_5^* 的元素的几次方可以被5求余后等于1
$$

$$
GCD(l,Ф(N))=1 \ \ \ => _l^- ∈Z_{Ф(N)}^*
\\证明如下\\
∵GCD(m,n)=1
\\∴ \ _m^- ∈Z_{n}^*
\\实际上，如果G是个有限的群组，且g∈G ，那么ord(g)_|^| |G|
\\\ \ Z_{n}^*是有限的
\\若 m=ord(_l^-)=>\\(_l^-)^m=(_1^-)<=>l^m=1(mod \ Ф(N) )
\\=>l^m-1=kФ(N) \ (k∈Z)
\\∴ y^{l^m-1}=1(mod \ N)
\\=>y^{l^m}=y(mod \ N)
\\如果m比通过加密找到的x小，那么RSA加密系统的l将有极其大的秩在Z_{n}^*内
\\y^{l^m-1}=y^{kФ(N)}=(y^{Ф(N)})^k=1(mod N)
\\
\\综上 \ \ GCD(x,n)=1\ 且\ y=x^l(mod \ N),x=y^d(mod N) 
\\ =>GCD(y,N)=1 \ =>y^{kФ(N)}=1(mod N)
$$

$$
计算雅可比符号 \(\left( \frac{383}{507} \right)\) 需要详细运用雅可比符号的性质，包括分解分母、利用乘法性以及利用二次互反律。以下是详细的计算步骤：

 步骤 1：分解分母 \(507\)

首先，将分母 \(507\) 分解为素数的幂：

\[
507 = 3 \times 13^2
\]

因此，雅可比符号可以分解为：

\[
\left( \frac{383}{507} \right) = \left( \frac{383}{3} \right) \times \left( \frac{383}{13} \right)^2
\]

 步骤 2：计算 \(\left( \frac{383}{3} \right)\)

我们需要计算 \(\left( \frac{383}{3} \right)\)。首先，计算 \(383\) 除以 \(3\) 的余数：

\[
383 \div 3 = 127 \quad \text{余} \quad 2 \quad \Rightarrow \quad 383 \equiv 2 \pmod{3}
\]

因此：

\[
\left( \frac{383}{3} \right) = \left( \frac{2}{3} \right)
\]

根据雅可比符号对于 \( (2/3) \) 的计算规则：

\[
\left( \frac{2}{3} \right) = (-1)^{\frac{3^2 - 1}{8}} = (-1)^{1} = -1
\]

所以：

\[
\left( \frac{383}{3} \right) = -1
\]

 步骤 3：计算 \(\left( \frac{383}{13} \right)\)

接下来，计算 \(\left( \frac{383}{13} \right)\)。首先，计算 \(383\) 除以 \(13\) 的余数：

\[
383 \div 13 = 29 \quad \text{余} \quad 6 \quad \Rightarrow \quad 383 \equiv 6 \pmod{13}
\]

因此：

\[
\left( \frac{383}{13} \right) = \left( \frac{6}{13} \right)
\]

将 \(6\) 分解为素数因子：

\[
6 = 2 \times 3
\]

所以：

\[
\left( \frac{6}{13} \right) = \left( \frac{2}{13} \right) \times \left( \frac{3}{13} \right)
\]

**计算 \(\left( \frac{2}{13} \right)\)：**

根据雅可比符号的性质：

\[
\left( \frac{2}{p} \right) = 
\begin{cases} 
1 & \text{如果 } p \equiv 1 \text{ 或 } 7 \pmod{8} \\
-1 & \text{如果 } p \equiv 3 \text{ 或 } 5 \pmod{8}
\end{cases}
\]

由于 \(13 \equiv 5 \pmod{8}\)，因此：

\[
\left( \frac{2}{13} \right) = -1
\]

**计算 \(\left( \frac{3}{13} \right)\)：**

使用二次互反律：

\[
\left( \frac{3}{13} \right) = \left( \frac{13}{3} \right) \times (-1)^{\frac{(3-1)(13-1)}{4}} = \left( \frac{1}{3} \right) \times (-1)^6 = 1 \times 1 = 1
\]

因此：

\[
\left( \frac{6}{13} \right) = (-1) \times 1 = -1
\]

\[
\left( \frac{383}{13} \right) = -1
\]

 步骤 4：综合计算 \(\left( \frac{383}{507} \right)\)

回到最初的分解：

\[
\left( \frac{383}{507} \right) = \left( \frac{383}{3} \right) \times \left( \frac{383}{13} \right)^2 = (-1) \times (-1)^2 = (-1) \times 1 = -1
\]

 最终结果

\[
\boxed{-1}
\]
$$

$$
一、罗宾加密（Rabin 加密）解密
给定信息：
公钥（n）: 35
密文（c）: 21
目标： 找到明文 ( m )，使得 ( m^2 \equiv c \pmod{n} )，即 ( m^2 \equiv 21 \pmod{35} )

步骤 1：分解公钥 ( n )\\
首先，将 ( n = 35 ) 分解为两个素数的乘积：\\
[
35 = 5 \times 7
]

步骤 2：求解模 5 和模 7 的方程\\
我们需要分别在模 5 和模 7 下求解以下方程：\\

模 5 的方程：
[
m^2 \equiv 21 \pmod{5}
]
由于 ( 21 \equiv 1 \pmod{5} )，方程变为：
[
m^2 \equiv 1 \pmod{5}
]
这有两个解：
[
m \equiv \pm1 \pmod{5} \quad \Rightarrow \quad m \equiv 1 \pmod{5} \quad \text{或} \quad m \equiv 4 \pmod{5}
]

模 7 的方程：
[
m^2 \equiv 21 \pmod{7}
]
由于 ( 21 \equiv 0 \pmod{7} )，方程变为：
[
m^2 \equiv 0 \pmod{7}
]
只有一个解：
[
m \equiv 0 \pmod{7}
]

步骤 3：应用中国剩余定理（CRT）
我们现在有以下同余方程组：
[
\begin{cases}
m \equiv 1 \pmod{5} \
m \equiv 0 \pmod{7}
\end{cases}
\quad \text{或} \quad
\begin{cases}
m \equiv 4 \pmod{5} \
m \equiv 0 \pmod{7}
\end{cases}
]

第一个方程组：
设 ( m = 7k )
代入第一个方程：
[
7k \equiv 1 \pmod{5} \quad \Rightarrow \quad 2k \equiv 1 \pmod{5}
]
因此，
[
k \equiv 3 \pmod{5}
]
所以，
[
m = 7k = 7(5j + 3) = 35j + 21 \quad \Rightarrow \quad m \equiv 21 \pmod{35}
]
第二个方程组：
设 ( m = 7k )
代入第二个方程：
[
7k \equiv 4 \pmod{5} \quad \Rightarrow \quad 2k \equiv 4 \pmod{5} \quad \Rightarrow \quad k \equiv 2 \pmod{5}
]
所以，
[
m = 7k = 7(5j + 2) = 35j + 14 \quad \Rightarrow \quad m \equiv 14 \pmod{35}
]
步骤 4：总结解
因此，满足 ( m^2 \equiv 21 \pmod{35} ) 的明文 ( m ) 有两个解：
[
\boxed{m = 14 \quad \text{或} \quad m = 21}
]

二、RSA 解密
给定信息：
公钥（( n, e )）: ( n = 21 ), ( e = 5 )
密文（( c )）: 19
目标： 找到明文 ( m )，使得 ( m \equiv c^d \pmod{n} )，其中 ( d ) 是 ( e ) 关于 ( \varphi(n) ) 的逆元。

步骤 1：分解公钥 ( n )
首先，将 ( n = 21 ) 分解为两个素数的乘积：
[
21 = 3 \times 7
]

步骤 2：计算欧拉函数 ( \varphi(n) )
[
\varphi(21) = (3 - 1) \times (7 - 1) = 2 \times 6 = 12
]

步骤 3：计算私钥指数 ( d )
我们需要找到 ( d ) 满足：
[
e \times d \equiv 1 \pmod{12}
]
即：
[
5d \equiv 1 \pmod{12}
]
通过尝试，我们发现：
[
5 \times 5 = 25 \equiv 1 \pmod{12}
]
因此，
[
d = 5
]

步骤 4：解密密文
使用私钥指数 ( d = 5 )，计算明文 ( m )：
[
m \equiv c^d \pmod{n} = 19^5 \pmod{21}
]

为了简化计算，我们可以利用模运算性质：

计算 ( 19 \pmod{21} )：
[
19 \equiv 19 \pmod{21}
]

计算 ( 19^2 \pmod{21} )：
[
19^2 = 361 \equiv 361 - 17 \times 21 = 361 - 357 = 4 \pmod{21}
]

计算 ( 19^4 \pmod{21} )：
[
19^4 = (19^2)^2 = 4^2 = 16 \pmod{21}
]

计算 ( 19^5 \pmod{21} )：
[
19^5 = 19^4 \times 19 \equiv 16 \times 19 = 304 \equiv 304 - 14 \times 21 = 304 - 294 = 10 \pmod{21}
]

因此，明文 ( m ) 为：
[
\boxed{m = 10}
]
$$

