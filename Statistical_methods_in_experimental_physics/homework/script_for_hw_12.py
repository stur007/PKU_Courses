from scipy.stats import chi2
import matplotlib.pyplot as plt
import numpy as np

n = 5
xi_hat = 1.0
alpha = 0.159
beta = 0.159

def u_alpha(x):
    return x/(2*n)*chi2.ppf(1-alpha, 10)

def u_beta(x):
    return x/(2*n)*chi2.ppf(beta, 10)

x = np.linspace(0.01, 2, 1000)

plt.plot(x, u_alpha(x), label = 'u_alpha(xi)', color = 'blue')
plt.plot(x, u_beta(x), label =  'u_beta(xi)', color = 'orange')
plt.xlabel('xi')
plt.ylabel('u(xi)')
plt.axhline(1, label=f'xi_hat = {xi_hat}', color = 'green')
a = 2*n*xi_hat/chi2.ppf(1-alpha, 10)
b =  2*n*xi_hat/chi2.ppf(beta, 10)
plt.scatter([a, b], [1, 1], color='red', zorder=5)
plt.text(a, 1.02, f'a = {a:.3f}', ha='center', color='red')
plt.text(b, 1.02, f'b = {b:.3f}', ha='center', color='red')
plt.legend()
plt.savefig('9.2.png')
print(f'a = {a}, b = {b}')