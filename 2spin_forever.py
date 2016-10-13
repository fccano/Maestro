#!/usr/bin/python

import time
import maestro as m
s= m.Controller()

IZQ=4
DER=5

while (1):
	s.setTarget(IZQ,-1)
        s.setTarget(DER,1)
        time.sleep(2)

        s.setTarget(IZQ,0)
        s.setTarget(DER,0)
        time.sleep(0.35)

        s.setTarget(IZQ,1)
        s.setTarget(DER,-1)
        time.sleep(2)

        s.setTarget(IZQ,0)
        s.setTarget(DER,0)
        time.sleep(0.35)
