#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Sora Hirano <s23c1115wh@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause

import sys
import math

def combination(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

for line in sys.stdin:
    user_input = line.strip()
    n, r = map(int, user_input.split())
    result = combination(n, r)
    print(f"{n}C{r} = {result}") 
