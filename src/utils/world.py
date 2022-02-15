import pygimli.meshtools as mt
from typing import Any, List

def create_world(start: List, end: List, marker: int) -> Any:
    create = mt.createRectangle(start=start, end=end,
                            marker=marker)
    return create               
