import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
   
def pend(y, t, b, c):
    [y0, y1] = y
    yp = [b * (y0 - y0 * y1), c * (-y1 + y0 * y1)]
    return yp

if __name__ == "__main__":
    a = 1
    b = 0.2
    y0_0 = 0.1
    y1_0 = 1.0
        
    y_0 = [y0_0,y1_0]
    
    t= np.linspace(0,5, 100)
    
    sol = odeint(pend,y_0,t,args=(a,b))
    
    plt.plot(t, sol[:, 0], 'b', label='y0(t)')
    plt.plot(t, sol[:, 1], 'g', label='y1(t)')
    plt.legend(loc='best')
    plt.xlabel('t (years)')
    plt.grid()
    plt.show()
    
    
    plt.plot(sol[:,1], sol[:,0])
    plt.ylabel('y0')
    plt.xlabel('y1')
    plt.grid()
    plt.show()