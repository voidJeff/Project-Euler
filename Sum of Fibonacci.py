i = 0
n_l = [1, 2]
while n_l[len(n_l)-1] + n_l[len(n_l)-2] <= 4000000:
    n_l.append(n_l[len(n_l)-1] + n_l[len(n_l)-2])
while n_l[i]%2 != 0 and i < 4000000:
    n_l.remove(n_l[i])
    i += 1
print(sum(n_l))
