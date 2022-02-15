
def start_sensors(bh_spacing: float, bh_length: float, n_gx: float, n_gy: float, sensor_spacing_x: float, sensor_spacing_y: float) -> float:
    start_x = (bh_spacing + sensor_spacing_x - (n_gx * sensor_spacing_x))/2 
    start_y = (bh_length + sensor_spacing_y - (n_gy * sensor_spacing_y))/2 
    return start_x, start_y
