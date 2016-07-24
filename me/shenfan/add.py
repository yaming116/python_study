#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

' a test model'

__author__ = 'yaming'

def add(x, y):
    if not isinstance(x,  (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("not int")
    return x + y


if __name__ == '__main__':
    print(add(1.2, 3.3 ))