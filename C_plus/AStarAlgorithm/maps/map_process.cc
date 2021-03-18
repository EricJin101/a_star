// Copyright (c) 2021 Trunk.Tech. All rights reserved.
//

#include "map_process.h"
namespace eric{
namespace a_star{
void map_process::map_generate (const GlobalMap& global_map){
    cout << "Map generating ..." << endl;
    ifstream myfile("./maps/123.txt");
    ofstream outfile("out.txt",ios::app); //ios::app指追加写入
    string temp;
    while(getline(myfile,temp)) //按行读取字符串
    {
        cout << temp << endl;
        global_map.x = 1;
        global_map.y =1;
        outfile<<temp;//写文件
        outfile<<endl;
    }
    myfile.close();
    outfile.close();

}

}
}
