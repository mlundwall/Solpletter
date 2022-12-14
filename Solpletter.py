# -*- coding: utf-8 -*-
"""
Solpletter kildekode
Fourier-transformation

Created on Wed Oct 16 11:26:54 2019
@author: Mads Lundwall 2019
"""

from matplotlib import pyplot

from scipy.fftpack import fft

import numpy as np

from PletData import pletalle

print()
print("*-----------------------------------------------*")
print("*      Solpletter, dominerende periode          *")
print("*      Data fra 1700 til 2019                   *")
print("*      Beregnet med fourrier-transformation     *")
print("*-----------------------------------------------*")

pletallep=[row[1] for row in pletalle]
pletallea=[row[0] for row in pletalle]

#pletallep=[row[1] for row in plet128]
#pletallea=[row[0] for row in plet128]

pyplot.figure(figsize=(20,10))
pyplot.plot(pletallea,pletallep)
pyplot.title("Solpletter, antal 1700-2019")
pyplot.savefig(fname="Solpletter.antal.pdf",orientation="landscape",)
#pyplot.close() # I stedet for .show(), da vi kun vil gemme plottet, ikke vise det
pyplot.show()

fourier=fft(pletallep)[1:159] 
# Fra nr 1 til halvdelen (ialt er der = 319 i pletalle)
# Nr 0 fjenes, da den er en konstant (=summen af alle)

pyplot.figure(figsize=(20,10))
pyplot.plot(fourier.real)
pyplot.plot(fourier.imag)
pyplot.title("real-imag")
pyplot.savefig(fname="Solpletter.re-im.pdf",orientation="landscape",)
pyplot.close() # I stedet for .show(), da vi kun vil gemme plottet, ikke vise det
#pyplot.show()

res    = abs(fourier)

pyplot.figure(figsize=(20,10))
pyplot.title("Abs(Fourier) uden nul\"frekvens\"")
pyplot.plot(res)
pyplot.savefig(fname="Solpletter.ftt.pdf",orientation="landscape",)
pyplot.close() # I stedet for .show(), da vi kun vil gemme plottet, ikke vise det
#pyplot.show()

m      = max(res)          # Finder maksimum amplityde
l      = len(pletallep)    # Længden af dataset

f      = np.where(res==m)  # Finder frekvens for maksimum amplityde
p      = f[0][0] + 1       # f er frekvens med maks amplityde. Vi lægger en til, da der tælles fra 0
periode= l/p               # Periode (i år) er den fulde længde i år divideret med frekvensen der har maks amplityde

print()
print("Maximum periode={0:.2f} fundet i pos={1:d} af {2:d}".format(m,p,l))
print("Periode={0:.2f}".format(periode))
print()
print("Grafer Solpletter*.pdf ")
print("gemt i samme dir som kildefilen")