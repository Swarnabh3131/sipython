# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 14:44:48 2019

@author:Swarnabh Srivastava
"""

set1 = {1,2, 'SIP', 'Dhiraj', True}
set1

set1[0]
set1

for i in set1 : print(i, end= ' ')

'Dhiraj' in set1
'Kounal' in set1

set1.add('Pooja')
set1

set1.add('Pooja')
set1

set1.update(['ABC', 'DEF'])
set1

set1.update('XYZ')
set1

len(set1)

set1.remove('Pooja')
set1


teamA = {'India', 'Australia', 'Pakistan', 'England'}
teamB = {'Bangladesh', 'New Zealand', 'West Indies', 'India'}
teamA
teamB

teamA.update(['Sri Lanka'])
teamA

teamA.union(teamB)

teamA.difference(teamB)