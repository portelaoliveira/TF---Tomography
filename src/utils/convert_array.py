from typing import Dict, List

def array_convert_sensor_or_source(data:List[Dict], array_convert_sensor_or_source:bool = False)-> List[List]:

    if not array_convert_sensor_or_source:
        result = []
        for item in data:
            result.append([item['coord_sensor_x'], item['coord_sensor_y']])
        return result

    result = []
    for item in data:
        result.append([item['coord_source_x'], item['coord_source_y']])
    return result
