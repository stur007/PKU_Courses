from scipy.optimize import minimize
from scipy.stats import chi2

hs     = [1000, 828, 800, 600, 300]
ds     = [1500, 1340, 1328, 1172, 800]
sigma  = 15

def f(alpha, d, h):
    return (d - alpha * h) ** 2 / sigma ** 2

def g(alpha, beta, d, h):
    return (d - alpha * h - beta * h ** 2) ** 2 / sigma ** 2

def s(alpha, beta, d, h):
    return (d - alpha * h ** beta) ** 2 / sigma ** 2

def t(alpha, d, h):
    return (d - alpha * h ** 0.5) ** 2 / sigma ** 2

def chi_squared_f(params):
    alpha = params
    return sum(f(alpha, d, h) for d, h in zip(ds, hs))

def chi_squared_g(params):
    alpha, beta = params
    return sum(g(alpha, beta, d, h) for d, h in zip(ds, hs))

def chi_squared_s(params):
    alpha, beta = params
    return sum(s(alpha, beta, d, h) for d, h in zip(ds, hs))

def chi_squared_t(params):
    alpha = params
    return sum(t(alpha, d, h) for d, h in zip(ds, hs))

# Model f
result_f  = minimize(chi_squared_f, [1], method='Nelder-Mead')
f_alpha   = result_f.x[0]
chi2_min  = result_f.fun
p_value_f = chi2.sf(chi2_min, df=4)
print(f'f:d=alpha h\nalpha = {f_alpha:.4f}, chi2 = {chi2_min:.2f}, p = {p_value_f:.4e}')

# Model g
result_g  = minimize(chi_squared_g, [1, 1], method='Nelder-Mead')
g_alpha, g_beta = result_g.x
chi2_min  = result_g.fun
p_value_g = chi2.sf(chi2_min, df=3)
print(f'g:d=alpha h + beta h ^2\nalpha = {g_alpha:.4f}, beta = {g_beta:.4f}, chi2 = {chi2_min:.2f}, p = {p_value_g:.4e}')

# Model s
result_s  = minimize(chi_squared_s, [1, 1], method='Nelder-Mead')
s_alpha, s_beta = result_s.x
chi2_min  = result_s.fun
p_value_s = chi2.sf(chi2_min, df=3)
print(f's:d = alpha h^beta\nalpha = {s_alpha:.4f}, beta = {s_beta:.4f}, chi2 = {chi2_min:.2f}, p = {p_value_s:.4e}')

# Model t
result_t  = minimize(chi_squared_t, [1], method='Nelder-Mead')
t_alpha   = result_t.x[0]
chi2_min  = result_t.fun
p_value_t = chi2.sf(chi2_min, df=4)
print(f't:d = alpha sqrt(h)\nalpha = {t_alpha:.4f}, chi2 = {chi2_min:.2f}, p = {p_value_t:.4e}')
