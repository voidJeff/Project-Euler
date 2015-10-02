n_l = [1, 2]
while n_l[len(n_l)-1] + n_l[len(n_l)-2] <= 4000000:
    n_l.append(n_l[len(n_l)-1] + n_l[len(n_l)-2])
print(n_l)
