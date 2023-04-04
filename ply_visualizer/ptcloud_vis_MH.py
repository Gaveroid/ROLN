import glob, os
import numpy as np
import pptk, plyfile

# path="D:\Gavin\Documents\School\Clinic - LIDAR\ROLN\ply_visualizer\clouds"
# path="C:\Users\meh37\Desktop\Clinic_S23\ptcloud_head.ply"
path="ptcloud_head.ply"
youngCloud = plyfile.PlyData.read(path)['vertex']

xyz = np.c_[youngCloud['x'], youngCloud['z'], youngCloud['y']]
rgb = np.c_[youngCloud['red'], youngCloud['green'], youngCloud['blue']]

v = pptk.viewer(xyz)
v.attributes(rgb / 255)
v.set(lookat=(0.358,-0.658,-0.459)) # Zoom in for better head view
input("Press enter to continue...")
newCloud = v.get('selected')        # Can pass as an input to index parameter of xyz and rgb array
v.close()                           

selectedV = pptk.viewer(xyz[newCloud])
selectedV.attributes(rgb[newCloud] / 255)
selectedV.set(lookat=(0.344,-0.640,-0.400)) # Zoom in/out before clicking to move view

# input("Press enter to reset the view...")
# selectedV.set(lookat=(0.344,-0.640,-0.400))