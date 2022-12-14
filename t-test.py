# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 12:31:25 2019

@author: MLUC
"""

from ttestmodul import ztest, ttest

høj     = [1.4,1.2,1.4,1.1,1.1,1.2,1.4,1.3,1.2,1.1,1.2,1.5,1.2]
megethøj= [1.5,1.2,1.4,1.4,1.1,1.6,1.4,1.3,1.2,1.7]

lav     = [1.1,1.3,1.4,1.2,1.1,1.1,1.1,1.2,0.9]
megetlav= [1.2,1.1,1.0,1.1,1.2,1.2,1.1,1.3,1.1,1.1,1.1,0.8,1.0,0.9]

alderA  = [45,38,52,48,25,39,51,46,55,46]	
alder_A = [44,38,52,48,25,39,51,46,55,46]	
alderB  = [34,22,15,27,37,41,24,19,26,36]

born    = [5.5, 5.9, 6, 6, 6.1, 6.5, 6.5, 6.8, 7, 7.2, 7.4, 7.5, 7.5, 7.6, 7.7, 7.7, 7.8, 7.9, 8, 8, 8.2, 8.3, 8.5, 8.9, 9, 9.1, 9.4, 10, 11, 12]

#ttest(megethøj,megetlav)
#ttest2(høj,megetlav)
#ttest2(megethøj,lav)
#ttest(høj,lav)
#ttest2(megethøj,høj)
#ttest2(megetlav,lav)
#ttest2(alderA,alderB)
#ttest(alderA,alder_A,True)
#ttest(alderA,alder_A,False)

ztest(born,7.5)
