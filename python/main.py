#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Time   : 2020/12/29
Author : Jin Xinyu
"""
from AStar.a_star import AStar
from draw_the_path import draw_the_path


if __name__ == '__main__':
    aStar = AStar()
    aStar.run()
    draw_the_path(aStar.points['end_x'], aStar.points['end_y'], aStar.global_path)