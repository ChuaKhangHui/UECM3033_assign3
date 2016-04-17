import numpy as np
import sympy as sy

# DO NOT CHANGE THE NAME OF gausslegendre() function
def gausslegendre(f, a, b, n=20):
    
    # get Gauss points and weight for [-1,1]
    [node,weight] = np.polynomial.legendre.leggauss(n)

    # transform node from [-1,1] to [a,b]
    node_new = 0.5 * (b-a) * node + 0.5 * (a+b )
    y = f(node_new)
    
    ans = (0.5*(b-a)*np.dot(weight, y ))
    
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
