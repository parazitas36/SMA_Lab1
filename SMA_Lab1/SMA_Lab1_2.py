import numpy as np
import matplotlib.pyplot as plot
import math
from scipy.optimize import fsolve

def v(c):
    eps=1e-10
    if c == 0: # Protection from division by zero
        c+=eps
    g = 9.8
    m = 60
    v1 = 25
    t = 3
    return m*g/c*(1- math.e**(-t*c/m)) - v1

def plotv(c):
    g = 9.8
    m = 60
    v1 = 25
    t = 3
    return m*g/c*(1- math.e**(-t*c/m)) - v1

def chordsMethod(cn, c1):
    iterNr = 0
    eps=1e-9
    while iterNr < 100:
        vn=v(cn)
        v1=v(c1)
        k=np.abs(vn/v1)
        cmid=(cn+k*c1)/(1+k)
        if np.sign(v(cmid)) == np.sign(vn):
            cn = cmid
        else:
            c1 = cmid
        if cn - c1 <= eps:
            print('Pasipriesinimo koeficientas: %.10f, uztruko iteraciju: %d, tikslumas: %.10f'%(cmid, iterNr, np.abs(v(cmid))))
            plot.plot(cmid, np.abs(v(cmid)), marker='^', color='red')
            break
        iterNr+=1     

def drawWholeGraph():
    c = np.linspace(-70, 15, 100)
    y = plotv(c)
    print('Rasta saknis su fsolve: %.10f'%fsolve(plotv, c)[0])
    plot.plot(c, y)
    plot.grid()
    plot.axhline(color='green')
    plot.axvline(color='green')
    plot.show()

chordsMethod(20, -1)
drawWholeGraph()