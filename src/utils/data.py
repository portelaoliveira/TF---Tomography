import numpy as np
from typing import List, Dict


def generate_data(start_x: float, start_y: float, length_gx: float, length_gy: float, spacing_x: float, spacing_y: float, fg:bool = False) -> List[Dict]:
    results = []
    count = 0
    inverse = True

    if not fg:
        for x in np.arange(start_x, length_gx, spacing_x):
            inverse = not inverse
            signal = -1 if inverse else 1
            for y in np.arange( length_gy - 1 if inverse else start_y, start_y - 1  if inverse else length_gy,  signal * spacing_y ):
                count += 1
                results.append({
                    "id":count,
                    "coord_x":x,
                    "coord_y": y 
                })

        return results
    
    for x in np.arange(start_x, length_gx, spacing_x):
        for y in np.arange(start_y, length_gy, spacing_y):
            count = count + 1
            results.append({
                "id":count,
                "coord_x":x,
                "coord_y":y
            })
    return results 
    

# r = generate_data(3.0, 2.0, 11.0, 14.0, 4.0, 6.0)
# print(r)