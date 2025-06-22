from scipy.optimize import minimize
from scipy.stats import chi2
from math import sin, asin, pi

theta_i = [10, 20, 30, 40, 50, 60, 70, 80]
theta_r = [8, 15.5, 22.5, 29, 35, 40.5, 45.5, 50]
sigma = 0.5

def f(r, i, alpha):
    return (r-alpha*i)**2/sigma**2

def g(r, i, alpha, beta):
    return (r-alpha*i+beta*i**2)**2/sigma**2

def h(r, i , alpha):
    return (r-asin(sin(i)/alpha))**2/(sigma*pi/180)**2

def chi_squared_f(params):
    alpha = params[0]
    return sum(f(r, i, alpha) for r, i in zip(theta_r, theta_i))

def chi_squared_g(params):
    alpha, beta = params
    return sum(g(r, i, alpha, beta) for r ,i in zip(theta_r, theta_i))

def chi_squared_h(params):
    alpha = params[0]
    return sum(h(r*pi/180, i*pi/180, alpha) for r, i in zip(theta_r, theta_i))

result_f  = minimize(chi_squared_f, [1], method='Nelder-Mead')
f_alpha   = result_f.x[0]
chi2_min  = result_f.fun
p_value_f = chi2.sf(chi2_min, df=7)
print(f'f:theta_r=alpha theta_i\nalpha = {f_alpha:.4f}, chi2 = {chi2_min:.2f}, p = {p_value_f:.4e}')

result_g  = minimize(chi_squared_g, [1, 1], method='Nelder-Mead')
f_alpha, f_beta = result_g.x
chi2_min  = result_g.fun
p_value_g = chi2.sf(chi2_min, df=6)
print(f'g:theta_r = alpha theta_i - beta theta_i^2\nalpha = {f_alpha:.4f}, beta = {f_beta:.4f}, chi2 = {chi2_min:.2f}, p = {p_value_g:.4e}')

result_h  = minimize(chi_squared_h, [1.5], method='Nelder-Mead')
f_alpha   = result_h.x[0]
chi2_min  = result_h.fun
p_value_h = chi2.sf(chi2_min, df=7)
print(f'h:theta_r = arcsin(sin(theta_i)/alpha)\nalpha = {f_alpha:.4f}, chi2 = {chi2_min:.2f}, p = {p_value_h:.4e}')