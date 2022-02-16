from tkinter import Tk
from tkinter.filedialog import askopenfilename
from typing import Any, Dict, List

def formatted_data(data: List[List]) -> List[Dict[str, Any]]:
    filterd_data = []
    data = data[1:]

    quantity_source = data.pop(0)[1]
    quantity_sensors = data.pop(0)[1]

    for item in range(int(quantity_source)):
        filterd_data.append(
            {
                "id": item + 1,
                "data": [ { 
                    "id": item[0],
                    "travel_time": item[1]
                 } for item in data[:int(quantity_sensors)]] 
            
            }
        )

        data = data[int(quantity_sensors)+1:]

    return filterd_data


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

r = formatted_data(read_field_data())
print(r)