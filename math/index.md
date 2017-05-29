## Bayes therom
$$
P(X)=\sum_{y}{P(X,Y)}\\
P(Y|X)P(X)=P(Y, X)=P(X, Y)=P(X|Y)P(Y) \\
P(Y|X) = \frac{P(Y, X)}{P(X)}=\frac{P(X, Y)}{P(X)}=\frac{P(X|Y)P(Y)}{P(X)} \\
P(y_i|x_0) = \frac{P(x_0|y_i)P(y_i)}{P(x_0)}=\frac{P(x_0|y_i)P(y_i)}{\sum_{j}{P(x_0, y_j)}}=\frac{P(x_0|y_i)P(y_i)}{\sum_{j}{P(x_0|y_j)P(y_j)}}\\
\sum_k{P(y_k|x_0)}=\sum_{k}{\frac{P(x_0|y_k)P(y_k)}{P(x_0)}}=\frac{\sum_{k}{P(x_0|y_k)P(y_k)}}{P(x_0)}=\frac{\sum_{k}{P(x_0|y_k)P(y_k)}}{\sum_{j}{P(x_0|y_j)P(y_j)}}=1
$$

