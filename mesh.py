#convert the .ply file to .obj file

import numpy as np
import open3d as o3d
import os
import sys
import argparse

#take input file by button selection of tkinter file
parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, default='results/aligned/pcd/test_pairs/BJ721E05W-J11@9=person.ply', help='input file')
parser.add_argument('--output', type=str, default='output.obj', help='output file')
opt = parser.parse_args()

#read the input file
mesh = o3d.io.read_triangle_mesh(opt.input)

#write the output file
o3d.io.write_triangle_mesh(opt.output, mesh)
