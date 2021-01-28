"""
This module has functions associated with analyzing the geometry of a molecule.

When run as a script and given an xyz file, this script will print out the bonds. Run

$ python geometry_analysis.py --help

to see input options.
"""

import numpy
import os

def calculate_distance(atom1_coord, atom2_coord):
    x_distance = atom1_coord[0] - atom2_coord[0]
    y_distance = atom1_coord[1] - atom2_coord[1]
    z_distance = atom1_coord[2] - atom2_coord[2]
    bond_length_12 = numpy.sqrt(x_distance**2+y_distance**2+z_distance**2)
    return bond_length_12

def bond_check(atom_distance, minimum_length=0, maximum_length=1.5):
    if atom_distance > minimum_length and atom_distance <= maximum_length:
        return True
    else:
        return False

def open_xyz(filename):
     xyz_file = numpy.genfromtxt(fname=filename, skip_header=2, dtype='unicode')
     symbols = xyz_file[:,0]
     coord = (xyz_file[:,1:])
     coord = coord.astype(numpy.float)
     return symbols, coord

file_location = os.path.join('data', 'water.xyz')
symbols, coord = open_xyz(file_location)
num_atoms = len(symbols)
for num1 in range(0,num_atoms):
     for num2 in range(0,num_atoms):
         if num1<num2:
             bond_length_12 = calculate_distance(coord[num1], coord[num2])
             if bond_check(bond_length_12) is True:
                 print(F'{symbols[num1]} to {symbols[num2]} : {bond_length_12:.3f}')
