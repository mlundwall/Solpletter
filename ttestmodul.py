# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 12:56:36 2019

@author: Mads Lundwall
Test af t-test funktione
"""

from scipy import stats as stats
import statsmodels.stats as w
from statistics import mean, stdev

def ttest(a,b,ensvar=True):
    anta=len(a)
    ma=mean(a)
    sda=stdev(a)
    antb=len(b)
    mb=mean(b)
    sdb=stdev(b)
    print("Antal, stdev og mean af a {0:.4f}, {1:.4f}, {2:.4f}".format(anta,ma,sda))
    print("Antal, stdev og mean af b {0:.4f}, {1:.4f}, {2:.4f}".format(antb,mb,sdb))
    
    if ensvar :
        print("Under antagelse af ens varians:")
    else :
        print("UDEN antagelse om ens varians:")

    p=stats.ttest_ind(a,b,equal_var=ensvar)

    print("Tosidig t-test - ingen forskel = {0:.4f} p-værdi = {1:.4f}".format(p[0],p[1]))    
    if p[1]<0.05:
        print("Nulhypotese (ens middelværdi) forkastet da {0:.2f} < 0.05".format(p[1]))
    else :
        print("Nulhypotese (ens middelværdi) GODKENDT da  {0:.3f} >=0.05".format(p[1]))

    print()

def ztest(a,middelpop):
    anta=len(a)
    ma=mean(a)
    sda=stdev(a)
    print("Antal, stdev og mean af a {0:.4f}, {1:.4f}, {2:.4f}".format(anta,ma,sda))
    
    print("Under antagelse af ens varians:")

    p=w.weightstats.ztest(a,None,middelpop)
    print(p)
    print("Tosidig Z-test - ingen forskel = {0:.4f} p-værdi = {1:.4f}".format(p[0],p[1]))    
    if p[1]<0.05:
        print("Nulhypotese (ens middelværdi) forkastet da {0:.2f} < 0.05".format(p[1]))
    else :
        print("Nulhypotese (ens middelværdi) GODKENDT da  {0:.3f} >=0.05".format(p[1]))

    print()

 