a = [1, 0, 1, 0]
b = [0, 1, 0, 1]
n = 4
r = [0] * (2 * n - 1)
for i in range(n):
    for j in range(n):
        r[i + j] += a[i] * b[j]
print(r)