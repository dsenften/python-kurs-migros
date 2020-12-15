sum = 0

old_sum = -1
eps = 0.00001
i = 1

while sum - old_sum > eps:
    old_sum = sum
    sum += i
    i /= 2
    print(i, sum)
