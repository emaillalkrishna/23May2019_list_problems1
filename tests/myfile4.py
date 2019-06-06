l1 = []
l2 = [1, 2, 3, 4, 5]
for var in l2:
    if var not in l1:
        l1.append(var)
        print(l1)
