i = 0
n_l = [1, 2]
while n_l[len(n_l)-1] + n_l[len(n_l)-2] <= 4000000:
    n_l.append(n_l[len(n_l)-1] + n_l[len(n_l)-2])
while n_l.count(i*2) == 1 and i < 2000000:
    n_l.remove(i*2)
    i += 1
print(n_l)
