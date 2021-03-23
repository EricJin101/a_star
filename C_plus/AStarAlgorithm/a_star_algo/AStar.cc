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

    void core_aStar(int x, int y)
    {
        cout << "findPath" << findPath << endl;
        data_prepare();
        initialize_root_node();
        cout << "done " << endl;

    }
}
}