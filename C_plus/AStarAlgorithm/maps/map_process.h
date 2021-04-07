// Copyright (c) 2021 Trunk.Tech. All rights reserved.
//

#ifndef ASTAR_MAP_PROCESS_H
#define ASTAR_MAP_PROCESS_H

#include <iostream>
#include <fstream>
#include <vector>
#include "../utils/path.h"
using namespace std;
namespace eric {
    namespace a_star {
        class map_process {
        public:
            static void map_generate(path::global_map& globalMap, path::map_info& mapInfo);
            static void coordination_confirm(path::map_info& mapInfo, path::global_map& globalMap, string map_line, int row);
        };
    }
}
#endif //ASTAR_MAP_PROCESS_H
