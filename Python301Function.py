###### Hello function
# name=raw_input("what is your name? ")
#
# def hello(name):
#     return "Hello " + name
#
# hello(name)

##### y = x+1 function
# import matplotlib.pyplot as plot
#
# def f(x):
#     return x + 1
# xs = range(-3, 4)
# ys = []
# for x in xs:
#     ys.append(f(x))
#
# plot.plot(xs,ys)
# plot.show()

#####Square of x
# import matplotlib.pyplot as plot
# def f(x):
#     return x ** 2
# xs = range(-100, 100)
# ys = []
# for x in xs:
#     ys.append(f(x))
#
# plot.plot(xs,ys)
# plot.show()



# ######## ODD OR EVEN
# import matplotlib.pyplot as plot
# def f(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return -1
# xs = range(-5, 5)
# ys = []
# for x in xs:
#     ys.append(f(x))
#
# plot.bar(xs, ys)
# plot.show()


# ######## SIN
# import matplotlib.pyplot as plot
# import math
#
# def f(x):
#     return math.sin(x)
#
# xs = range(-5, 5)
# ys = []
# for x in xs:
#     ys.append(f(x))
#
# plot.plot(xs, ys)
# plot.show()

# ######## SIN part 2 (cleaning it up)
import matplotlib.pyplot as plot
import math
from numpy import arange

def f(x):
    return math.sin(x)

xs = arange(-5, 6, 0.1)
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()
