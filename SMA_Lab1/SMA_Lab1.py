import numpy as np
import matplotlib.pyplot as plot

# f(x)=−0.67𝑥^4+2.51𝑥^3+2.27𝑥^2−4.02𝑥−2.48, g(x) = 𝑒^(−𝑥^2)sin(𝑥^2)(𝑥+2) −3≤𝑥≤3
# Grubus ivertis: R = 7
# Tikslesnis ivertis: Rneig = 2.418, Rteig = 4.763

intervals=[]

def fx(x):
    return 0.67*x**4 - 2.5*x**3 - 2.27*x**2 + 4.02*x + 2.48

def drawWholeGraph():
    x = np.linspace(-3, 5, 100)
    y = fx(x)

    plot.plot(x, y)
    #acc_interval = plot.plot([-2.418, 4.763], [0, 0], marker='^', color='blue', label='Tikslesnis ivertis')
    #plot.legend(handles=acc_interval)
    plot.grid()
    plot.axhline(color='green')
    plot.axvline(color='green')
    plot.show()

def intervalSearch():
    colors = ['orange', 'red', 'yellow', 'purple']
    left = -2.418
    right = 4.763
    step = 0.1
    x = left
    y = fx(x)
    lastSign = np.sign(y)
    iter = left
    while iter < right:
        x = iter
        y = fx(x)
        currentSign = np.sign(y)
        if lastSign != currentSign:
            interval = {'left' : iter-step, 'right': iter}
            intervals.append(interval)
            lastSign = currentSign
        iter+=step
    #Rnr = 0
    #legendIntervals = []
    #for interval in intervals:
    #    legend_interval = plot.plot([float(interval['left']), float(interval['right'])], [0, 0], marker='^', color=colors[Rnr])
    #    legendIntervals.append(legend_interval)
    #    Rnr+=1
    #plot.legend(handles=[legendIntervals[0], legendIntervals[1], legendIntervals[2], legendIntervals[3]], labels=['Saknis: 1', 'Saknis: 2', 'Saknis: 3', 'Saknis: 4'])
            
def simpleIterationMethod():
    alpha = -30
    xn=4
    eps=1e-9
    iterNr=0
    iterMax=1000
    while iterNr < iterMax:
        fn=fx(xn)/alpha + xn
        prec = np.abs(fx(fn))
        if prec <= eps:
            print('Saknis rasta: %.10f, iteraciju kiekis: %d, tikslumas: %.10f'%(fn, iterNr, prec))
            break
        iterNr+=1
        xn=fn

    
def scanMethod(interval):
    left=interval['left']
    right=interval['right']
    step = 0.5
    prec = 1e-9
    x = left
    y = fx(x)
    root=None
    lastSign = np.sign(y)
    iterNr = 0
    while iterNr < 500:
        iter=left
        while iter <= right:
            x = iter
            y = fx(x)
            iterNr+=1
            currentSign = np.sign(y)
            if lastSign != currentSign:
                if np.abs(y) <= prec:
                    root=x
                    print('Saknis rasta %f:, iteraciju kiekis: %d, tikslumas: %.10f'%(root, iterNr, np.abs(y)))
                    break
                else:
                    right = iter
                    left = right - np.abs(step)
                    step=step/4
                    x = left
                    y = fx(x)
                    lastSign = np.sign(y)
                    break
            iter+=step
        if not root is None:
            break
        step=step/4

def secantsMethod(x0, x1):
    fx0 = fx(x0) # fx(x^i-1)
    fx1 = fx(x1) # fx(x^i)
    xn = x1 - fx1/((fx1-fx0)/(x1-x0))
    eps = 1e-9
    iterNr = 0
    while iterNr < 100:
        fx0 = fx(x0) # x^i-1
        fx1 = fx(x1) # x^i
        if np.abs(fx1) <= eps or np.abs(fx0) <= eps:
            precision=None
            if np.abs(fx1) <= eps:
                precision=np.abs(fx1)
            else:
                precision=np.abs(fx0)
            print('Saknis rasta: %f, iteraciju kiekis: %d, tikslumas: %.10f'%(xn, iterNr, precision))
            break
        xn = x1 - fx1/((fx1-fx0)/(x1-x0))
        iterNr+=1
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
print('Paprastuju iteraciju metodas')
simpleIterationMethod()
print()
print('Kvazi-Niutono metodas')
secantsMethod(2, 4)
drawWholeGraph()
