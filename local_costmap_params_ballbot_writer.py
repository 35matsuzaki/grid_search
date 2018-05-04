#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np
argvs = sys.argv
write_file = argvs[0].replace("_writer.py", ".yaml")
data = np.genfromtxt('params.csv', dtype = None, delimiter=',')
read_params = data[:,int(argvs[1])]
file = open(write_file, "w")
file.write('local_costmap:\n')
file.write('   global_frame: odom\n')
file.write('   robot_base_frame: cog #base change.20180410\n')
file.write('   update_frequency: 10.0 # 1.0 # hz=frame/sec\n')
file.write('   publish_frequency: 0.01 # 0.5 # sec/frame\n')
file.write('   static_map: true\n')
file.write('   transform_tolerance: 1.0\n')
file.write('   person_range : 0.5 # m\n')
file.write('   rolling_window : true\n')
file.write('   plugins :\n')
file.write('#  - {name: static_layer,            type: "costmap_2d_mt::StaticLayer"}\n')
file.write('   - {name: obstacle_layer,            type: "costmap_2d_mt::ObstacleLayer"}\n')
file.write('#  - {name: inflation_layer,         type: "costmap_2d_mt::InflationLayer"}\n')
file.write('   dwa :\n')
file.write('    map_range : 4.0 # m map_height = map_width = this parameter.\n')
file.write('    map_resolution : 0.1 # m/cell\n')
file.write('    map_range_to_remove_robot : 0.3 # m Observation is regarded as robot if norm(robot - observation) < this parameter.\n')
file.write('    map_inflation_range : %s # m This is radius.\n' % read_params[0])
file.write('    map_calc_method: %s # possible method:"linear" or "exp" or "square"\n' % read_params[1])
file.write('    fill_map_with_zero: false # for debug\n')
file.write('   scan:\n')
file.write('    topic: /scan # /laser_scan change.20180410\n')
file.write('    min_obstacle_height: 0.05\n')
file.write('    max_obstacle_height: 1.8\n')
file.write('    obstacle_range: 8.0\n')
