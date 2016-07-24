#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"a test object"

__author__="yaming"

import types

class Student:

    def __init__(self, name, score):
        self.__name = name
        self.score = score

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def print_score(self):
        # print('name: ' + self.name + ", score:"  + self.score)
        print('%s %s ' % (self.__name, self.score))


def test_student():

    mike = Student("mike", 60)

    mike.print_score()

    mike.age = 11

    print(mike.age)

    print(mike.score)

    mike.set_name("mike 2")

    print(mike.get_name())



class Animal:

    def run(self):
        print("Animal is run")

class Dog(Animal):

    def run(self):
        print("Dog is run")


class Cat(Animal):

    def run(self):

        print("Cat is run")


def test_Animal(animal):
    animal.run()

class Timer(object):

    def run(self):
        print("start ")

def fun():
    pass

class my_Dog(object):

    def __len__(self):
        return 100

if __name__ == '__main__':
    # test_student()
    #
    # test_Animal(Animal())
    # test_Animal(Dog())
    # test_Animal(Cat())
    # test_Animal(Timer())

    # print(type(123))
    #
    # print(type(Dog()))
    # print(type('1111'))
    #
    # print(type (abs))
    #
    # print(type(fun) == types.FunctionType)
    #
    # print(dir("ABC"))
    #
    # print(len(my_Dog()))




    animal = Animal()


    if hasattr(animal, 'name'):
        print("animal has name")

    animal.name = "test"

    print(animal)
    print(getattr(animal, 'name'))

    if hasattr(animal, 'name'):
        setattr(animal, 'name', 'hello')

    print(animal)
    print(getattr(animal, 'name'))







