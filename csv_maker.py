#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import numpy as np
import shutil
import time

argvs = sys.argv

if len(argvs) != 2:
    print "usage python %s <outpu_name.csv>" % argvs[0]
    exit()

local_map_infration_range_list = [6.0,7.0,8.0]
local_map_calc_method_list  = ["linear", "exp"]
fnav_dangerous_radius_list = [0.6, 0.1]
fnav_sigma_list = [1.1]
fnav_heading_list = [0.0]
fnav_distance_list = [0.75, 0.5]
fnav_time_list = [0.5, 0.75]
fnav_simulate_time_list = [1.8]
fnav_max_velocity_list = [1.1]
fnav_max_acceleration_list = [8.0]
fnav_resolution_velocity_list = [0.05]
fnav_pre_vel_weight_list = ["true"]
fnav_pre_vel_sigma_list = [0.7]
fnav_pre_vel_value_list = [100]
fnav_min_vel_value_list = [0.5]

output_np = np.array([[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]])
count = 80
for local_map_infration_range in local_map_infration_range_list:
    for local_map_calc_method in local_map_calc_method_list:
        for fnav_dangerous_radius in fnav_dangerous_radius_list:
            for fnav_sigma in fnav_sigma_list:
                for fnav_heading in fnav_heading_list:
                    for fnav_distance in fnav_distance_list:
                        for fnav_time in fnav_time_list:
                            for fnav_simulate_time in fnav_simulate_time_list:
                                for fnav_max_velocity in fnav_max_velocity_list:
                                    for fnav_max_acceleration in fnav_max_acceleration_list:
                                        for fnav_resolution_velocity in fnav_resolution_velocity_list:
                                            for fnav_pre_vel_weight in fnav_pre_vel_weight_list:
                                                for fnav_pre_vel_sigma in fnav_pre_vel_sigma_list:
                                                    for fnav_pre_vel_value in fnav_pre_vel_value_list:
                                                        for fnav_min_vel_value in fnav_min_vel_value_list:
                                                            tmp_np = np.array([[local_map_infration_range],[local_map_calc_method],[fnav_dangerous_radius],[fnav_sigma],[fnav_heading],[fnav_distance],[fnav_time],[fnav_simulate_time],[fnav_max_velocity],[fnav_max_acceleration],[fnav_resolution_velocity],[fnav_pre_vel_weight],[fnav_pre_vel_sigma],[fnav_pre_vel_value],[fnav_min_vel_value],[count]])
                                                            output_np = np.append(output_np, tmp_np, axis=1)
                                                            count += 1

np.savetxt(argvs[1], output_np, delimiter=",", fmt="%s")
# f.close()
