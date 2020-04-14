def Wlasny(data):
    for i in range(0, len(data), 2):
        yield data[i]


slowo = "Kwadrat"
slowo2 = "Owal"
nn = Wlasny(slowo)
print(nn.__next__())
print(slowo2)
print(nn.__next__())
print(slowo2)
print(nn.__next__())
print(slowo2)
print(nn.__next__())
