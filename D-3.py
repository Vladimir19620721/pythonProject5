"""Ввести строку. Вывести на экран букву, которая находится в середине этой строки.
Также, если эта центральная буква равна первой букве в строке, то создать и вывести часть строки между первым и последним символами исходной строки.
(подсказка: для получения центральной буквы, найдите длину строки и разделите ее пополам. Для создания результирующий строки используйте срез)"""

a = input()
s = len(a)
d = int(s/2)
f = s-1
g =a[d]
print(g)
if a[0] == a[d]:
    print(a[1:d])

