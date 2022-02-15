from typing import Dict, List

def array_convert(data:List[Dict])-> List[List]:
    result = []
    for item in data:
        result.append([item['coord_x'], item['coord_y']])
    return result