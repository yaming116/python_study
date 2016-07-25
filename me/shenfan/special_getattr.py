#!/usr/bin/env python3
# _*_ coding; utf-8 _*_

class Student(object):

    def __init__(self):
        self.name = "mike"

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


s = Student()
print(s.name)
print(s.score)
print(s.age())
# AttributeError: "Student" object has no attribute 'grade'
print(s.grade)
