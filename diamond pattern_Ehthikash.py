# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 13:59:34 2021

@author: ehthi
"""

countout=0

while countout<5:
    countin1=4
    while countin1>countout:
        print(' ',end='')
        countin1=countin1-1
    countin2=0
    while countin2<=countout:
        print('# ',end='')
        countin2=countin2+1
    print('')
    countout=countout+1
    

count1=0
while count1<4:
    count2=0
    while count2<=count1:
        print(' ',end='')
        count2=count2+1
    count3=4
    while count3>count1:
        print('# ',end='')
        count3=count3-1
    print('')
    count1=count1+1
    
