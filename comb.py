#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Sora Hirano
# SPDX-License-Identifier: BSD-3-Clause

import sys
import math

def combinations(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

for line in sys.stdin:
    user_input = line.strip()
    if not user_input:
        print("無効な入力: ")
        sys.exit(1)
    try:
        n, r = map(int, user_input.split())
        result = combinations(n, r)
        print(f"{n}C{r} = {result}")
    except ValueError:
        print(f"無効な入力: {user_input}")
        sys.exit(1)  


