from config.parameters import*
from itertools import product
from components.file_dialog import save_file, read_file
from utils.convert_array import array_convert_sensor_or_source
from utils.create_crosshole import createSeismicData
import numpy as np
import pygimli as pg
from utils.create_model_graphics import create_model_and_mesh, inversion_mesh_grid, invert, travel_time_manager, true_model_and_inversion_result, visualized_rays
from utils.data import generate_data
from utils.world import create_world

pg.utils.units.quants['vel']['cMap'] = 'inferno_r'

world = create_world([0.0, (bh_length)], [(bh_spacing), 0.0], 0)
g = generate_data(start_x, start_y, length_gx, length_gy, sensor_spacing_x, sensor_spacing_y)
filename = save_file(g)
g = read_file()
geo = array_convert_sensor_or_source(g)
elements=[]
elements = array_convert_sensor_or_source(g)
ga = np.array(geo)
ng = len(geo)
numbersg = np.arange(ng)

s = generate_data(start_source_x, start_source_y, length_sx, length_sy, source_spacing_x, source_spacing_y, True)
filename = save_file(s)
s = read_file()
sour = array_convert_sensor_or_source(s, True)
sa = np.array(sour)
ns = len(sour)
numberss = np.arange(ns)

rays = np.array(list(product(numbersg, numberss + ng)))

elements = [*elements, *sour]

sensors = np.array(elements)

concrete_block = create_world([((bh_length)/2)-cb_length*0.5, ((bh_spacing)/2)+cb_spacing*0.5], [((bh_length)/2)+cb_length*0.5, ((bh_spacing)/2)-cb_spacing*0.5], 1)

geom = world + concrete_block

for sen in sensors:
    geom.createNode(sen)

mesh_fwd, model = create_model_and_mesh(geom)

scheme = createSeismicData(sensors,rays,'both')

tt, data = travel_time_manager(mesh_fwd, scheme, model)

mesh = inversion_mesh_grid(0, bh_spacing + refinement, bh_length + refinement, 
                            refinement, ga[:, 0], ga[:, 1], sa[:, 0], sa[:, 1])

invmodel = invert(tt, data, mesh)

fig, ax = true_model_and_inversion_result(mesh_fwd, model, tt, 
                                            ga[:, 0], ga[:, 1], sa[:, 0], sa[:, 1])

fig, ax = visualized_rays(tt, ga[:, 0], ga[:, 1], sa[:, 0], sa[:, 1])
