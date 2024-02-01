"""
HW8
Savchenko Kirill
"""

import re
from colorama import init
init(autoreset=True)

# 1. HOME NUMBER

# TEST inf 1.HN 2.MN 3.EMAIL 4.FULL NAME
# inf = ['1234567890', '123456789', '12345678900', 'qwertyuiop', 'q123456789', '1qwertyuio', 'qwertyuio', '_123456789']
# inf = ['+123456789012', '+123456789qwe', '123456789012', '=123456789012', '_123456789012', '+qwertyuiopqw']
# inf = ['dd@dd.dd', 'dddd.dd', '23de@ww3ww', '12232323', 'srfhg@srf.hg.com', 'wrt@y.uio', 'wrt@yu@io.cc', '23.23@23']

inf = [input("Enter your home number: ")]

for valid in inf:
    if re.match(r'\d{10}$', valid):
        print('\033[32;1m'"Your home number is valid!")
    else:
        print('\033[31;1m'"Enter valid home number!")

# 2. MOBILE NUMBER

inf = [input("Enter your mobile number: ")]
for valid in inf:
    if re.match(r'\+?\d{12}$', valid):
        print("\033[32;1m""Your mobile number is valid!")
    else:
        print("\033[31;1m""Enter valid mobile number!")

# 3. EMAIL

inf = [input("Enter your email: ")]
for valid in inf:
    if re.match(r'\w{2,64}@\w{2,127}\.\w{2,127}', valid):
        print("\033[32;1m""Your email is valid!")
    else:
        print("\033[31;1m""Enter valid email!")
