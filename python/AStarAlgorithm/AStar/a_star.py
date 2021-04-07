#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Time   : 2020/12/29
Author : Jin Xinyu
"""
"""
ATTENTION: subscript and coordinate
"""
import sys
MAX_INT=sys.maxsize


class MapGenerate:
    def __init__(self):
        self.points = {'start_x': 0.0, 'start_y': 0.0,
                       'end_x': 0.0, 'end_y': 0.0,
                       'threshold_we': 0, 'threshold_sn': 0}
        self.global_path = []
        self.file_path = '223.txt'

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
            if 'e' in p:
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
        self.open_list = []
        self.close_list = []
        self.global_path = []
        self.points = None
        self.find_path = False

    def generate_points(self):
        self.points = {'start_x': 0.0, 'start_y': 0.0,
                       'end_x': 0.0, 'end_y': 0.0,
                       'threshold_we': 0, 'threshold_sn': 0}

    def initialize_child(self):
        child = {
            'wn': {'x': 0, 'y': 0, 'f': 0, 'g': 0, 'h': 0}, 'n': {'x': 0, 'y': 0, 'f': 0, 'g': 0, 'h': 0},
            'en': {'x': 0, 'y': 0, 'f': 0, 'g': 0, 'h': 0}, 'w': {'x': 0, 'y': 0, 'f': 0, 'g': 0, 'h': 0},
            'e': {'x': 0, 'y': 0, 'f': 0, 'g': 0, 'h': 0}, 'ws': {'x': 0, 'y': 0, 'f': 0, 'g': 0, 'h': 0},
            's': {'x': 0, 'y': 0, 'f': 0, 'g': 0, 'h': 0}, 'es': {'x': 0, 'y': 0, 'f': 0, 'g': 0, 'h': 0}
        }
        return child

    def initialize_root_node(self):
        h = abs(self.points['end_x'] - self.points['start_x']) + abs(self.points['end_y'] - self.points['start_y'])
        self.global_path[self.points['start_x'] - 1][self.points['start_y'] - 1][2] = h
        self.global_path[self.points['start_x'] - 1][self.points['start_y'] - 1][4] = h
        self.global_path[self.points['start_x'] - 1][self.points['start_y'] - 1][0][0] = self.points['start_x']
        self.global_path[self.points['start_x'] - 1][self.points['start_y'] - 1][0][1] = self.points['start_y']
        self.close_list.append(
            {
                'father': [self.points['start_x'], self.points['start_y']],
                'itself': [self.points['start_x'], self.points['start_y']],
                'cost': [h, 0, h]  # f g h
            }
        )

    def data_prepare(self):
        self.generate_points()
        _map = MapGenerate()
        self.global_path, self.points = _map.read_from_file()
        self.initialize_root_node()
        self.core_a_star(self.points['start_x'], self.points['start_y'])

    def core_a_star(self, x, y):
        while not self.find_path:
            g = self.global_path[x - 1][y - 1][3]  # historical g, real g
            child = self.eight_direction(x, y, self.initialize_child(), self.points['threshold_we'], self.points['threshold_sn'], g)  # raw
            self.add_child_to_open_list(x, y, child)
            self.sequencing_cost_f()
            _coordinate = self.open_list[0]
            self.add_to_close_list(x, y, _coordinate)
            x = _coordinate['itself'][0]
            y = _coordinate['itself'][1]

    def run(self):
        self.data_prepare()

    def inspect_eight_node(self, _child):
        for c in _child:
            if self.child_valid_check(_child[c]):
                pass

    def add_to_close_list(self, x, y, _child):
        if not self.check_in_close_list(_child['itself'][0], _child['itself'][1]):
            self.close_list.append({
                'father': [x, y], 'itself': _child['itself'],
                'cost': _child['cost']
            })
            del self.open_list[0]
        if self.check_in_open_list(_child['itself'][0], _child['itself'][1]):
            pass

    def add_child_to_open_list(self, x, y, child):
        for c in child:
            if self.child_valid_check(child[c]):
                if not self.check_in_close_list(child[c]['x'], child[c]['y']):
                    if not self.check_in_open_list(child[c]['x'], child[c]['y']):
                        self.open_list.append({
                            'father': [x, y], 'itself': [child[c]['x'], child[c]['y']],
                            'cost': [child[c]['f'], child[c]['g'], child[c]['h']]
                        })
                        self.update_global_path(x, y, child[c])
                    else:  # in the open list
                        for _open in range(len(self.open_list)):
                            if self.open_list[_open]['itself'] == [child[c]['x'], child[c]['y']]:
                                if self.open_list[_open]['cost'][1] > child[c]['g']:
                                    self.open_list[_open]['father'] = [x, y]
                                    self.open_list[_open]['cost'][1] = child[c]['g']
                                    self.open_list[_open]['cost'][0] = self.open_list[_open]['cost'][2] + child[c]['g']
                                    self.update_global_path(x, y, child[c])
                else:  # already in this list
                    self.compare_child_node_cost_g(x, y, child[c])

    def eight_direction(self, _cx, _cy, child, th_we, th_sn, g):
        """
        :param _cx: coordinate x of current point
        :param _cy: coordinate y of current point
        :param child: 8 direction child node
        :param th_we: threshold west  - east
        :param th_sn: threshold south - north
        :return:
        """
        for i in child:
            if i == 'wn':
                if child['wn']['x'] == 0 and child['wn']['y'] == 0:
                    child['wn']['x'] = _cx - 1 if _cx - 1 > 0 else -1
                    child['wn']['y'] = _cy - 1 if _cy - 1 > 0 else -1
                    child['wn']['h'] = abs(child['wn']['x'] - self.points['end_x']) + abs(child['wn']['y'] - self.points['end_y'])
                    child['wn']['g'] = g + 1.4
                    child['wn']['f'] = child['wn']['h'] + child['wn']['g']
            elif i == 'n':
                if child['n']['x'] == 0 and child['n']['y'] == 0:
                    child['n']['x'] = _cx - 1 if _cx - 1 > 0 else -1
                    child['n']['y'] = _cy
                    child['n']['h'] = abs(child['n']['x'] - self.points['end_x']) + abs(child['n']['y'] - self.points['end_y'])
                    child['n']['g'] = g + 1
                    child['n']['f'] = child['n']['h'] + child['n']['g']
            elif i == 'en':
                if child['en']['x'] == 0 and child['en']['y'] == 0:
                    child['en']['x'] = _cx - 1 if _cx - 1 > 0 else -1
                    child['en']['y'] = _cy + 1 if _cy + 1 <= th_we else -1
                    child['en']['h'] = abs(child['en']['x'] - self.points['end_x']) + abs(child['en']['y'] - self.points['end_y'])
                    child['en']['g'] = g + 1.4
                    child['en']['f'] = child['en']['h'] + child['en']['g']
            elif i == 'w':
                if child['w']['x'] == 0 and child['w']['y'] == 0:
                    child['w']['x'] = _cx
                    child['w']['y'] = _cy - 1 if _cy - 1 > 0 else -1
                    child['w']['h'] = abs(child['w']['x'] - self.points['end_x']) + abs(child['w']['y'] - self.points['end_y'])
                    child['w']['g'] = g + 1
                    child['w']['f'] = child['w']['h'] + child['w']['g']
            elif i == 'e':
                if child['e']['x'] == 0 and child['e']['y'] == 0:
                    child['e']['x'] = _cx
                    child['e']['y'] = _cy + 1 if _cy + 1 <= th_we else -1
                    child['e']['h'] = abs(child['e']['x'] - self.points['end_x']) + abs(child['e']['y'] - self.points['end_y'])
                    child['e']['g'] = g + 1
                    child['e']['f'] = child['e']['h'] + child['e']['g']
            elif i == 'ws':
                if child['ws']['x'] == 0 and child['ws']['y'] == 0:
                    child['ws']['x'] = _cx + 1 if _cx + 1 <= th_sn else -1
                    child['ws']['y'] = _cy - 1 if _cy - 1 > 0 else -1
                    child['ws']['h'] = abs(child['ws']['x'] - self.points['end_x']) + abs(child['ws']['y'] - self.points['end_y'])
                    child['ws']['g'] = g + 1.4
                    child['ws']['f'] = child['ws']['h'] + child['ws']['g']
            elif i == 's':
                if child['s']['x'] == 0 and child['s']['y'] == 0:
                    child['s']['x'] = _cx + 1 if _cx + 1 <= th_sn else -1
                    child['s']['y'] = _cy
                    child['s']['h'] = abs(child['s']['x'] - self.points['end_x']) + abs(child['s']['y'] - self.points['end_y'])
                    child['s']['g'] = g + 1
                    child['s']['f'] = child['s']['h'] + child['s']['g']
            elif i == 'es':
                if child['es']['x'] == 0 and child['es']['y'] == 0:
                    child['es']['x'] = _cx + 1 if _cx + 1 <= th_sn else -1
                    child['es']['y'] = _cy + 1 if _cy + 1 <= th_we else -1
                    child['es']['h'] = abs(child['es']['x'] - self.points['end_x']) + abs(child['es']['y'] - self.points['end_y'])
                    child['es']['g'] = g + 1.4
                    child['es']['f'] = child['es']['h'] + child['es']['g']
        return child

    def sequencing_cost_f(self):
        if len(self.open_list) < 0:
            self.find_path = True
            return
        for i in range(len(self.open_list) - 1):
            for j in range(i + 1, len(self.open_list)):
                if self.open_list[i]['cost'][0] > self.open_list[j]['cost'][0]:
                    tem = self.open_list[i]
                    self.open_list[i] = self.open_list[j]
                    self.open_list[j] = tem

    def check_in_open_list(self, x, y):
        for c in self.open_list:
            if c['itself'] == [x, y]:
                return True
        return False

    def check_in_close_list(self, x, y):
        for c in self.close_list:
            if c['itself'] == [x, y]:
                return True
        return False

    def child_valid_check(self, _child):
        """
        :param _child: {'x': 0, 'y': 0, 'f': 0, 'g': 0, 'h': 0}
        :return: True or False
        """
        if _child['x'] > 0 and _child['y'] > 0 and self.global_path[_child['x'] - 1][_child['y'] - 1][5] != 'O':
            if self.global_path[_child['x'] - 1][_child['y'] - 1][5] == 'e':
                self.find_path = True
            return True
        return False

    def compare_child_node_cost_g(self, x, y, _child):
        # for c in range(len(self.open_list)):
        #     if self.open_list[c]['itself'] == [_child['x'], _child['y']]:
        #         if self.open_list[c]['cost'][1] > _child['g']:
        #             self.open_list[c]['cost'][1] = _child['g']
        #             self.open_list[c]['cost'][0] = _child['g'] + _child['h']
        #             self.open_list[c]['father'] = [x, y]
        for c in range(len(self.close_list)):
            if self.close_list[c]['itself'] == [_child['x'], _child['y']]:
                if self.close_list[c]['cost'][1] < _child['g']:
                    self.update_father_node([x, y], [_child['x'], _child['y']])

    def update_father_node(self, child, father):
        for _close in range(len(self.close_list)):
            if self.close_list[_close]['itself'] == child:
                self.close_list[_close]['father'] = father
                # pass

    def update_global_path(self, x, y, _child):

        self.global_path[_child['x'] - 1][_child['y'] - 1][0] = [x, y]
        self.global_path[_child['x'] - 1][_child['y'] - 1][2] = _child['f']
        self.global_path[_child['x'] - 1][_child['y'] - 1][3] = _child['g']
        self.global_path[_child['x'] - 1][_child['y'] - 1][4] = _child['h']
