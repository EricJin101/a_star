// Copyright (c) 2021 Trunk.Tech. All rights reserved.
//

#ifndef ASTAR_MAP_PROCESS_H
#define ASTAR_MAP_PROCESS_H

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
namespace eric {
    namespace a_star {
        struct PathPoint
        {
            double x;
            double y;
            double cost;
        };

        struct GlobalMap : PathPoint
        {
            PathPoint pt;
        };
        class map_process {
        public:
            typedef vector<GlobalMap> global_map;

            void map_generate(const GlobalMap &global_map);
        };
    }
}
#endif //ASTAR_MAP_PROCESS_H
