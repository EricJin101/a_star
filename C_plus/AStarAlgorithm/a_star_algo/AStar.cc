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

    void update_father_node()
    {
        //
    }

    void compare_child_node_cost_g(int x, int y, int child_id)
    {
        for (int id_close{0}; id_close < closeList.size(); ++id_close)
        {
            //
            if (closeList[id_close].x == x && closeList[id_close].y ==y
                    && closeList[id_close].cost_g < childList[child_id].cost_g)
            {
                update_father_node();
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

    bool check_in_open_list(int x, int y)
    {
        for (int i{0}; i < openList.size(); ++i)
        {
            if (openList[i].current.x == x && openList[i].current.y == y)
            { return true;}
        }
        return false;// can not find a point in close list
    }

    bool check_in_close_list(int x, int y)
    {
        for (int i{0}; i < closeList.size(); ++i)
        {
            if (closeList[i].current.x == x && closeList[i].current.y == y)
            { return true;}
        }
        return false;// can not find a point in close list
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

    void update_global_path(int x, int y, int child_idx)
    {
        globalMap[current_idx(x, y)].x = x;
        globalMap[current_idx(x, y)].y = y;
        globalMap[current_idx(x, y)].cost_f = childList[child_idx].cost_f;
        globalMap[current_idx(x, y)].cost_g = childList[child_idx].cost_g;
        globalMap[current_idx(x, y)].cost_h = childList[child_idx].cost_h;
    }

    void add_child_to_openlist(int x, int y)
    {
        for(int i = 0; i>childList.size(); ++i)
        {
            // valid check
            if (!check_child_valid(childList[i]))
            {
                continue;
            }
            if (!check_in_close_list(childList[i].current.x, childList[i].current.y))
            {
                if (!check_in_open_list(childList[i].current.x, childList[i].current.y))
                {
                    // update open list
                    path::PathList temp;
                    temp.current.x = childList[i].current.x;
                    temp.current.y = childList[i].current.y;
                    temp.historical.x = x;
                    temp.historical.y = y;
                    temp.cost_f = childList[i].cost_f;
                    temp.cost_g = childList[i].cost_g;
                    temp.cost_h = childList[i].cost_h;
                    openList.push_back(temp);
                    update_global_path(x,y,i);
                }else
                {
                    // compare child node,which one has a smaller g
                    for (int idx_open{0}; idx_open < openList.size(); ++i)
                    {
                        if (childList[i].current.x == openList[idx_open].current.x
                            && childList[i].current.y == openList[idx_open].current.y
                            && openList[idx_open].cost_g  > childList[i].cost_g)
                        {
                            openList[idx_open].historical.x = x;
                            openList[idx_open].historical.y = y;
                            openList[idx_open].cost_g = childList[i].cost_g;
                            openList[idx_open].cost_f = openList[idx_open].cost_g + openList[idx_open].cost_h;
                        }
                    }
                }
            }else{
                // in close list
                //compare_child_node_cost;
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
            add_child_to_openlist(x, y);
        }

    }
}
}