// Copyright (c) 2021 Eric Jin. All rights reserved.
//
#include "AStar.h"
namespace eric{
namespace aStarAlgorithm {
    void Init()
    {
        cout << "Initializing open_list, close_list, global_map..." << endl;
        open_list openList{};
        close_list closeList{};
        findPath = false;
    }
    void data_prepare()
    {
        a_star::map_process mapProcess;
        mapProcess.map_generate(globalMap, mapInfo);
    }

    void initialize_root_node()
    {
        //UPDATE ALL G
        int idx = mapInfo.map_start.first + mapInfo.map_start.second * 5;
        // 初始化所有代价
        for (int i{0}; i < mapInfo.boundary.second; ++i)
        {
            for (int j{0}; j < mapInfo.boundary.first; ++j)
            {
                int temp_id = i + j * mapInfo.boundary.first;
                double h = abs(mapInfo.map_end.first - j) + abs(mapInfo.map_end.second - i);
                globalMap[temp_id].cost_f = 0 + h;
                globalMap[temp_id].cost_g = 0;
                globalMap[temp_id].cost_h = h;
            }
        }

    }

    int current_idx(int x, int y)
    {
        return x + mapInfo.boundary.first * y;
    }

    double manhattan_dis(int x1, int y1, int x2, int y2)
    {
        return abs(x1 - x2) + abs(y1 - y2);
    }

    bool check_in_close_list()
    {

    }

    bool check_child_valid(path::PathList pathList)
    {
        if ((pathList.current.x > 0) && (pathList.current.y > 0 ) && globalMap[current_idx(pathList.current.x, pathList.current.y)].type != 'O')
        {
            if (globalMap[current_idx(pathList.current.x, pathList.current.y)].type != 'O')
            {
                findPath = true;
            }
            return true;
        }
        return false;
    }

    void add_child_to_openlist()
    {
        for(int i = 0; i>childList.size(); ++i)
        {
            // valid check
            if (!check_child_valid(childList[i]))
            {
                continue;
            }

        }
    }


    void eight_direction(int x, int y)
    {// 0 - 7, 8个方向。东、东北、北、西北、西、西南、南、东南
        for (int i{0}; i < 8; ++i)
        {
            path::PathList point{};
            cout << "sin: " << round(sin(i * 45* M_PI / 180)) << endl;
            double delta_x = round(cos(i * 45* M_PI / 180));
            double delta_y = round(sin(i * 45* M_PI / 180));
            point.current.x = x + delta_x > 0 ? x + delta_x : -1;
            point.current.y = y + delta_y > 0 ? y + delta_y : -1;
            point.cost_g = globalMap[current_idx(x, y)].cost_g + 1.414;
            point.cost_h = manhattan_dis(point.current.x, point.current.y, mapInfo.map_end.first, mapInfo.map_end.second);
            point.cost_f = point.cost_g + point.cost_h;
            childList.push_back(point);
        }
    }


    void core_aStar(int x, int y)
    {
        // x y 即将处理的点，默认为起点
        cout << "findPath" << findPath << endl;
        data_prepare();
        initialize_root_node();
        cout << "done " << endl;
        while (!findPath)
        {
            double g = globalMap[mapInfo.map_start.first + mapInfo.map_start.second * 5].cost_g;
            eight_direction(x, y);
        }

    }
}
}