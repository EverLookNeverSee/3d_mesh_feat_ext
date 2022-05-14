"""
    .off file to numpy array convertor
    @author: Milad Sadeghi DM - EverLookNeverSee@GitHub
"""


import igl
import numpy as np
from os import walk
from typing import Generator
from os.path import abspath, join


def mesh_loader(path: str) -> Generator:
    """
    List and load all mesh files(.off) in given directory with valid extension
    :param path: Path to the directory
    :return: Yields loaded mesh files
    """
    path = abspath(path)
    mesh_pool = list()
    valid_file_extension = "off"
    for root, dirs, files in walk(path):
        for file in files:
            if file.split(".")[-1] in valid_file_extension:
                mesh_pool.append(join(root, file))
    for mesh in mesh_pool:
        v, f = igl.read_triangle_mesh(mesh, dtypef=float)
        yield v, f
