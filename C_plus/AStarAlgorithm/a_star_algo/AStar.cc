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
        cout << "aaaaaaaaaa" << mapInfo.map_start.first << endl;
        cout << mapInfo.map_start.second << endl;
        cout << globalMap[idx].type << endl;
        cout << globalMap[idx].current.x << endl;
        cout << globalMap[idx].current.y << endl;
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