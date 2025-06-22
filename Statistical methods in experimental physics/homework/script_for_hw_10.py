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
        total += (n - nu)**2 / n
    return total

initial = [1.4e-23, 1000]
result = minimize(chi_squared, initial, method='Nelder-Mead', bounds = [(1e-25, None),  (1, None)])

k_fit, nu0_fit = result.x

print(f"k = {k_fit:.4e} J/K")
print(f"nu_0 = {nu0_fit:.4f}")