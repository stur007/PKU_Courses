import math
from scipy.optimize import minimize
from scipy.stats import chi2

r = 0.52e-6         
g = 9.80            
rho = 6.3           
T = 293             
R = 8.32            

z_values = [0, 6e-6, 12e-6, 18e-6]
n_values = [1880, 940, 530, 305]

C = 4 * math.pi * r**3 * rho * g / (3 * T)

def nu_z(nu0, k, z):
    return nu0 * math.exp(-C * z / k)

def chi_squared(params):
    k, nu0 = params
    total = 0.0
    for n, z in zip(n_values, z_values):
        nu = nu_z(nu0, k, z)
        total += 2 * (n * math.log(n / nu) + nu - n)
    return total

initial = [1.4e-23, 1000]
result = minimize(chi_squared, initial, method='Nelder-Mead')

k_fit, nu0_fit = result.x
chi2_min = result.fun
NA_fit = R / k_fit
dof = len(n_values) - 2
p_value = chi2.sf(chi2_min, dof)

print(f"P-value = {p_value:.4f}")
print(f"k = {k_fit:.4e} J/K")
print(f"nu_0 = {nu0_fit:.4f}")
print(f"chi^2 = {chi2_min:.4f}")
print(f"N_A = {NA_fit:.3e}")
print(f"p_value = {p_value:.4f}")