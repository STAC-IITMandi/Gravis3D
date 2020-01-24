from body import Body
from numpy.random import normal
from vpython import vector

class Nbodies:
    """
    A class to implement all bodies.
    """
    def __init__(self, N = None):
        self.N = N or 10
        x,y,z = normal(0,1e12,N), normal(0,1e12,N), normal(0,1e12,N)
        vx,vy,vz = normal(0,2*1e4,N), normal(0,2*1e4,N), normal(0,2*1e4,N)
        r = abs(normal(1e8,1e7,N))
        self.bodies = []
        for i in range(N):
            newbody = Body(radius = r[i], pos = vector(x[i],y[i],z[i]), velocity = vector(vx[i],vy[i],vz[i]))
            self.bodies.append(newbody)
            