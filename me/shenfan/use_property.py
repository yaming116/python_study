#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

'a test module for property'

class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError('_width must int')
        if width < 0:
            raise ValueError("width < 0")
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError('height must int')
        if height < 0:
            raise ValueError("height < 0")
        self._height = height

    @property
    def resolution(self):
        return self._height * self._width



if __name__ == '__main__':
    s = Screen()
    s.width = 1024
    s.height = 768
    print(s.resolution)
    assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution


