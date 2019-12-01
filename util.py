import math
from functools import reduce

def lcm(a):
	lcm = a[0]
	for i in a[1:]:
		lcm = lcm * i // math.gcd(lcm, i)
	return lcm