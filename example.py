from monte import Monte

def f(): pass
a = range(10)
trials = 10

a = Monte(f, a, trials)
print(a)