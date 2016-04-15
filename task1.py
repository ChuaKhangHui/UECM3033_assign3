import numpy as np
import sympy as sy

#Your optional code here
#You can import some modules or create additional functions
#def gauss_legendre(n):
#    k=sp.arange(1.0,n)       
#    a_band = sp.zeros((2,n)) 
#    a_band[1,0:n-1] = k/sp.sqrt(4*k*k-1) 
#    x,V=sp.linalg.eig_banded(a_band,lower=True) 
#    w=2*sp.real(sp.power(V[0,:],2)) 
#    return x, w
    
#def quad_gauss ( f , a , b , deg ) :
#    # get Gauss points for [-1,1]
#    [gx ,w] = gaussquad(deg) ;
#    # transform to [a,b]
#    x = 0.5∗(b−a ) ∗gx +0.5∗(a+b )
#    y = f ( x )
#    return 0.5∗(b−a ) ∗dot (w, y )

# DO NOT CHANGE THE NAME OF gausslegendre() function
def gausslegendre(f, a, b, n=20):
    
    [pt,weight] = np.polynomial.legendre.leggauss(n+1)
#    print (pt)
#    print (weight)
    
    pt = 0.5*(b-a) *pt +0.5*(a+b )
    y = f(pt)
    
    ans = (0.5*(b-a) *np.dot(weight, y ))
    
    return ans

if __name__ == "__main__":
    def f(x):
        return (x**2 +7*x)/(1 +np.sqrt(x))**4
    
    def my_integral():
        x = sy.Symbol('x')
        ans = sy.integrate((x**2 +7*x)/(1 +sy.sqrt(x))**4, (x,0, 1))
        return ans
    
    print('Answer:                    I = ', my_integral())
    print('Your implementation gives: I = ', gausslegendre(f, 0,1,))
