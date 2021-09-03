#Variant 5 - Zadanie 1
#21(3) = 2∙3^1+1∙3^0 = 6+1 = 7(10)
print('Введите количество чисел троичной системы счисления, а затем сами числа:')
b = []
n = int(input())
for i in range(n):
    b.append(int(input()))
number = 0
dlina = len(b)
for i in range(0, dlina):
    number = number + int(b[i])*(3**(dlina-i-1))
print(number)