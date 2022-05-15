Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def cylinder(r, h):
from math import pi
def circle(r): return pi*r**2
s = 2*pi*r*h
if input('Full area? [y/n]: ') == 'y': \
s += 2*circle(r)
return s

r, h = 1, 1
print('s =', cylinder(r, h))