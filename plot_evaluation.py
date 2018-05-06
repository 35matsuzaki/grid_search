#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import numpy as np
import shutil
import time

argvs = sys.argv
if len(argvs) != 4:
    print "usage python %s <params.csv> <result.csv> <output.csv>" % argvs[0]
    exit()

def readCsv(filename,colnum):
    data = np.loadtxt(filename, delimiter=',', dtype = str)
    return data
    # return data[:,colnum].astype(np.float)

def save_result(filename, data):
    f = open(filename, 'w')
    for key, value in data:
        print key, ":", value
        f.write(key+ "," + str(value) + "\n")
    f.close()
    print "Save Result"


if __name__ == "__main__":
    params_csv = argvs[1]
    result_csv = argvs[2]
    params_data = readCsv(params_csv, 1)
    result_data = readCsv(result_csv, 1)
    # print params_data[1,:]

    output_np = np.array([[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]])
    for i in range(params_data.shape[1]):

        local_map_infration_range_flag=local_map_calc_method_flag=fnav_dangerous_radius_flag=fnav_sigma_flag=fnav_heading_flag=fnav_distance_flag=fnav_time_flag=fnav_simulate_time_flag=fnav_max_velocity_flag=fnav_max_acceleration_flag=fnav_resolution_velocity_flag=fnav_pre_vel_weight_flag=fnav_pre_vel_sigma_flag=fnav_pre_vel_value_flag=fnav_min_vel_value_flag = True

        local_map_infration_range = None
        local_map_calc_method = "exp"
        fnav_dangerous_radius = None
        fnav_sigma = None
        fnav_heading = None
        fnav_distance = None
        fnav_time = None
        fnav_simulate_time = None
        fnav_max_velocity = None
        fnav_max_acceleration = None
        fnav_resolution_velocity = None
        fnav_pre_vel_weight = "false"
        fnav_pre_vel_sigma = None
        fnav_pre_vel_value = None
        fnav_min_vel_value = 0.0

        if local_map_infration_range != None:
            if local_map_infration_range != float(params_data[0,i]):
                local_map_infration_range_flag = False
        if local_map_calc_method != None:
            if local_map_calc_method != params_data[1,i]:
                local_map_calc_method_flag = False
        if fnav_dangerous_radius != None:
            if fnav_dangerous_radius != float(params_data[2,i]):
                fnav_dangerous_radius_flag = False
        if fnav_sigma != None:
            if fnav_sigma != float(params_data[3,i]):
                fnav_sigma_flag = False
        if fnav_heading != None:
            if fnav_heading != float(params_data[4,i]):
                fnav_heading_flag = False
        if fnav_distance != None:
            if fnav_distance != float(params_data[5,i]):
                fnav_distance_flag = False
        if fnav_time != None:
            if fnav_time != float(params_data[6,i]):
                fnav_time_flag = False
        if fnav_simulate_time != None:
            if fnav_simulate_time != float(params_data[7,i]):
                fnav_simulate_time_flag = False
        if fnav_max_velocity != None:
            if fnav_max_velocity != float(params_data[8,i]):
                fnav_max_velocity_flag = False
        if fnav_max_acceleration != None:
            if fnav_max_acceleration != float(params_data[9,i]):
                fnav_max_acceleration_flag = False
        if fnav_resolution_velocity != None:
            if fnav_resolution_velocity != float(params_data[10,i]):
                fnav_resolution_velocity_flag = False
        if fnav_pre_vel_weight != None:
            if fnav_pre_vel_weight != params_data[11,i]:
                fnav_pre_vel_weight_flag = False
        if fnav_pre_vel_sigma != None:
            if fnav_pre_vel_sigma != float(params_data[12,i]):
                fnav_pre_vel_sigma_flag = False
        if fnav_pre_vel_value != None:
            if fnav_pre_vel_value != float(params_data[13,i]):
                fnav_pre_vel_value_flag = False
        if fnav_min_vel_value != None:
            if fnav_min_vel_value != float(params_data[14,i]):
                fnav_min_vel_value_flag = False

        output_flag = local_map_infration_range_flag and local_map_calc_method_flag and fnav_dangerous_radius_flag and fnav_sigma_flag and fnav_heading_flag and fnav_distance_flag and fnav_time_flag and fnav_simulate_time_flag and fnav_max_velocity_flag and fnav_max_acceleration_flag and fnav_resolution_velocity_flag and fnav_pre_vel_weight_flag and fnav_pre_vel_sigma_flag and fnav_pre_vel_value_flag and fnav_min_vel_value_flag

        if output_flag:
            num_index =  params_data.shape[0]-1

            result_index = np.where(result_data[:,0] == params_data[num_index,i].split(".")[0])[0]

            result = result_data[result_index,1]
            result_params_data = np.append(params_data[:,i],result)

            tmp_np = np.reshape(result_params_data,( result_params_data.shape[0],1))

            output_np = np.append(output_np, tmp_np, axis=1)

    np.savetxt(argvs[3], output_np, delimiter=",", fmt="%s")
