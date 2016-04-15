import numpy as np
from scipy.integrate import odeint

def pend(yy, t, b, c):
    [y0, y1] = yy
    yyp = [a * (y0 - y0 * y1), b * (-y1 + y0 * y1)]
    return yyp

if __name__ == "__main__":
    a = 1
    b = 0.2
    y0 = 0.1
    y1 = 1.0
    
    y0p = a * (y0 - y0 * y1)
    y1p = b * (-y1 + y0 * y1)
    
    
    yy0 = [0.1,1.0] #[y0,y1]
    
    t= np.linspace(0,5, 5+1)
    
    sol = odeint(pend,yy0,t, args=(a,b))
    
    import matplotlib.pyplot as plt
    plt.plot(t, sol[:, 0], 'b', label='theta(t)')
    plt.plot(t, sol[:, 1], 'g', label='omega(t)')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()