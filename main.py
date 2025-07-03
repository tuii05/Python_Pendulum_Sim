#Megjegyzés: struct-like dataclass
#from dataclasses import dataclass

#@dataclass
#class Point:
#    x: float
#    y: float
#    z: float

#p = Point(1.5,2.5,3.5)
#print(p)

#Plot készítés
#xpoints = np.array([0,6])
#ypoints = np.array([0,250])
#plt.plot(xpoints, ypoints)
#plt.title("Teszt")
#plt.xlabel("x")
#plt.ylabel("y")
#plt.show()

import matplotlib.pyplot as plt
import numpy as np
import inga
import plot

#Beolvasás
nums = []
file = open("datas.txt")
string = file.read();
string = string.replace(',',' ').split()
for i in string:
    try:
        nums.append(float(i))
    except ValueError:
        pass

#Inicializálás
inga1 = inga.Inga(nums[0]*3.14/180,nums[1],nums[2],nums[3])

#Mozgásegyenletből koordináták kinyerése
c = inga1.ujcoords(nums[4])

#Phi(t), phidot(t) ábra elkészítése
abra = plot.Plot(c)
abra.draw(nums[4])


