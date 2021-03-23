// Copyright (c) 2021 Trunk.Tech. All rights reserved.
//

#ifndef ASTAR_ASTAR_H
#define ASTAR_ASTAR_H
#include "../utils/path.h"
#include <cmath>

namespace eric {
namespace aStarAlgorithm{
        typedef vector<path::PathList> open_list;
        typedef vector<path::PathList> close_list;
        typedef vector<path::PathList> child_list;
        bool findPath;
        path::global_map globalMap;
        path::map_info mapInfo;
        child_list childList;
        static void Init();
}
}
#endif //ASTAR_ASTAR_H
