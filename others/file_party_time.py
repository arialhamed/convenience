import os
from random import random, randint
# run at own risk lmao
# e.g.: 2023-04-23 17:33:55.902208172 +0800
while True:
	for i in os.listdir():
		Y = str(1900 + randint(0,120))
		M = str(randint(1,12)).zfill(2)
		d = str(randint(1,28)).zfill(2)
		h = str(randint(0,23)).zfill(2)
		m = str(randint(0,59)).zfill(2)
		s = str(randint(0,59)).zfill(2)
		p = str(randint(0,999999999)).zfill(9)
		os.system(f"touch -d \"{Y}-{M}-{d} {h}:{m}:{s}.{p} +0800\" \"{i}\"")