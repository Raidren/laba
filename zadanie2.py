#Variant 5 - Zadanie 2
print('Введите количество чисел массива, а затем сами числа:')
b = []
n = int(input())
for i in range(n):
    b.append(int(input()))
b = [v for k,v in enumerate(b) if k%2] #Выбираем числа, которые только на четных позициях относительно самого языка программирования(0,1,2,3...), т.е в последоватальности 1,2,3,4  , будут выбраны 2,4
print('Числа на четных позициях:',b)
c = b.copy()
c = [x for x in c if not x%2]
o = len(c)
print('Числа на четных позициях и при этом четные:', c, 'Их количество:', o)




