#include "maps/map_process.cc"
#include "a_star_algo/AStar.cc"
#include <time.h>
int main()
{
    cout << "A Start Algorithm Starting ..." << endl;
    eric::a_star::map_process mapProcess;
//    mapProcess.map_generate();
    eric::aStarAlgorithm::Init();
    eric::aStarAlgorithm::core_aStar(0,2);
    return 0;
}