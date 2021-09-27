import numpy as np
import matplotlib.pyplot as plot
import math
from scipy.optimize import fsolve

intervals=[]

def gx(x):
    return math.e**(-x**2)*np.sin(x**2)*(x+2)



def drawWholeGraph():
    x = np.linspace(-3.5, 3.5, 1000)
    y = gx(x)
    print()
    print('Fsolve rastos saknys:')
    print(fsolve(gx, np.linspace(-3, 3, 100)))
    plot.plot(x, y)
    #acc_interval = plot.plot([-3, 3], [0, 0], marker='^', color='orange', label='Duotas intervalas')
    #plot.legend(handles=acc_interval)
    plot.grid()
    plot.axhline(color='green')
    plot.axvline(color='green')
    plot.show()

def intervalSearch():
    colors = ['orange', 'red', 'yellow', 'purple', 'cyan']
    left = -3
    right = 3
    step = 0.03
    x = left
    y = gx(x)
    lastSign = np.sign(y)
    iter = left
    while iter < right:
        x = iter
        y = gx(x)
        currentSign = np.sign(y)
        if lastSign != currentSign:
            interval = {'left' : iter-step, 'right': iter}
            intervals.append(interval)
            lastSign = currentSign
        iter+=step
    #rnr = 0
    #legendintervals = []
    #for interval in intervals:
    #    legend_interval = plot.plot([float(interval['left']), float(interval['right'])], [0, 0], marker='^', color=colors[rnr])
    #    legendintervals.append(legend_interval)
    #    rnr+=1
    #plot.legend(handles=[legendintervals[0], legendintervals[1], legendintervals[2], legendintervals[3]], labels=['saknis: 1', 'saknis: 2', 'saknis: 3', 'saknis: 4'])
            
def simpleIterationMethod():
    alpha = 0.01
    xn=-2.2
    eps=1e-9
    iterNr=0
    iterMax=1000
    while iterNr < iterMax:
        gn=gx(xn)/alpha + xn
        prec = np.abs(gx(gn))
        if prec <= eps:
            print('Saknis rasta: %.10f, iteraciju kiekis: %d, tikslumas: %.10f'%(gn, iterNr, prec))
            break
        iterNr+=1
        xn=gn

    
def scanMethod(interval):
    left=interval['left']
    right=interval['right']
    step = 0.01
    x = left
    y = gx(x)
    prec = 1e-9
    root=None
    lastSign = np.sign(y)
    iterNr = 0
    while iterNr < 500:
        iter=left
        while iter <= right:
            x = iter
            y = gx(x)
            iterNr+=1
            currentSign = np.sign(y)
            if lastSign != currentSign:
                if np.abs(y) <= prec:
                    root=x
                    print('Saknis rasta %f:, iteraciju kiekis: %d tikslumas: %.10f'%(root, iterNr, np.abs(y)))
                    break
                else:
                    right = iter
                    left = right - np.abs(step)
                    step=step/4
                    x = left
                    y = gx(x)
                    lastSign = np.sign(y)
                    break
            iter+=step
        if not root is None:
            break
        step=step/4

def secantsMethod(x0, x1):
    gx0 = gx(x0) # fx(x^i-1)
    gx1 = gx(x1) # fx(x^i)
    xn = x1 - gx1/((gx1-gx0)/(x1-x0))
    eps=1e-9
    iterNr = 0
    while iterNr < 100:
        gx0 = gx(x0) # x^i-1
        gx1 = gx(x1) # x^i 
        iterNr+=1
        if np.abs(gx1) <= eps or np.abs(gx0) <= eps:
            precision=None
            if np.abs(gx1) <=eps:
                precision = np.abs(gx1)
            else:
                precision = np.abs(gx0)
            print('Saknis rasta: %f, iteraciju kiekis: %d tikslumas: %.10f'%(xn, iterNr, precision))
            break
        xn = x1 - gx1/((gx1-gx0)/(x1-x0))
       
        x0 = x1
        x1=xn

print('Iesko intervalu...')
intervalSearch()
print('Rasti intervalai:')
[print(interval) for interval in intervals]
print()
print('Ieskoma saknies intervale [%f;%f] skenuojant mazejanciu zyngsniu'%(intervals[0]['left'], intervals[0]['right']))
scanMethod(intervals[0])
print()
print('Ieskoma saknies intervale [%f;%f] skenuojant mazejanciu zyngsniu'%(intervals[1]['left'], intervals[1]['right']))
scanMethod(intervals[1])
print()
print('Ieskoma saknies intervale [%f;%f] skenuojant mazejanciu zyngsniu'%(intervals[2]['left'], intervals[2]['right']))
scanMethod(intervals[2])
print()
print('Ieskoma saknies intervale [%f;%f] skenuojant mazejanciu zyngsniu'%(intervals[3]['left'], intervals[3]['right']))
scanMethod(intervals[3])
print()
print('Ieskoma saknies intervale [%f;%f] skenuojant mazejanciu zyngsniu'%(intervals[4]['left'], intervals[4]['right']))
scanMethod(intervals[4])
print()
print('Paprastuju iteraciju metodas')
simpleIterationMethod()
print()
print('Kvazi-Niutono metodas')
secantsMethod(-1.9, -1)

drawWholeGraph()

