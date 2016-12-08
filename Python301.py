# import matplotlib.pyplot as plot
#
# def f(x):
#     return 2 * x + 1
#
# def g(x):
#     return x + 1
#
# xs = range(-3, 5)
# fys = []
# for x in xs:
#     fys.append(f(x))
#
# gys = []
# for x in xs:
#     gys.append(g(x))
#
# plot.plot(xs, fys, xs, gys)
# plot.show()

name = 'Raj'
age = 5
def sentence ():
    return '%s is %d years old.' % (name, age)

print sentence()
