

import numpy as np
import matplotlib.pyplot as plt
ln = np.log


def fonction1(x):
    return 1-ln(x)

def fonction2(x):
    return x**2-2

def fonction3(x):
    return np.cos(x)

def derive1(x):
    return -1/x

def derive2(x):
    return 2*x

def derive3(x):
    return -np.sin(x)

def tacc(x, h):
    return (fonction2(x + h) - fonction2(x))/h

/opt/anaconda2/lib/python2.7/site-packages/matplotlib/font_manager.py:278: UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.
  'Matplotlib is building the font cache using fc-list. '

tacc(1, 1) ici dérivé de cos en utilisant tacc fonctionne bien derive2(1) par contre la fonction tacc ne fonctionne pas sur la deuxième fonction

def erreur(N, h):
    tab = np.arange(0, N, 1)
    tab2 = derive2(tab)

    tab3 = tacc(tab, h)

    tab4 = tab2 - tab3

    tab4 = np.abs(tab4)

    
    a = (np.sum(tab4))/N
    return a

def erreurh(N):
    h = [10**(-1),10**(-2),10**(-3),10**(-4),10**(-5)]
    tab[len(h)]
    
    for i in range(0, len(h)):
        tab[i] = erreur(N, h[i])
        print(erreur(N, h[i]))
        
    return tab

plt.plot(erreurh(8))

0.09999999999998577
0.009999999999882991
0.0010000000021999078
9.999999362531042e-05
9.9997913339811e-06

[<matplotlib.lines.Line2D at 0x7f5e19a51250>]

