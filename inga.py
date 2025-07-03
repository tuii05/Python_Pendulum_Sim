from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt
import math


#Struktúra-féleség
@dataclass
class xypt:
    x: float
    y: float
    phi: float
    phidot: float
    t: float
    

class Inga:
    #Konstruktor
    def __init__(self, phi0: float, L: float, m: float, k: float):
        self.phi0 = phi0
        self.L = L
        self.m = m
        self.k = k
    #Print függvény
    def print(self):
        print("Phi0 = ", self.phi0)
        print("L = ", self.L)
        print("m = ", self.m)
        print("k = ", self.k)
    #A mozgásegyenlet változóinak adott időbeli értékét adja vissza.
    def iteracio(self, c0: xypt, dt: float):
        #print(c0.x)
        #c0.x = 4
        #return c0
        phi0 = c0.phi
        phidot0 = c0.phidot
        theta = self.m*pow(self.L,2)
        phidot = (1-self.k*pow(self.L,2)/theta*dt)*phidot0-self.m*9.81*self.L/theta*math.sin(phi0)*dt
        phi = phidot0*dt + phi0
        return xypt(self.L*math.sin(phi), self.L*math.cos(phi), phi, phidot, c0.t + dt)
    #A diffferenciálegyenlet megoldását adja meg, amely a koordináták időfüggését adja vissza.
    def ujcoords(self, T: float):
        dt = 0.01
        theta = self.m*pow(self.L,2)
        c0 = xypt(self.L*math.sin(self.phi0), self.L*math.cos(self.phi0), self.phi0, 0, 0)
        c = [c0]
        c0 = self.iteracio(c0, dt)
        while(c0.t < T):
            c.append(c0)
            c0 = self.iteracio(c0, dt)
        return np.array(c, dtype=object)


