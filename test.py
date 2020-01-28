#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 10:48:19 2020

@author: shunkeai
"""

from vpython import *
scene3 = canvas(title='Ring and Ball',
     width=800, height=600,
     center=vector(0,0,0), forward=vector(0,-1,0), background=color.black)

Bob1=sphere(pos = vector(-3,0,0), radius=0.5, color=color.white)
Bob2=sphere(pos = vector(1,0,0), radius=0.5, color=color.white)
#initial position of two "Black hold"

r1=Bob1.pos
r2=Bob2.pos
theta=0.1    #initial phase angle
orbitr0=3.0  #initial orbiting radius
orbitr=orbitr0
centerx=r1.x-orbitr*cos(3.14-theta) # find center of mass
centerz=r1.z+orbitr*sin(3.14-theta) 

while orbitr > 0:
    rate(10)
    Bob1.pos=r1
    Bob2.pos=r2
    r1.x= centerx+orbitr*cos(theta)
    r1.z= centerz+orbitr*sin(theta)
    r2.x= centerx+orbitr*cos(theta-3.14)
    r2.z= centerz+orbitr*sin(theta-3.14)
    #update position of the binary "Blackhole"
    orbitr=orbitr-0.01     #update orbiting radius
    theta=theta+0.05*(orbitr0/orbitr)**(3/2) #update phase angle
    