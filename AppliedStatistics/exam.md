## 置信区间

### 单个正态总体均值的区间估计

$$
\text{$\sigma^2$已知 $\implies \bar X \pm Z_{\frac{\alpha}{2}}\frac{\sigma}{\sqrt n}$} \\

\text{$\sigma^2$未知 $\implies \bar X \pm T_{\frac{\alpha}{2},n-1}\frac{S}{\sqrt n}$}\\

\text{$\mu,\sigma^2$未知 $\implies \frac{(n-1)S^2}{\chi^2_{\frac{\alpha}{2},n-1}}<\sigma^2<\frac{(n-1)S^2}{\chi^2_{\frac{1-\alpha}{2},n-1}}$}\\
$$

### 两个正态总体参数的区间估计

$$
\text{$\sigma_x^2,\sigma_y^2$已知$\implies G=\frac{(\bar X-\bar Y)-(\mu_x-\mu_y)}{\sqrt{\frac{\sigma_x^2}{n_x}+\frac{\sigma_y^2}{n_y}}}\backsim N(0,1)$}\implies (\bar X-\bar Y)\pm Z_{\frac{\alpha}{2}}\sqrt{\frac{\sigma_x^2}{n_x}+\frac{\sigma_y^2}{n_y}}\\\\\\
\text{$\sigma_x^2=\sigma_y^2$未知}\implies \hat\sigma^2=S_w^2=\frac{(n_x-1)S_x^2+(n_y-1)S_y^2}{n_x+n_y-2}\\\implies
\frac{(\bar X-\bar Y)-(\mu_x-\mu_y)}{S_w\sqrt{\frac{1}{n_x}+\frac{1}{n_y}}}\backsim T_{n_x+n_y-2}\implies (\bar X-\bar Y)\pm T_{\frac{\alpha}{2},(n_x+n_y-2)}S_w\sqrt{\frac{1}{n_x}+\frac{1}{n_y}}\\\\\\
\text{$\sigma_x^2\not=\sigma_y^2$未知}\implies\begin{cases}
\frac{(\bar X-\bar Y)-(\mu_x-\mu_y)}{\sqrt{\frac{S_x^2}{n_x}+\frac{S_y^2}{n_y}}}\backsim N(0,1)\implies (\bar X-\bar Y)\pm Z_{\frac{\alpha}{2}}\sqrt{\frac{S_x^2}{n_x}+\frac{S_y^2}{n_y}}  & \text{if $n$ >30} \\
...\backsim T_k,k=min(n_x -1,n_y -1)\implies (\bar X-\bar Y)\pm T_{\frac{\alpha}{2},k}\sqrt{\frac{S_x^2}{n_x}+\frac{S_y^2}{n_y}}, & \text{if $n<30$} \\
\end{cases}
$$

# 假设验证

### 单个正态总体均值的假设检验

$$
双边假设:\\
统计量:Z_0=\frac{\bar X -\mu_0}{\sigma/\sqrt n},T_0=\frac{\bar X -\mu_0}{S/\sqrt n}\\
拒绝(大了就拒):|Z_0|\geq Z_{\frac\alpha2},|T_0|\geq T_{\frac\alpha2,n-1}\\
P\_(比\alpha小了就拒):P\_=2(1-\phi(|Z_0|)),P\_=2P\{T_{n-1}\geq|T_0|\}\\\\

单边假设:\\
拒绝:(Z_0\leq-Z_\alpha,Z_0\geq Z_\alpha),(T_0\leq-T_{\alpha,n-1},T_0\geq T_{\alpha,n-1})\\
P\_:(\phi(Z_0),1-\phi(Z_0)),(P\{T_{n-1}\leq T_0\},P\{T_{n-1}\geq T_0\})
$$

### 两个正态总体参数的假设检验

$$
双边假设:\\
\sigma_x\sigma_y已知\implies统计量:Z_0=\frac{\bar X -\bar Y}{\sqrt{\frac{\sigma_x^2}{n_x}+\frac{\sigma_y^2}{n_y}}},拒绝:|Z_0|\geq Z_{\frac\alpha2},P\_=2(1-\phi(|Z_0|))\\\\\\\\

\sigma_x=\sigma_y未知\implies\hat\sigma^2=S_w^2=\frac{(n_x-1)S_x^2+(n_y-1)S_y^2}{n_x+n_y-2}\\\implies 统计量:T_0=\frac{\bar X -\bar Y}{S_w\sqrt{\frac{1}{n_x}+\frac{1}{n_y}}}
拒绝:|T_0|\geq T_{\frac\alpha2,n_x+n_y-2},P\_=2P\{T_{n_x+n_y-2}\geq|T_0|\}\\\\\\\\

\sigma_x\not=\sigma_y未知\implies T_0=\frac{\bar X -\bar Y}{\sqrt{\frac{S_x^2}{n_x}+\frac{S_y^2}{n_y}}}\implies \begin{cases}
拒绝:|T_0|\geq Z_{\frac\alpha2},P\_=2(1-\phi(|T_0|)) &n>30\\
拒绝:|T_0|\geq T_{\frac\alpha2,k},P\_=2P\{T_{k}\geq|T_0|\}&n<30\\
\end{cases}\\
k=min(n_x-1,n_y-1)|k=\frac{(\frac{S_x^2}{n_x}+\frac{S_y^2}{n_y})^2}{\frac{(\frac{S_x^2}{n_x})^2}{n_x-1}+\frac{(\frac{S_y^2}{n_y})^2}{n_y-1}}
$$



### 方差检验


$$
\text{双边假设}\\
F=\frac{S_x^2}{S_y^2}\implies W=\{F\le F_{\frac{1-\alpha}{2},n_x-1,n_y-1}或者F> F_{\frac{\alpha}{2},n_x-1,n_y-1} \}\\
\text{单边假设}\\
F=\frac{S_x^2}{S_y^2}\implies W=\{F< F_{1-\alpha,n_x-1,n_y-1},F>F_{\alpha,n_x-1,n_y-1} \}
$$


# 拟合度优先检验

$$
拒绝:Q_{n-1}=\sum_{i=1}^n\frac{(x_i-\hat x_i)^2}{\hat x_i}
=\sum_{i=1}^n\frac{(样本值-期望值)^2}{期望值}
\geq \chi^2_{\alpha,n-r-1}
$$

