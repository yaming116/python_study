#!/usr/bin/evn python3
# _*_ coding: utf-8 _*_

from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon

print('day1 = ' , day1)
print('Weekday.Tue = ' , Weekday.Tue)
print('Weekday[\'Tue\'] = ' , Weekday['Tue'])
print("Weekday.Tue.value = ", Weekday.Tue.value)
print('day1 == Weekday.Mon ?', day1 == Weekday.Mon)
print('day1 == Weekday.Tue ? ', day1 == Weekday.Tue)
print('day1 == Weekday(1) ? ', day1 == Weekday(1))


for name, member in Weekday.__members__.items():
    print(name, "=>", member)

Mouth = Enum('Mouth', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Mouth.__members__.items():
    print(name, '=>', member, ',', member.value)
