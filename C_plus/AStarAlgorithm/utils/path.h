// Copyright (c) 2021 Trunk.Tech. All rights reserved.
//

#ifndef ASTAR_PATH_H
#define ASTAR_PATH_H
#include <vector>
using namespace std;
namespace eric {
    namespace path {
        struct Coordinate
        {
            int x;
            int y;
        };
        struct PathList : Coordinate
        {
            Coordinate historical;
            Coordinate current;
            double cost_f;
            double cost_g;
            double cost_h;
            char type;
        };

        struct MapInfo
        {
            pair<int, int> map_start;
            pair<int, int> map_end;
            pair<int, int> boundary;
        };
        typedef vector<PathList> global_map;
        typedef MapInfo map_info;

    }
}
#endif //ASTAR_PATH_H
