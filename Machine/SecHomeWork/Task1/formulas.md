$$
if\ we \ have \ f(X)=a^TX \\
f(X)=a^TX = \sum_{i=1}^n \ a_i X_i \\
so \ \frac {\partial f(X)}{\partial X_j}=
\frac {\partial}{\partial X_j}(\sum_{i=1}^n \ a_i X_i)
\\
so \ \frac{df(x)}{dX}=a
$$

$$
\frac {\partial Tr(ABC)}{\partial A}=\frac {\partial Tr(ABC)}{\partial ABC} \cdot \frac {\partial ABC}{\partial A}=1 \cdot \frac {\partial ABC}{\partial A}
\\\frac {\partial ABC}{\partial A}=\frac {\partial (AB)C}{\partial A}=\frac {\partial AB}{\partial A} \cdot C
\\  if\ A=\left[ 
\begin{array}{cc}
		A_{11} & A_{12} \\
        A_{21} & A_{22}  \\
    \end{array}  \right]
  \\  if\ B=\left[ 
\begin{array}{cc}
		B_{11} & B_{12} \\
        B_{21} & B_{22}  \\
    \end{array}  \right]
    \\AB=\left[ 
\begin{array}{cc}
		A_{11}B_{11}+A_{12}B_{21} & 			A_{11}B_{12}+A_{12}B_{22} \\
        A_{21}B_{11}+A_{22}B_{21} & A_{21}B_{12}+A_{22}B_{22}  \\
    \end{array}  \right]
    \\ so  \ \frac {\partial (A_{11}B_{11}+A_{12}B_{21})}{\partial A_{ij}}=        \begin{cases}
            B_{11},  & \text{$i=1,j=1$} \\
            B_{21}, & \text{$i=1,j=2$} \\
            0, & \text{other} \\
        \end{cases}
   \\ \therefore \frac {\partial AB}{\partial A} \cdot C=B^TC
$$

