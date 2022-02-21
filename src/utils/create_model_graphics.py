import pygimli as pg
import matplotlib.pyplot as plt
import pygimli.meshtools as mt
import numpy as np
from typing import Any, Literal, List
from pygimli.physics.traveltime import TravelTimeManager

def create_model_and_mesh(geom: Any, quality: float = 34, area: float = 0.25) -> Any:
    mesh_fwd = mt.createMesh(geom, quality, area)
    model = np.array([2000., 2300, 1700])[mesh_fwd.cellMarkers()]
    return mesh_fwd, model

def travel_time_manager(mesh: Any, scheme: Any, model: Any, secnodes: Literal = 4, noiselevel: float = 0.001, noiseabs: float = 1e-5, seed: Literal = 1337) -> Any:
    tt = TravelTimeManager()
    data = tt.simulate(mesh=mesh, scheme=scheme, slowness=1./model,
                    secNodes=secnodes, noiseLevel=noiselevel, noiseAbs=noiseabs, seed=seed)
    return tt, data

def inversion_mesh_grid(start: float, end_x: float, end_y: float, footsteps: float, ga: List, ga1: List, sa: List, sa1: List) -> Any:
    x = np.arange(start, end_x, footsteps)
    y = np.arange(start, end_y, footsteps)
    mesh = pg.meshtools.createGrid(x, y)

    ax, _ = pg.show(mesh, hold=True)

    ax.plot(ga, ga1, "kv")
    ax.plot(sa, sa1, "ro")
    return mesh

def invert(tt: Any, data: Any, mesh: Any, secnodes: int = 3, lam: int = 1000, zweight: float = 1.0, usegradient: bool = False, verbose: bool = True) -> Any:
    tt.inv.inv.setRecalcJacobian(True)

    invmodel = tt.invert(data, mesh=mesh, secNodes=secnodes, lam=lam, zWeight=zweight,
                        useGradient=usegradient, verbose=verbose)
    print("chi^2 = %.2f" % tt.inv.chi2())
    return invmodel

def true_model_and_inversion_result(mesh_fwd: Any, model: Any, tt: Any, ga: List, ga1: List, sa: List, sa1: List) -> Any:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 7), sharex=True, sharey=True)
    ax1.set_title("Forward model and mesh")
    ax2.set_title("Inversion result - Real data")
    
    pg.show(mesh_fwd, model, ax=ax1, showMesh=True,
            label=pg.unit('vel'), cMap=pg.cmap('vel'), nLevs=3)

    for ax in (ax1, ax2):
        ax.plot(ga, ga1, "kv")
        ax.plot(sa, sa1, "ro")

    tt.showResult(ax=ax2, logScale=False, nLevs=3)
    fig.tight_layout()
    return fig, ax
    
def visualized_rays(tt: Any, ga: List, ga1: List, sa: List, sa1: List) -> Any:
    fig, ax = plt.subplots()
    tt.showCoverage(ax=ax, cMap="Blues")
    tt.drawRayPaths(ax=ax, color="y", alpha=0.3)

    ax.plot(ga, ga1, "kv")
    ax.plot(sa, sa1, "ro")
    return fig, ax
    