import random
import time


start_time = time.time()
l=range(100)
random.shuffle(l)

# l.index - this will actaully get the stuff in l

# l[a], l[b] = l[b], l[a]
# l.index[a]
# l.index[b]
# print l


for pos in xrange(len(l)-1):
    if l[pos] > l[pos +1]:
        l[pos], l[pos + 1] = l[pos + 1] , l[pos]
    for pos2 in xrange(len(l)-1):
        if l[pos2] > l[pos2 +1]:
            l[pos2], l[pos2 + 1] = l[pos2 + 1] , l[pos2]
print l

running_time = time.time()- start_time
print running_time
