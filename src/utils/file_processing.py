import numpy as np
import json
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfile
from typing import Any, Dict, List, Tuple

def generate_data(start_x: float, start_y: float, length_gx: float, length_gy: float, spacing_x: float, spacing_y: float, sensor_or_source:bool = False) -> List[Dict]:
    results = []
    count = 0
    inverse = True

    if not sensor_or_source:
        for x in np.arange(start_x, length_gx, spacing_x):
            inverse = not inverse
            signal = -1 if inverse else 1
            for y in np.arange( length_gy - spacing_y if inverse else start_y, start_y - spacing_y  if inverse else length_gy,  signal * spacing_y ):
                count += 1
                results.append({
                    "sensor_id":count,
                    "coord_sensor_x":x,
                    "coord_sensor_y": y 
                })

        return results
    
    for x in np.arange(start_x, length_gx, spacing_x):
        for y in np.arange(start_y, length_gy, spacing_y):
            count = count + 1
            results.append({
                "source_id":count,
                "coord_source_x":x,
                "coord_source_y":y
            })
    return results 

def save_file(data: List[Dict]):
    Tk().withdraw() 
    try:
        with asksaveasfile(mode="w", defaultextension=".json") as file:
            file.write(json.dumps(data))
    except:
        print("O processo foi cancelado")

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
                **sensor,
                **genereted_sensor_date[count],
                "source_id": count_id,
                "coord_source_x": genereted_source_date[count_id-1]["coord_source_x"],
                "coord_source_y": genereted_source_date[count_id-1]["coord_source_y"],
            }
            )
            count += 1
    
    return result

r = formatted_data(read_field_data())
genereted_sensor_date = generate_data(3.5, 2.5, 7.5, 8.5, 1.0, 1.0)
genereted_source_date = generate_data(3.0, 2.0, 11.0, 14.0, 4.0, 6.0, True)
result = joing_datas(
        genereted_source_date=genereted_source_date,
        genereted_sensor_date=genereted_sensor_date,
        date_formatted=r[0]
    )
file_name = save_file(result)
# print(result)