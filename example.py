import math
from monte import Monte

a = range(-1000, 1000)
a = map(lambda x: x/1000.0, a)
# [-1.0, -0.999, -0.998, -0.997, -0.996 ...
# 0.995, 0.996, 0.997, 0.998, 0.999]
trials = 100

a = Monte(math.sin, a, trials)
results = a.test()
print(sum(results)/trials)
print(a)
