import os

def memtake(N):
    L = []
    for i in range(N):
        l = [float(f) for f in range(10000)]
        L.append(l)
        del l
    return len(L)

print(memtake(10))
print("Luck!")