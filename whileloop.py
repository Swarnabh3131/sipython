# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 23:46:34 2019

@author:Swarnabh Srivastava
"""

i = 1
while (i < 10):
    print(i, end =' ')
    i += 1 #printing values till 10
    
i = 1
while (i < 10):
    print(i, end = '\t')
    if i == 4 : #ending here
        print('Exiting Loop at this point')
        break
    i += 1
    
i = 1
while (i < 10):
    print(i, end = '\t')
    i += 1
    if i == 5 : #continue with loop
       continue