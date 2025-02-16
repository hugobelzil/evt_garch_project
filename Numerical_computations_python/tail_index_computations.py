# -*- coding: utf-8 -*-
"""tail_index_computations.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LY1C-oJoI9TE-A4xN8oAphkPJf6CBnNM
"""

import numpy as np
from scipy import integrate,stats

"""# ***Defining the functions to optimize***

see formulas in the notebook/writtent report

## ***Gaussian innovations***

Here, we assume $Z_t\sim\mathcal{N}(0,1)$
"""

def F_G(kappa,alpha_1,beta_1):
  def integrand(z):
    p = (alpha_1*(z)+beta_1)**(kappa/2)
    return p*(stats.chi2.pdf(z,df=1))
  integral,_ = integrate.quad(integrand,a=0,b=750) #b=np.inf also works but its better to use a high finite value for quad.integrate
  return integral

def d_F_G(kappa,alpha_1,beta_1):
  def integrand(z):
    p = (alpha_1*(z)+beta_1)**(kappa/2)
    q = 0.5*math.log(alpha_1*(z)+beta_1)
    return p*q*(stats.chi2.pdf(z,df=1))
  integral,_ = integrate.quad(integrand,a=0,b=750)
  return integral


def newtons_method_gauss(alpha_1,beta_1):
  max_iter = 1000     #these parameters can be changed according to your preferences
  epsilon = 10e-5
  kappa_not = 40     #integral will converge for any kappa_not
  iter=0
  flag=True

  while flag==True and iter<max_iter:
    prev_kappa = kappa_not
    kappa_not = kappa_not - ((F_G(kappa_not,alpha_1,beta_1)-1)/(d_F_G(kappa_not,alpha_1,beta_1)))
    iter+=1
    flag=(abs(kappa_not-prev_kappa)>=epsilon)
    #print(kappa_not) #comment out to avoid printing each value of the iteration
    if iter==max_iter:
      print(f"Newton's method did not converge within {max_iter} iterations for alpha1 = {alpha_1} and beta1 = {beta_1}")
      return None

  print(f"Convergence in {iter} iteration(s) to : ")
  return kappa_not

"""## ***Fitted parameters***"""

alpha_1_A = 0.0890
beta_1_A = 0.895
newtons_method_gauss(alpha_1_A,beta_1_A)

"""## ***Student-$t$ innovations***

We now assume $Z_t\sim t(\nu)$, for some $\nu>0$. Note that while we typically encounter $\nu \in \mathbb{N}$, we could have values of $\nu$ which could be non-integers here.  
"""

def F_t(kappa,alpha_1,beta_1,nu):
  def integrand(z):
    p = (alpha_1*(z**2)+beta_1)**(kappa/2)
    return p*(stats.t.pdf(z,df=nu,scale=np.sqrt((nu-2)/nu)))
  integral,_ = integrate.quad(integrand,a=-np.inf,b=np.inf) #b=np.inf also works but its better to use a high finite value for quad.integrate
  return integral

def d_F_t(kappa,alpha_1,beta_1,nu):
  def integrand(z):
    p = (alpha_1*(z**2)+beta_1)**(kappa/2)
    q = 0.5*np.log(alpha_1*(z**2)+beta_1)
    return p*q*(stats.t.pdf(z,df=nu,scale=np.sqrt((nu-2)/nu)))
  integral,_ = integrate.quad(integrand,a=-np.inf,b=np.inf)
  return integral

def newtons_method_student(alpha_1,beta_1,nu):
  max_iter = 1000     #these parameters can be changed according to your preferences
  epsilon = 10e-5
  kappa_not = nu-0.1
  iter=0
  flag=True

  while flag==True and iter<max_iter:
    prev_kappa = kappa_not
    kappa_not = kappa_not - ((F_t(kappa_not,alpha_1,beta_1,nu)-1)/(d_F_t(kappa_not,alpha_1,beta_1,nu)))
    iter+=1
    flag=(abs(kappa_not-prev_kappa)>=epsilon)
    #print(kappa_not) #uncomment to print each value of the iteration
    if iter==max_iter:
      print(f"Newton's method did not converge within {max_iter} iterations for alpha1 = {alpha_1} and beta1 = {beta_1}")
      return None

  print(f"Convergence in {iter} iteration(s) to : ")
  return kappa_not

"""## ***Fitted parameters***"""

alpha_1_B=0.065670
beta_1_B=0.916909
nu_B=6.318297
newtons_method_student(alpha_1=alpha_1_B,beta_1=beta_1_B,nu=nu_B)

"""# ***Generalized Hyperbolic innovations***

The GH random variable has the following p.d.f. : \\

$$
f_X(x; \lambda, a, b) =
\frac{(a^{2} - b^{2})^{\frac{\lambda}{2}}}{\sqrt{\pi}\,2^{\lambda-1} a^{\lambda} K_{\lambda}(\sqrt{a^{2}-b^{2}})}
\left(\frac{\sqrt{1 + x^{2}}}{a}\right)^{λ - \tfrac{1}{2}}
e^{b x}
K_{\lambda-\frac{1}{2}}\bigl(a \sqrt{1 + x^{2}}\bigr)
$$

\\

where $K_\lambda(⋅)$ denotes the modified Bessel function of the second kind. Fortunately, SciPy.stats contains all the implementation we need for the numerical computations of this distribution. Note that $\texttt{RUgarch}$ and $\texttt{SciPy}$ use different parametrizations which we have to take into account and undo before proceed to computations

"""

#bessel function for reparameterization
from scipy.special import kv

alpha_1 = 0.066449
beta_1 = 0.917172

#RUGarch parameters (change your parameters here)
zeta = 0.250040 #'shape' in the rugarch output
rho=-0.960222 #'skew' in the rugarch output
lam=-3.970268 #'ghlambda', which is 'p' in scipy

K_lam=kv(lam,zeta) #bessel function computations
K_lam_plus_1=kv(lam+1,zeta)
K_lam_plus_2=kv(lam+2,zeta)

#calculations for delta
ratio1 = K_lam_plus_1/(zeta*K_lam)
ratio2 = K_lam_plus_2/K_lam
ratio3 = (K_lam_plus_1/K_lam)**2

#according to rugarch documentation page 21
inside = ratio1+((rho**2)/(1-(rho**2)))*(ratio2-ratio3)
delta_temp = inside**(-0.5)

#the parameters below correspond to the 'standard' parameters
alpha=zeta/(delta_temp*np.sqrt(1-rho**2))
beta=alpha*rho
delta=zeta/(alpha*np.sqrt(1-rho**2))
mu=(-beta*(delta**2)*K_lam_plus_1)/(zeta*K_lam)

#Below are these parameters
print("Alpha =", alpha)
print("Beta =", beta)
print("Delta =", delta)
print("Mu =", mu)
print("Lambda =",lam)

def F_ghyp(kappa, alpha_1, beta_1, p, a, b, loc, scale):
    def integrand(z):
        power_term = (alpha_1*(z**2) + beta_1)**(kappa/2)
        pdf_val = stats.genhyperbolic.pdf(z, p, a, b, loc=loc, scale=scale)
        return power_term * pdf_val
    integral, _ = integrate.quad(integrand, -np.inf, np.inf)
    return integral

def d_F_ghyp(kappa, alpha_1, beta_1, p, a, b, loc, scale):
    def integrand(z):
        power_term = (alpha_1*(z**2) + beta_1)**(kappa/2)
        q = 0.5 * math.log(alpha_1*(z**2) + beta_1)
        pdf_val = stats.genhyperbolic.pdf(z, p, a, b, loc=loc, scale=scale)
        return power_term * q * pdf_val
    integral, _ = integrate.quad(integrand, -np.inf, np.inf)
    return integral

def newtons_method_genhyp(alpha_1, beta_1, p, a, b, loc, scale):
    max_iter=1000
    epsilon=1e-5
    kappa_not=10
    iter_count=0
    flag=True

    while flag and iter_count<max_iter:
        prev_kappa = kappa_not
        kappa_not = kappa_not - (((F_ghyp(kappa_not,alpha_1,beta_1,p,a,b,loc,scale) - 1))/d_F_ghyp(kappa_not,alpha_1,beta_1,p,a,b,loc,scale))
        iter_count += 1
        flag = (abs(kappa_not-prev_kappa)>=epsilon)

        if iter_count==max_iter:
            print(f"Newton's method did not converge within {max_iter} iterations for alpha_1 = {alpha_1} and beta_1 = {beta_1}")
            return None

    print(f"Convergence in {iter_count} iteration(s) to : ")
    return kappa_not

#Careful! Scipy's parametrization is different:
result = newtons_method_genhyp(alpha_1,beta_1,p=lam,a=(alpha*delta),b=beta*delta,loc=mu,scale=delta)
print("Result:", result)

"""# ***Checking Mikosch and Starica assumptions***"""

nu = 6.318    #change your parameters here
alpha_1 = 0.05 #these are arbitrary parameters
beta_1 = 0.95

#this function below computes the value of E[lnA] for t distributed innovations
def mikosch_and_starica_assumption(z,alpha_1=alpha_1,beta_1=beta_1,nu=nu):
  return (np.log(alpha_1*(z**(2))+beta_1)*stats.t.pdf(z,df=nu,scale=np.sqrt((nu-2)/nu))) #change alpha_1, beta_1 and nu accordingly
a = integrate.quad(mikosch_and_starica_assumption,a=-np.inf,b=np.inf)

#a[0] is the computed approximation of E[lnA], a[1] is a bound of error
if a[0]>0:
  print(f"Mikosch and Starica conditions do not hold, E[ln(A)] = {round(a[0],5)} > 0")
else:
  print(f"Mikosch and Starica conditions hold : E[ln(A)] = {round(a[0],5)} < 0")