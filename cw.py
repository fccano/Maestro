#!/usr/bin/python

import time
import maestro as m
s= m.Controller()
izq = 4
der = 5
s.setTarget(izq,1)
s.setTarget(der,-1)

time.sleep(5)

s.setTarget(izq,0)
s.setTarget(der,0)
