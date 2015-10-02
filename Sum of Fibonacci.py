i = 0
n_l = [1, 2]
while n_l[len(n_l)-1] + n_l[len(n_l)-2] <= 4000000:
    n_l.append(n_l[len(n_l)-1] + n_l[len(n_l)-2])
for x in n_l:  
    if x%2 != 0:
        n_l.remove(x)
print(sum(n_l))
