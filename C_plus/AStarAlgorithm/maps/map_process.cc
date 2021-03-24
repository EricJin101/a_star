// Copyright (c) 2021 Trunk.Tech. All rights reserved.
//

#include "map_process.h"
namespace eric{
namespace a_star{
void map_process::map_generate (path::global_map& globalMap, path::map_info& mapInfo)
{
    cout << "Map generating ..." << endl;
    ifstream myfile("./maps/223.txt");
    ofstream outfile("out.txt",ios::app); //ios::app指追加写入
    string temp;
    int i{0};
    while(getline(myfile,temp)) //按行读取字符串
    {
        cout << "line : " << i << endl;
        cout << temp << endl;
        coordination_confirm(mapInfo, globalMap, temp, i);
        outfile<<temp;//写文件
        outfile<<endl;
        i ++ ;
    }
    mapInfo.boundary.first = temp.size();
    mapInfo.boundary.second = i;

    myfile.close();
    outfile.close();

}

    void map_process::coordination_confirm(path::map_info& mapInfo,
            path::global_map& globalMap,
            string map_line, int row) {
        path::PathList pathPoint{};
        for (int x_coord{0}; x_coord < map_line.size(); x_coord ++)
        {
            pathPoint.current.x = x_coord;
            pathPoint.current.y = row;
            pathPoint.historical.x = 0;
            pathPoint.historical.y = 0;
            pathPoint.cost_f = 0;
            pathPoint.cost_g = 0;
            pathPoint.cost_h = 0;
            pathPoint.type = map_line[x_coord];
            if (map_line[x_coord] == 's')
            {
                mapInfo.map_start.first = x_coord;
                mapInfo.map_start.second = row;
                pathPoint.historical.x = x_coord;
                pathPoint.historical.y = row;
            }else if (map_line[x_coord] == 'e')
            {
                mapInfo.map_end.first = x_coord;
                mapInfo.map_end.second = row;
            }
            globalMap.push_back(pathPoint);
            cout << "x_coordinate: " << x_coord << endl;
        }
        cout << "map generate finished" << endl;
    }


    void print_map()
    {

    }
}
}
