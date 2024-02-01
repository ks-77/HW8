"""
HW8
Savchenko Kirill
"""

import re
from colorama import init
init(autoreset=True)

# 1. HOME NUMBER

# TEST inf
# inf = ['1234567890', '123456789', '12345678900', 'qwertyuiop', 'q123456789', '1qwertyuio', 'qwertyuio', '_123456789']

inf = [input("Enter your home number: ")]

for valid in inf:
    if re.match(r'\d{10}$', valid):
        print('\033[32;1m'"Your home number is valid!")
    else:
        print('\033[31;1m'"Enter valid home number!")
