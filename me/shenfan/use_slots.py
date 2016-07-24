#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

'a test module for slots'

__author__='yaming'

from types import MethodType

class Student:
    __slots__=('name', 'age')


def set_age(self, age):
    self.age = age

if __name__ == '__main__':
    student = Student()

    student.name = 'mike';

    print(student.name)

    student.set_age = MethodType(set_age, student)

    student.set_age(20)

    print(student.age)

    Student.set_age = set_age

    studentLi = Student()

    studentLi.set_age(20)

    print(studentLi.age)

    student.test = 1


