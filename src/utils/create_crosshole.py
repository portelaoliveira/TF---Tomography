import numpy as np
import pygimli as pg
from typing import Dict, List

def createSeismicData(sensors: List[Dict], rays: List[Dict], type: str) -> List[List]:
    """
    Create crosshole scheme assuming two boreholes with an equal number of sensors.

    Parameters
    ----------
    sensors : array (Nx2)
        Array with position of sensors.

    Returns
    -------
    scheme : DataContainer
        Data container with `sensors` predefined sensor indices 's' and 'g' for shot and receiver numbers.
    """

    # Empty container
    scheme = pg.DataContainer()

    # Add sensors
    for sen in sensors:
        scheme.createSensor(sen)

    # Add measurements
    scheme.resize(len(rays))
    if type == 's':
        scheme["s"] = rays[:, 0]
        scheme["valid"] = np.ones(len(rays))
        scheme.registerSensorIndex("s")
    elif type == 'g':
        scheme["g"] = rays[:, 1]
        scheme["valid"] = np.ones(len(rays))
        scheme.registerSensorIndex("g")
    elif type == 'both':
        scheme["s"] = rays[:, 0]
        scheme["g"] = rays[:, 1]
        scheme["valid"] = np.ones(len(rays))
        scheme.registerSensorIndex("s")
        scheme.registerSensorIndex("g")
    return scheme