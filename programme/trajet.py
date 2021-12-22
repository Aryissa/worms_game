import numpy as np
import math
import matplotlib.pyplot as plt


def euler(vx,vy,x,y,h):
    i=np.array([vx,vy,x,y])
    f1=np.array([i]) ##1=>t
    ifin=i+h*f1
    vx=ifin[0][0]
    vy=ifin[0][1]
    x=ifin[0][2]
    y=ifin[0][3]
    
    tabX=np.array([])
    tabY=np.array([])
    tabX=tabX+np.array([x])
    tabY=tabY+np.array([x])
    return tabX,tabY


def main():
    vx=1
    vy=1
    x=1
    y=2
    h=0.1
    cmpt=0
    while(cmpt<10):
     x,y=euler(vx,vy,x,y,h)
     cmpt+=1
    plt.plot(x, y, color='green', marker='o', linestyle='dashed', linewidth=2)
    plt.show()


main()