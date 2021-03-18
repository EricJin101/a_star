#include "maps/map_process.cc"

int main()
{
    cout << "A Start Algorithm Starting ..." << endl;
    eric::a_star::map_process mapProcess;
    eric::a_star::GlobalMap globalMap{};
    mapProcess.map_generate(globalMap);
}