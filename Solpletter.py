# -*- coding: utf-8 -*-
"""
Finder den dominerende periode i solpletaktiviteten i en bestemt periode
Benytter Fast-fourier transformation (fft)

@author: Mads Lundwall 2022
"""
from matplotlib import pyplot
from scipy.fftpack import fft
import numpy as np
from PletData import pletalle, plet128


class SolPletter:
    # Klasse, der laver beregningen
    # Lokale, offentlige egenskaber :
    m = 0   # Indeks med maksimal amplitude
    p = 0   # Frekvens med maksimal amplitude
    l = 0   # Længden af datasæt
    f = None
    f0 = complex(0, 0)  # Fasen - fourrier-transformationens 0-indeks


    def findperiode(self, kun128=True, visalleplot=False) -> float:
        # Argumenter
        # - kun120 - angiver om der kun skal hentes data fra 128 halvår - optimalt for fft
        # - visalleplot - angiver alle plot vises på skærmen, eller blot gemmes som PDF
        # Returnerer
        # - Fremherskende periode i år

        if kun128:
            startår = "1892"
            grafext = "_128"
        else:
            startår = "1700"
            grafext = "_alle"
        print()
        print("*-----------------------------------------------*")
        print("*      Solpletter, dominerende periode          *")
        print("*      Data fra " + startår + " til 2019                   *")
        print("*      Beregnet med fourier-transformation      *")
        print("*-----------------------------------------------*")

        if kun128:
            pletallep = [row[1] for row in plet128]  # Årstal
            pletallea = [row[0] for row in plet128]  # Antal pletter
        else:
            pletallep = [row[1] for row in pletalle]
            pletallea = [row[0] for row in pletalle]

        pyplot.figure(figsize=(20, 10))
        pyplot.plot(pletallea, pletallep)
        pyplot.title("Solpletter, antal " + startår + "-2019")
        pyplot.savefig(fname="Solpletter.antal" + grafext + ".pdf", orientation="landscape", )
        # Dette plot vises altid
        pyplot.show()

        # Selve FFT - transformationen :
        fou = fft(pletallep)
        fourier = fou[1:159]
        self.f0 = fou[0]
        # FFT: Nr 0 fjernes, da den er en konstant (=summen af alle)
        # Fra nr 1 til halvdelen (ialt er der = 319 ellers 128.
        # Sat til maks, da FFT kun tager til slut på dataset)

        pyplot.figure(figsize=(20, 10))
        pyplot.plot(fourier.real)
        pyplot.plot(fourier.imag)
        pyplot.title("real-imag")
        pyplot.savefig(fname="Solpletter.re-im" + grafext + ".pdf", orientation="landscape", )
        if not visalleplot:
            pyplot.close()  # I stedet for .show(), da vi kun vil gemme plottet, ikke vise det
        else:
            pyplot.show()

        # Vi tager absolut værdien = img^2+re^2 for at finde max amplitude
        # Se tildeling til selv.m længere nede
        res = abs(fourier)

        pyplot.figure(figsize=(20, 10))
        pyplot.title("Abs(Fourier) uden nul \"frekvens\"")
        pyplot.plot(res)
        pyplot.savefig(fname="Solpletter.ftt" + grafext + ".pdf", orientation="landscape", )
        if not visalleplot:
            pyplot.close()  # I stedet for .show(), da vi kun vil gemme plottet, ikke vise det
        else:
            pyplot.show()

        self.m = max(res)  # Finder maksimum amplitude
        self.l = len(pletallep)  # Længden af dataset

        self.f = np.where(res == self.m)  # Finder frekvens for maksimum amplitude
        self.p = self.f[0][0] + 1  # F er frekvens med maks amplitude. Vi lægger en til, da der tælles fra 0
        return self.l / self.p  # Periode (i år) er den fulde længde i år divideret med frekvensen der har maks amplitude


plet = SolPletter()

periode = plet.findperiode(True, False)
print()
print("128 målinger:")
print("Fase = {0:.2f}".format(plet.f0))
print("Maximum periode-amplitude = {0:.2f} fundet i pos = {1:d} af {2:d}".format(plet.m, plet.p, plet.l))
print("Periode omregnet til år   = {0:.2f}".format(periode))

periode = plet.findperiode(False, False)
print()
print("Alle målinger:")
print("Fase = {0:.2f}".format(plet.f0))
print("Maximum periode-amplitude = {0:.2f} fundet i pos = {1:d} af {2:d}".format(plet.m, plet.p, plet.l))
print("Periode omregnet til år   = {0:.2f}".format(periode))

print()
print("Grafer Solpletter*.pdf ")
print("gemt i samme dir som kildefilen")

input("Tryk for at afslutte ...")
