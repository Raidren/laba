print('Введите количество чисел, а затем сами числа, которые будут сортироваться:')
a = []
N = int(input())
for i in range(N):
    a.append(int(input()))

i = 0
while i < N - 1:
    j = 0
    while j < N - 1 - i:
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
        j += 1
    i += 1

print(a)