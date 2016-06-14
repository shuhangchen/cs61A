class Such:
    def __init__(self, iteration):
        self.iteration = iteration
    def __next__(self):
        if self.iteration == 0:
            raise StopIteration
        self.iteration //= 2
        return self.iteration
    def __iter__(self):
        while self.iteration < 30:
            yield self.iteration
            self.iteration += 10
s = Such(16)
next(s)
next(s)
slst = []
for j in s:
    slst.append(j)


next(s)
for j in s:
    slst.append(j)
print(slst)
