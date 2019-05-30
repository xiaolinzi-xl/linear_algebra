#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-29 16:43
# @Author  : xiaolinzi
class Vector:

    def __init__(self, lst):
        self._values = list(lst)

    def __repr__(self):
        return 'Vector({})'.format(self._values)

    def __str__(self):
        return '({})'.format(', '.join(str(e) for e in self._values))

    # 表示返回向量长度（有多少个元素）
    def __len__(self):
        return len(self._values)

    # 取向量的第 index 个元素
    def __getitem__(self, item):
        return self._values[item]

    # 返回向量的迭代器
    def __iter__(self):
        return self._values.__iter__()

    # 向量加法，返回结果向量
    def __add__(self, other):
        assert len(self) == len(other), 'Error in adding. Length of vectors must be same.'
        return Vector([a + b for a, b in zip(self, other)])

    # 向量减法
    def __sub__(self, other):
        assert len(self) == len(other), 'Error in subtracting. Length of vectors must be same.'
        return Vector([a - b for a, b in zip(self, other)])

    # 返回数量乘法的结果：self * k
    def __mul__(self, k):
        return Vector([k * e for e in self])

    # 返回数量乘法的结果：k * self
    def __rmul__(self, k):
        return self * k

    # 返回向量取正的结果向量
    def __pos__(self):
        return 1 * self

    # 返回向量取负的结果向量
    def __neg__(self):
        return -1 * self
