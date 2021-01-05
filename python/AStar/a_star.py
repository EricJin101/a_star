#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Time   : 2020/12/29
Author : Jin Xinyu
"""
"""
ATTENTION: subscript and coordinate
"""


class MapGenerate:
    def __init__(self):
        self.points = {'start_x': 0.0, 'start_y': 0.0,
                       'end_x': 0.0, 'end_y': 0.0,
                       'threshold_we': 0, 'threshold_sn': 0}
        self.global_path = []
        self.file_path = '123.txt'

    def read_from_file(self):
        _list = []
        _points = []
        with open(self.file_path, 'r') as f:
            _list.append(f.readlines())
        _i = 0
        self.points['threshold_we'] = len(_list[0][0]) - 1
        self.points['threshold_sn'] = len(_list[0])
        for p in _list[0]:
            if 's' in p:
                self.points['start_y'] = p.find('s') + 1
                self.points['start_x'] = _i + 1
            elif 'e' in p:
                self.points['end_y'] = p.find('e') + 1
                self.points['end_x'] = _i + 1
            _y = 1
            for _j in p[0:self.points['threshold_we']]:
                point = [[0, 0], [_i + 1, _y], 0, 0, 0, _j]
                _points.append(point)
                _y += 1
            self.global_path.append(_points)
            _points = []
            _i += 1
        return self.global_path, self.points


class AStar:
    def __init__(self):
        self.global_path = []
        self.points = None
        self.find_path = False

    def generate_points(self):
        self.points = {'start_x': 0.0, 'start_y': 0.0,
                       'end_x': 0.0, 'end_y': 0.0,
                       'threshold_we': 0, 'threshold_sn': 0}

    def initialize_child(self):
        child = {
            'wn': {'x': 0, 'y': 0}, 'n': {'x': 0, 'y': 0}, 'en': {'x': 0, 'y': 0}, 'w': {'x': 0, 'y': 0},
            'e': {'x': 0, 'y': 0}, 'ws': {'x': 0, 'y': 0}, 's': {'x': 0, 'y': 0}, 'es': {'x': 0, 'y': 0}
        }
        return child

    def data_prepare(self):
        self.generate_points()
        _map = MapGenerate()
        self.global_path, self.points = _map.read_from_file()
        _c_x = self.points['start_x']
        _c_y = self.points['start_y']
        _e_x = self.points['end_x']
        _e_y = self.points['end_y']
        h = abs(_e_x - _c_x) + abs(_e_y - _c_y)
        self.global_path[_c_x - 1][_c_y - 1][2] = h
        self.global_path[_c_x - 1][_c_y - 1][4] = h
        self.global_path[_c_x - 1][_c_y - 1][0][0] = _c_x
        self.global_path[_c_x - 1][_c_y - 1][0][1] = _c_y

        child = self.eight_direction(_c_x, _c_y, self.initialize_child(), self.points['threshold_we'], self.points['threshold_sn'])
        self.global_path = self.find_father_node(child, self.global_path, self.global_path[_c_x - 1][_c_y - 1])
        traversal = 1
        while not self.find_path:
            for g in self.global_path:
                for q in g:
                    if q[3] == traversal:
                        _child = self.initialize_child()
                        _child = self.eight_direction(q[1][0], q[1][1], _child, self.points['threshold_we'], self.points['threshold_sn'])
                        self.global_path = self.find_father_node(_child, self.global_path, self.global_path[q[1][0] - 1][q[1][1] - 1])
            traversal += 1
            if traversal > self.points['threshold_we'] + self.points['threshold_sn']:
                break

    def run(self):
        self.data_prepare()

    def eight_direction(self, _cx, _cy, child, th_we, th_sn):
        for i in child:
            if i == 'wn':
                if child['wn']['x'] == 0 and child['wn']['y'] == 0:
                    # this point not traversal
                    child['wn']['x'] = _cx - 1 if _cx - 1 > 0 else -1
                    child['wn']['y'] = _cy - 1 if _cy - 1 > 0 else -1
            elif i == 'n':
                if child['n']['x'] == 0 and child['n']['y'] == 0:
                    child['n']['x'] = _cx - 1 if _cx - 1 > 0 else -1
                    child['n']['y'] = _cy
            elif i == 'en':
                if child['en']['x'] == 0 and child['en']['y'] == 0:
                    child['en']['x'] = _cx - 1 if _cx - 1 > 0 else -1
                    child['en']['y'] = _cy + 1 if _cy + 1 <= th_we else -1
            elif i == 'w':
                if child['w']['x'] == 0 and child['w']['y'] == 0:
                    child['w']['x'] = _cx
                    child['w']['y'] = _cy - 1 if _cy - 1 > 0 else -1
            elif i == 'e':
                if child['e']['x'] == 0 and child['e']['y'] == 0:
                    child['e']['x'] = _cx
                    child['e']['y'] = _cy + 1 if _cy + 1 <= th_we else -1
            elif i == 'ws':
                if child['ws']['x'] == 0 and child['ws']['y'] == 0:
                    child['ws']['x'] = _cx - 1 if _cx - 1 > 0 else -1
                    child['ws']['y'] = _cy - 1 if _cy - 1 > 0 else -1
            elif i == 's':
                if child['s']['x'] == 0 and child['s']['y'] == 0:
                    child['s']['x'] = _cx + 1 if _cx + 1 <= th_sn else -1
                    child['s']['y'] = _cy
            elif i == 'es':
                if child['es']['x'] == 0 and child['es']['y'] == 0:
                    child['es']['x'] = _cx + 1 if _cx + 1 <= th_sn else -1
                    child['es']['y'] = _cy + 1 if _cy + 1 <= th_we else -1
        return child

    def find_father_node(self, child, global_path, current_point):
        """
        :param child: 8 direction coordinate
        :param global_path:
        :param current_point: father node
        :return:
        """
        for i in child:
            if child[i]['x'] > 0 and child[i]['y'] > 0:
                # this child node is valid
                if global_path[child[i]['x'] - 1][child[i]['y'] - 1][0][0] == 0:
                    # record is's father node
                    if global_path[child[i]['x'] - 1][child[i]['y'] - 1][5] == '#':
                        global_path[child[i]['x'] - 1][child[i]['y'] - 1][0][0] = current_point[1][0]
                        global_path[child[i]['x'] - 1][child[i]['y'] - 1][0][1] = current_point[1][1]

                        g = global_path[current_point[1][0] - 1][current_point[1][1] - 1][3] + 1
                        h = abs(self.points['end_y'] - child[i]['y']) + abs(self.points['end_x'] - child[i]['x'])
                        global_path[child[i]['x'] - 1][child[i]['y'] - 1][2] = g + h  # f
                        global_path[child[i]['x'] - 1][child[i]['y'] - 1][3] = g  # g real distance to current point
                        global_path[child[i]['x'] - 1][child[i]['y'] - 1][4] = h  # h manhattan distance
                    elif global_path[child[i]['x'] - 1][child[i]['y'] - 1][5] == 'O':
                        global_path[child[i]['x'] - 1][child[i]['y'] - 1][0][0] = -1
                        global_path[child[i]['x'] - 1][child[i]['y'] - 1][0][1] = -1
                        global_path[child[i]['x'] - 1][child[i]['y'] - 1][2] = -1  # f
                        global_path[child[i]['x'] - 1][child[i]['y'] - 1][3] = -1  # g real distance to current point
                        global_path[child[i]['x'] - 1][child[i]['y'] - 1][4] = -1
                    elif global_path[child[i]['x'] - 1][child[i]['y'] - 1][5] == 'e':
                        print('Find end point at: ', current_point[1][0], current_point[1][1])
                        global_path[child[i]['x'] - 1][child[i]['y'] - 1][0][0] = current_point[1][0]
                        global_path[child[i]['x'] - 1][child[i]['y'] - 1][0][1] = current_point[1][1]
                        self.find_path = True
                        return global_path
        return global_path
