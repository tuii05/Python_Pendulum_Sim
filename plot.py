import matplotlib.pyplot as plt
import numpy as np

class Plot:
    def __init__(self, c: object):
        self.phi = np.array([ci.phi for ci in c])
        self.phidot = np.array([ci.phidot for ci in c])
        self.t = np.array([ci.t for ci in c])
    def draw(self, T: float):
        phi = self.phi
        phidot = self.phidot
        t = self.t
        plt.figure("Szimuláció")
        #   phi(t)
        plt.subplot(2,1,1)
        plt.plot(t, phi)
        plt.ylabel("$\\phi$ (rad)")
        plt.grid(True)
        plt.xlim(0,T)
        plt.ylim(min(phi),max(phi))
        #   phidot(t)
        plt.subplot(2,1,2)
        plt.plot(t, phidot)
        plt.xlabel("t (s)")
        plt.ylabel("$\\omega$ (rad)")
        plt.xlim(0,T)
        plt.ylim(min(phidot),max(phidot))
        plt.grid(True)
        #   Cím
        plt.suptitle("Inga szimuláció")
        plt.show()
