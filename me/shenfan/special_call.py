#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

class Student(object):

    def __init__(self, name):
        self.name = name


    def __call__(self):
        print('My name is %s.' % self.name)


s = Student('mike')
s()

