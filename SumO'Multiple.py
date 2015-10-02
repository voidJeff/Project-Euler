num = list(range(1, 1001))
n = 0
while n < len(num):
    if num[n]%3 != 0 or num[n]%5 != 0:
        if num.count(num[n]) != 0:
            num.remove(num[n])
    n += 1
print(num)
print(sum(num))
