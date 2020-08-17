"""
bezier.py
by Ted Morin

a simple program to play with bezier curves
"""
import numpy as np
import sympy as sy
from scipy.special import comb as choose

def bezier1d(points):
#    d = len(points[0])
    N = len(points) - 1
    bez_x = lambda t: sum([
            choose(N,k)*np.power(t,k)*np.power(1-t,N-k)*points[k][0]
                                for k in range(N+1) ]) 
    bez_y = lambda t: sum([
            choose(N,k)*np.power(t,k)*np.power(1-t,N-k)*points[k][1]
                                for k in range(N+1) ]) 
    return bez_x, bez_y

if __name__ == "__main__":
    # prepare to plot some data
    import matplotlib.pyplot as plt
    plt.plot([0,1,1,0,0], [0,0,1,1,0], 'k-')
    n = 5
    plt.title("Click on {} points!".format(n))
    points = np.array(plt.ginput(n))

    x = points[:,0]
    y = points[:,1]
    #x = np.array([point[0] for point in points])
    #y = np.array([point[1] for point in points])
    bez_x, bez_y = bezier1d(points)

    # make the bezier curve data
    fit_points_per_input_point = 10
    t = np.linspace(0,1, len(x)*fit_points_per_input_point)
    x_bez = bez_x(t)
    y_bez = bez_y(t)

    plt.close()
    plt.plot([0,1,1,0,0], [0,0,1,1,0], 'k-')
    plt.plot(x_bez, y_bez, 'b--')
    plt.plot(x,y, 'r+')
    plt.title("Bezier!")
    plt.show()
