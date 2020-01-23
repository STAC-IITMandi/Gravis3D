from vpython import color,vector, mag2, mag
from numpy import pi
from main import G

class Body:
    '''
    A class representing all the bodies
    in the simulation.
    '''
    def __init__(self, radius = None, position = None, velocity = None, colour = None,density = None):
        self.radius = radius or 6.9634*1e9
        self.density = density or 1408  #avg sun density
        self.mass = (4/3)*pi*(self.radius**3)*self.density
        self.position = position or vector(0,0,0)
        self.velocity = velocity or vector(0,0,0)
        self.colour = colour or color.orange

    def move(self):
        self.position += self.velocity

    def attract(self, attractor):
        force = G*(self.mass*attractor.mass)/(mag2(attractor.position - self.position))*(attractor.position - self.position)
        self.velocity += force
        attractor.velocity -= force

    def is_collision(self, other):
        if mag(self.position-other.position) <= mag(self.radius) + mag(other.radius) :
            return True
        else:
            return False

    def merged(self, other):
        mass = self.mass + other.mass
        radius = (0.75*(1/pi)*(1/1408)*mass)*(1/3)
        velocity = (self.mass*self.velocity + other.mass*other.velocity)/(mass)
        return mass, radius, velocity
        