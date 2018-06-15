#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Comment

__author__ = 'qiunet'

import random
from types import LambdaType
from types import FunctionType
from types import BuiltinFunctionType
from collections import Iterable


def randomInt(start: int, end: int) -> int:
    """
    随机整数
    :param start: 开始数
    :param end: 结束数
    :return: 随机整数
    """
    return random.randint(start, end)


def randomFloat(start: int, end: int) -> float:
    """
    随机浮点数
    :param start: 开始数
    :param end: 结束数
    :return: 随机浮点
    """
    return random.uniform(start, end)


def isPowerOfTwo(num: int) -> bool:
    """
    判断一个数, 是否是2的幂数
    :param num: 整数
    :return: bool
    """
    return (num & -num) == num


def sort(it: Iterable, reverse: bool= False, key: [FunctionType or LambdaType or BuiltinFunctionType]=None):
    """
    排序
    :param it: 
    :param reverse: 
    :param key: 
    :return: 
    """
    return list(sorted(it, key=key, reverse=reverse))


def forceToInt(num) -> int:
    """
    强转int (python 只有一种整数数据类型. int 但是指的是长整型 )
    :param num: 整数 
    :return: int
    """
    return num & 0xFFFFFFFF


def forceToShort(num) -> int:
    """
    强转short
    :param num: 整数 
    :return: short
    """
    return num & 0xFFFF


def forceToByte(num) -> int:
    """
    强转byte
    :param num: 整数 
    :return: byte
    """
    return num & 0xFF
