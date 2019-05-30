#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-29 16:51
# @Author  : xiaolinzi
from playLA.Vector import Vector

if __name__ == '__main__':
    vec = Vector([5, 2])
    print(vec)
    print(len(vec))
    print('\nvec[0] = {}, vec[1] = {}'.format(vec[0], vec[1]))

    vec2 = Vector([3, 4])
    print('{} + {} = {}'.format(vec, vec2, vec + vec2))
    print('{} - {} = {}'.format(vec, vec2, vec - vec2))
    print('{} * {} = {}'.format(vec, 3, vec * 3))
    print('{} * {} = {}\n'.format(3, vec, 3 * vec))

    print('+{} = {}'.format(vec, +vec))
    print('-{} = {}'.format(vec, -vec))
