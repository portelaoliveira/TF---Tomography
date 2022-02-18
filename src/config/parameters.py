from config.calculate_start_sensor import start_sensors 

# Acquisition parameters

bh_spacing = 10.0 # Metros eixo x
bh_length = 10.0  # Metros eixo y
sensor_spacing_x = 1.0 # Metros
sensor_spacing_y = 1.0 # Metros
source_spacing_x = 4.0 # Metros
source_spacing_y = 6.0 # Metros
start_source_x = 3.0 # Metros
start_source_y = 2.0 # Metros
n_gx = 4 # Número de geofones em X
n_gy = 6 # Número de geofones em Y
start_x, start_y = start_sensors(bh_spacing, bh_length, n_gx, n_gy, sensor_spacing_x, sensor_spacing_y)
length_gx = n_gx * sensor_spacing_x + start_x # Metros
length_gy = n_gy * sensor_spacing_y + start_y # Metros
n_sx = 2 # Número de fontes em X
n_sy = 2 # Número de fontes em Y
length_sx = n_sx * source_spacing_x + start_source_x # Metros
length_sy = n_sy * source_spacing_y + start_source_y # Metros

# Create forward model and mesh

cb_spacing = 1.0 # Metros
cb_length = 1.0  # Metros

#Criação da grade de inversão
refinement = 0.25 