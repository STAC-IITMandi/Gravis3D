from body import Body
from numpy.random import normal
from vpython import *

class Nbodies:
    """
    A class to implement all bodies.
    """
    def __init__(self, N = None):
        self.N = N or 10
        x,y,z = normal(0,1e11,N), normal(0,1e11,N), normal(0,1e11,N)
        vx,vy,vz = normal(0,1e7,N), normal(0,1e7,N), normal(0,1e7,N)
        r = abs(normal(1e9,1e8,N))
        self.bodies = []
        for i in range(N):
            newbody = Body(radius = r[i], pos = vector(x[i],y[i],z[i]), velocity = vector(vx[i],vy[i],vz[i]))
            #newbody = Body()
            self.bodies.append(newbody)
        
    def update(self):
        for i in range(self.N):
            for j in range(self.N):
                if i!=j:
                    self.bodies[i].attract(self.bodies[j])
                    #self.bodies[i].move()
            