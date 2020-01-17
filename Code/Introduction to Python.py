## Introduction to Python ##

# General introduction #
2 + 2               # In [1]
a = 2 + 2           # In [2]
a                   # In [3]
b = 2 * 3           # In [4]
b - 1
b**2
import math         # In [5]
math.sqrt(2)

# Numbers and strings #
type(a)             # In [6]
b = math.sqrt(2)    # In [7]
type(b)
type(2)             # In [8]
type(2.0)           # In [9]
float(2)            # In [10]
int(2.3)            # In [11]
d = 5 < a           # In [12]
d
type(d)             # In [13]
a == 4              # In [14]
math.sqrt(d)        # In [15]
1 - d               # In [16]
c = 'Messi'         # In [17]
type(c)

# Lists #
x = ['Messi', 'Cristiano', 'Neymar', 'Coutinho']    # In [18]
len(x)                                              # In [19]

y = x + [2, 3]                                      # In [20]
y
len(y)                                              # In [21]
y[0:2]                                              # In [22]
y[3:]                                               # In [23]
y[:3]                                               # In [24]
set(y)                                              # In [25]
list(set([1, 0, 1, 0, 7]))                          # In [26]

# For loops #
squares = [0]                               # In [27]
for i in range(1, 4):
    squares = squares + [i**2]
squares
squares = [i**2 for i in range(0,4)]        # In [28]
squares
[len(name) for name in x]                   # In [29]
fib = [1, 1]                                # In [30]
for i in range(2, 10):
    fib = fib + [fib[i-1] + fib[i-2]]
fib                                         # In [31]

# Functions #
def f(x):                                   # In [32]
    y = 1/(1 - x**2)
    return(y)
f(2)                                        # In [33]
f(1)                                        # In [34]
f('Mary')                                   # In [35]
def g(x, y): return x*y/(x**2 + y**2)       # In [36]
g(1, 1)
f = lambda x: 1/(1 - x**2)                  # In [37]
