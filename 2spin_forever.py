#!/usr/bin/python

import time
import maestro as m
s= m.Controller()
izq = 4
der = 5

while 1:
	s.setTarget(izq,1)
	s.setTarget(der,-1)

	time.sleep(3)

	s.setTarget(izq,0)
	s.setTarget(der,0)
	
	time.sleep(1)


	s.setTarget(izq,-1)
	s.setTarget(der,1)
