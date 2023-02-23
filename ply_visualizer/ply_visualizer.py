import glob, os
import numpy as np
import pptk, plyfile

path="D:\Gavin\Documents\School\Clinic - LIDAR\ROLN\ply_visualizer\clouds"
clouds = glob.glob(path + "\*.ply")
wheresMyCloud = max(clouds, key=os.path.getctime)
youngCloud = plyfile.PlyData.read(wheresMyCloud)['vertex']

xyz = np.c_[youngCloud['x'], youngCloud['z'], youngCloud['y']]
rgb = np.c_[youngCloud['red'], youngCloud['green'], youngCloud['blue']]

v = pptk.viewer(xyz)
v.attributes(rgb / 255)
v.set(lookat=(1,1,1)) # this functionality is bugged -- as soon as you touch the window it resets the viewpoint to 0,0,0