# 1

## 1-1

$$
(\N,+)\ \ is\ \ \ Group?\\
1.Closure:\forall a,b\in \N \implies a+b \in \N\\
2.Associativity:\forall a,b,c\in \N\implies (a+b)+c=a+(b+c)\\
3.Identity\ ele:\exists e\in \N,\forall a\in \N\implies a+e=e+a=a\\
e=0\implies a+0=0+a=a\\
4.Inverse\ ele:\forall a\in \N,\exists b\in \N\implies a+b=b+a=e\\
e=0,b=a^{-1}=(-a)\implies a+(-a)=(-a)+a=0\\
\because\ (-a)\notin\N \\
\therefore (\N,+)\ \ is\ not \ Group
$$

## 1-2

$$
(\C,*)\ \ is\ \ \ Group?\\
1.Closure:\forall a,b\in \C \implies a \cdot b \in \C\\
2.Associativity:\forall a,b,c\in \C\implies (a\cdot b)\cdot c=a\cdot(b\cdot c)\\
3.Identity\ ele:\exists e\in \C,\forall a\in \C\implies a\cdot e=e\cdot a=a\\
e=1\implies a\cdot 1=1\cdot a=a\\
4.Inverse\ ele:\forall a\in \C,\exists b\in \C\implies a\cdot b=b\cdot a=e\\
e=1,b=a^{-1}=\frac{1}{a}=\frac{1}{m+ni}=\frac{m-ni}{m^2+n^2}\in \C \\ \implies a\cdot\frac{1}{a}=\frac{1}{a}\cdot a=1\\
but\ when\ a=0+0i,\ \frac{1}{a}= \frac{0-0i}{0}is\ no\ mathematical\ meaning\\

\therefore (\C,*)\ \ is\ not \ Group
$$

# 2

$$
352^{169}\equiv x\ mod \ 17\\
\because\phi(p^m)=p^m-p^{m-1}\\
\therefore\phi(p)=p-1\\
\therefore\phi(17)=16\\
\because352\equiv12\ mod \ 17 ,且a^{\phi(p)}\equiv1\ mod\ p\\
\therefore12^{\phi(17)}=12^{16}\equiv1\ mod\ 17\\
\therefore352^{169}\equiv12^{169}=12^{13\cdot 13}\equiv12^{(-3)\cdot(-3)}\equiv12^9 \ mod\ 17\\\equiv(-5)^9\equiv25\cdot 25\cdot 25\cdot 25\cdot (-5)\equiv8\cdot8\cdot8\cdot8(-5)\\\equiv64\cdot64\cdot(-5)\equiv(-4)\cdot(-4)\cdot(-5)\equiv(-1)\cdot(-5)\equiv5\ mod \ 17
$$

# 3

## 3-1

$$
Z^*_{11}=[\overline{1},...,\overline{11}]\\
\overline{7}^{-1}: \ 7\cdot x\equiv1\ mod \ 11\\
\implies7\cdot x-1=11\cdot k
\\\implies7\cdot x-11\cdot k=1\\
11\div7=1……4  \implies11-7\times1=4 \ \   ①     \\
7\div4=1……3  \implies7-4\times1=3   \ \    ②   \\
4\div3=1……1     \implies4-3\times1=1 \ \  ③   \\
\implies^{① ② 带入③ }\ \ 4-(7-4\times1)\times1=1\implies(11-7\times1)-(7-4\times1)\times1=1\\
\implies11-7-7+11-7=1\implies2\times11-3\times7=1\\
\implies        \begin{cases}
            k=-2   \\
            x=-3 \equiv-3\ mod\ 11\equiv 8\ mode\ 11 \\
        \end{cases}
$$

## 3-2

$$
Z^*_{19}=[\overline{1},...,\overline{18}]\\
\overline{9}^{-1}: \ 9\cdot x\equiv1\ mod \ 19\\
\implies9\cdot x-1=19\cdot k
\\\implies9\cdot x-19\cdot k=1\\
19\div9=2……1  \implies19-9\times2=1 \ \        \\


\implies        \begin{cases}
            k=-1   \\
            x=-2 \equiv-2\ mod\ 19\equiv 17\ mode\ 19 \\
        \end{cases}
$$

# 4

$$
Jacobi \ symbol\ (\frac{383}{507})
\\可能用到的公式:(\frac{m}{n})=(-1)^{\frac{m-1}{2}\cdot\frac{n-1}{2} }(\frac{n}{m});(\frac{-1}{n})=(-1)^{\frac{n-1}{2} };(\frac{2}{p})= \begin{cases}
            1 \ \ \  ,p\equiv1,7\ mod\ 8  \\
            -1,p\equiv3,5\ mod\ 8  \\
        \end{cases}
 \\
 (\frac{383}{507})=(\frac{383}{3\times13^{2}})=(\frac{383}{3})\cdot(\frac{383}{13})^2\\
 383\div3=127……2\implies383\equiv2 \ mod\ 3\equiv-1\ mod\ 3\\
  383\div13=29……6\implies383\equiv6 \ mod\ 13\\
  \therefore(\frac{383}{3})=(\frac{2}{3})=(\frac{-1}{3})=-1\\
   \therefore(\frac{383}{13})=(\frac{6}{13})=(-1)^{\frac{6-1}{2}\cdot\frac{13-1}{2} }(\frac{13}{6})=(-1)(\frac{13}{6})\\
   13\div6=2……1\implies13\equiv1 \ mod\ 6\\
   \therefore(\frac{383}{13})=(-1)(\frac{13}{6})=(-1)(\frac{1}{6})=(-1)(1)=-1\\
   \therefore(\frac{383}{507})=(\frac{383}{3})\cdot(\frac{383}{13})^2=(-1)\times(-1)^2=-1
$$

# 5

## 5-1

$$
罗宾:已知C\equiv21^2\ mod \ 35 ，求M^2\equiv21 \ mod \ 35
\\key=35=5\times7\\
①先求M^2\equiv21 \ mod \ 5\\
\because 21\equiv1 \ mod \ 5\\
\therefore M^2\equiv21 \ mod \ 5\equiv1 \ mod \ 5\implies        \begin{cases}
            M=-1\ mod \ 5\equiv4 \ mod \ 5  \\
            M=1 \ mod \ 5 \\
        \end{cases}\\
②再求M^2\equiv21 \ mod \ 7\\
\because 21\equiv0 \ mod \ 7\\
\therefore M^2\equiv0 \ mod \ 7\implies M\equiv0 \ mod \ 7\\
③CRT:\\
\begin{cases}
            M=-1\ mod \ 5 \\
            M=0 \ mod \ 7 \\
        \end{cases} or\begin{cases}
            M=4\ mod \ 5 \\
            M=0 \ mod \ 7 \\
        \end{cases}\\
        \implies\begin{cases}
            M-5n=1 \\
            M=7k \\
        \end{cases} \ or \ \begin{cases}
            M-5n=4 \\
            M=7k \\
        \end{cases}\\
                \implies\begin{cases}
            7k-5n=1 \\
            
        \end{cases} \ or \ \begin{cases}
			7k-5n=4 \\
        \end{cases}\\
 
 计算7k-5n=1如下：\\
 \begin{cases}
			 7\div5=1……2\implies 7-5\times 1=2 \\
			 5\div2=2……1 \implies 5-2\times 2=1 \\
        \end{cases}\implies 5-2\times(7-5)=1\\\implies \begin{cases}
            k=-2\equiv-2 \ mod \ 5\equiv3 \ mod \ 5 \\
            n=-3 \\
        \end{cases}\implies M=3\times7=21\\
  计算7k-5n=4如下：\\
 \begin{cases}
			 7\div5=1……2\implies 7-5\times 1=2 \\
			 5\div2=2……1 \implies 5-2\times 2=1 \\
        \end{cases}\implies 5-2\times(7-5)=1\\\implies 4\times(5-2\times(7-5))=4\times1
        \implies\begin{cases}
            k=-8\equiv-8 \ mod \ 5\equiv-3 \ mod \ 5\equiv2 \ mod \ 5 \\
            n=-12 \\
        \end{cases}\\\implies M=2\times7=14\\
   综上M=21\ or\ 14
$$

## 5-2

$$
RSA:已知C\equiv19^5\ mod \ 21 ，求19\equiv C^d \ mod \ 21
        \\
        1.key=21=3\times7\\
        2.\phi(n)=\phi(21)=\phi(3)\cdot\phi(7)=12\\
        3.5\cdot d\equiv1\ mod\ 12\implies5\cdot d-1=12\cdot k\implies5\cdot d-12\cdot k=1
        \\\implies \begin{cases}
			 12\div5=2……2\implies 12-5\times 2=2 \\
			 5\div2=2……1 \implies 5-2\times 2=1 \\
        \end{cases}\implies 5-2\times(12-5\times2)=1\\\implies5\times5-2\times12=1
        \implies\begin{cases}
			d=5 \\
			k=2 \\
        \end{cases}\\
        且C\equiv19^5\ mod \ 21=-2\cdot-2\cdot-2\cdot-2\cdot19=16\cdot19=(-5)\cdot(-2)=10\\
        所以解密为19\equiv 10^5 \ mod \ 21
$$

