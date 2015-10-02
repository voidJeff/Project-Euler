num = list(range(1, 1001))
n_num = []
i = 1
while i*3 <= 1000:
    if num.count(3*i) == 1:
        n_num.append(3*i)
    i += 1
i = 1
while i*5 <= 1000:    
    if num.count(5*i) == 1:
        n_num.append(5*i)
    i += 1
print(n_num)
print(sum(n_num))
