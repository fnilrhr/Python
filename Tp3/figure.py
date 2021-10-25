import numpy as np
from math import pi, sqrt
import matplotlib.pyplot as plt

    
def figure(n):
    fig, ax = plt.subplots(1)
    
    theta = np.linspace(0, 2*np.pi, 100)

    radius = n

    a = radius*np.cos(theta) 
    b = radius*np.sin(theta) 
    
    plt.plot(a, b)
    ax.set_aspect(1)
    ax.grid(linestyle='--')

    plt.title('Mon cercle', fontsize=15)
    
    x = np.array([-n, -n, n, n, -n])
    y = np.array([-n, n, n, -n, -n])
    ax.plot(x, y)
    
    c = np.array([(-(sqrt(2)/2))*n, -(sqrt(2)/2)*n, (sqrt(2)/2)*n, (sqrt(2)/2)*n, -(sqrt(2)/2)*n,(-sqrt(2)/2)*n,(sqrt(2)/2)*n])
    d = np.array([(-(sqrt(2)/2))*n, (sqrt(2)/2)*n, (sqrt(2)/2)*n, -(sqrt(2)/2)*n, -(sqrt(2)/2)*n,(sqrt(2)/2)*n,-(sqrt(2)/2)*n])
    ax.plot(c, d)    

    
    plt.show()
    

figure(float(2))
