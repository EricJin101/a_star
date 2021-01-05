#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Time   : 2020/12/29
Author : Jin Xinyu
"""


def draw_the_path(x, y, global_path):
    fp = global_path[x - 1][y - 1][0]
    while True:
        if global_path[fp[0] - 1][fp[1] - 1][5] == 's':
            break
        else:
            global_path[fp[0] - 1][fp[1] - 1][5] = ' '
        fp = global_path[fp[0] - 1][fp[1] - 1][0]

    for j in global_path:
        ttttt = ''
        for i in j:
            ttttt += i[5] + ' '
        print(ttttt)
        ttttt = ''