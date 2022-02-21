from tkinter import Tk
from tkinter.filedialog import askopenfilename
from typing import Any, Dict, List, Tuple

def formatted_data(data: List[List]) -> Tuple[List, int, int]:
    filterd_data = []
    data = data[1:]

    quantity_source = data.pop(0)[1]
    quantity_sensors = data.pop(0)[1]

    for item in range(int(quantity_source)):
        filterd_data.append(
            {
                "sensor_id": item + 1,
                "sensors": [ { 
                    "sensor_id": item[0],
                    "travel_time": item[1]
                 } for item in data[:int(quantity_sensors)]] 
            
            }
        )

        data = data[int(quantity_sensors)+1:]

    return filterd_data, quantity_source, quantity_sensors


def read_field_data() -> List[List]:
    Tk().withdraw()
    filename = askopenfilename(defaultextension=".vs")
    result = []
    with open(filename, "r") as file:
        for data in file:
            data = data.split()
            data = [float(item) for item in data]
            result.append(data)
    return result      

def joing_datas(genereted_source_date: List[Dict],genereted_sensor_date: List[Dict], date_formatted: List[Dict[str, Any]]):
    result = []
    count_id = 0
    for source in date_formatted:
        count = 0
        count_id += 1

        for sensor in source["sensors"]:
            result.append(
                {
                "trace_id": f'S{count_id:04d}G{int(sensor["sensor_id"]):04d}',
                **sensor,
                **genereted_sensor_date[count],
                "source_id": count_id,
                "coord_source_x": genereted_source_date[count_id-1]["coord_source_x"],
                "coord_source_y": genereted_source_date[count_id-1]["coord_source_y"],
            }
            )
            count += 1
            
    return result
    