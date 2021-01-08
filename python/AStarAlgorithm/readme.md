# A Star Algorithm 
### Generate Map

### Core of A Star 

- 1 Find Star Point and End Point
- 2 Initialize open list and close list

    Add start point into close list, and current point at start point
- 2 Loop until find end point

    a : see current point as father node, find child node in 8 direction. Including it's coordinate, f,g,h
    
    b : check child node is valid or not, if valid, add it into open list:
        
        i : if this child node not in open list, add it into the list;
        
        ii : if this child node already in open list, compare value 'g' of child node and open list, if child node is better,
        which means through child node will take fewer steps to this point, update 'father' coordinate and cost in open list

        iii : if child node in close list: 
        compare value 'g' of child node and close list, if child node is better, update 'father' coordinate and cost in close list
    
    c : sort the order of open list according to it's value of 'f'
    
    d : update current point, prepare to process the point in open list has smallest value 'f'
    
    e : add new current point into close list

### Result
![aStarResult](aStarResult.png)

