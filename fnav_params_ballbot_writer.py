#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np
argvs = sys.argv
write_file = argvs[0].replace("_writer.py", ".yaml")
data = np.genfromtxt('params.csv', dtype = None, delimiter=',')
read_params = data[:,int(argvs[1])]
file = open(write_file, "w")
file.write('fnav_move_base:\n')
file.write('  frame_id_robot: "cog" # change.20180410 "base"  # string: Coordinate frame of the base footprint of the robot\n')
file.write('  use_gridmap_path_planner : false\n')
file.write('  use_trajectory_planner : false\n')
file.write('  use_motion_planner : true\n')
file.write('\n')
file.write('  costmap2d_mt:\n')
file.write('    map_width: 4.0\n')
file.write('    map_height: 4.0\n')
file.write('\n')
file.write('  gridmap_path_planner:\n')
file.write('    frame_id_global: "map"  # string: Coordinate frame on which gridmap path plans are generated\n')
file.write('    plan_frequency: 1.0  # Hz, double\n')
file.write('\n')
file.write('  localmap_path_planner:\n')
file.write('    frame_id_global: "cog" # change.20180410 "base" #"odom"  # string: Coordinate frame on which localmap path plans are generated\n')
file.write('    plan_frequency: 50.0  # Hz, double\n')
file.write('    #show_took_time : false\n')
file.write('    always_create : true\n')
file.write('\n')
file.write('  trajectory_planner:\n')
file.write('    frame_id_global: "map" # string: Coordinate frame on which trajectory plans are generated\n')
file.write('    plan_frequency: 4.0  # Hz, double\n')
file.write('    goal_radius: 0.1 # m, double: use goal judgement\n')
file.write('    engine: "fnav_fx_trajectory_planner"  # "fnav_fx_trajectory_planner", "fnav_ompl_trajectory_planner"\n')
file.write('    cost_features:\n')
file.write('      weights:  # array of double\n')
file.write('        admittance: 1.0  # zero or a positive value. If this is set to a positive value, cost for places with static obstacles is calculated as infinity.\n')
file.write('        time: 0.50  # cost/sec\n')
file.write('        distance: 0.50  # cost/m\n')
file.write('        people_proximity: 0.50\n')
file.write('      params:\n')
file.write('        people_proximity:\n')
file.write('          critical_region_prediction_time: 8.0  # s, double\n')
file.write('          critical_region_radius: 1.0 # 3.0 # 0.5  # m, double\n')
file.write('          position_probability_variance: 1.0 # 5.0 # 1.0  # m^2, double\n')
file.write('          position_probability_to_cost_factor: 1.0  # double\n')
file.write('\n')
file.write('  motion_planner:\n')
file.write('    frame_id_global: "map" # string: Coordinate frame on which localmap path plans are generated\n')
file.write('    plan_frequency: 100.0  # Hz, double\n')
file.write('    trajectory_type : trajectory_topic # goal_topic or dst_pose_topic or trajectory_topic or trajectory_planner or trajectory_fix(hard cord)\n')
file.write('    ### goal_topc : /move_base_simple/goal # hard cording in movebase.cc\n')
file.write('    dst_pose_topic : /dst_pose\n')
file.write('    trajectory_topic : /decision_maker_trajectory\n')
file.write('    trajectory_fix: # map座標系指定 index,x,y,theta(未サポート),time(sec:移動開始からの相対時間)\n')
file.write('    - {x:  9.000 , y: 2.000, theta: 0.0, time: 5.0 } # fix\n')
file.write('    - {x: 10.250 , y: 1.350 , theta: 0.0, time: 8.0 } # fix\n')
file.write('    - {x: 11.500 , y: 0.700, theta: 0.0, time: 12.0 } # fix\n')
file.write('    - {x: 14.000 , y: 2.000, theta: 0.0, time: 16.0 } # fix\n')
file.write('    - {x: 20.000 , y: 2.000, theta: 0.0, time: 35.0 } # fix\n')
file.write('\n')
file.write('    decision_maker_time_param : 2.0 # 0.2\n')
file.write('    rviz_goal_time_velocity : 1.1 # m/s : RVIZでgoal指定した時の距離に対して時間を算出する速度\n')
file.write('    publish_cmd_type : state # state or velocity\n')
file.write('    publish_cmd_topic : /cmd_state\n')
file.write('    pub_debug_topic : true\n')
file.write('\n')
file.write('    dangerous_radius : %s #1.5 #0.1 # meter # 大きすぎるとdwaの候補点が0個になってしまいうまく回避できない\n' % read_params[2])
file.write('    show_candicate_points : true # for debug\n')
file.write('\n')
file.write('    adjust_param:\n')
file.write('      goal_radius: 0.5 # m\n')
file.write('      waypoint_radius : 0.0 # m\n')
file.write('      adjust_speed_param : 0.0 # if goal distance is less than max velocity * this parameter , and slow down.\n')
file.write('      minimum_time : 0.005 # sec:dwa input time difference from waypoint(0)\n')
file.write('      prepare_time : 0.0 #1.5 #sec :\n')
file.write('      stop_turn_angular: 35.0 # (deg) ロボットの向きとWaypointの成す角がパラメータ以上だった場合には、停止して向きだけを変更する。\n')
file.write('     \n')
file.write('    dwa :\n')
file.write('      maxWz :                       0.5   # rad/s   最高角速度(yaw)\n')
file.write('      wzRes :                       0.5   # rad/ss  最高角加速度(yaw)\n')
file.write('      sigma_test : [%s,0.0,0.0,%s]      # time scoreを計算する正規分布の分散値、大きいほど障害物から離れる\n' % (read_params[3], read_params[3]))
file.write('      delta_time:                   0.1   # sec   : 軌道を予測する際の刻み幅、小さくすれば正確な予測が出来る（要デバッグ）\n')
file.write('      max_velocity:                %s    # 1.1   # m/s   :ロボット最高速度 2018/4/9 パラメータ変更\n' % read_params[8])
file.write('      max_angular_velocity:        20.0   # deg   :ロボット最高角速度\n')
file.write('      max_acceleration:            %s    #4.0   # m/ss  :ロボット最高加速度 2018/4/9 パラメータ変更\n' % read_params[9])
file.write('      max_angular_acceleration:   100.0   # deg/ss:ロボット最高角加速度、未使用\n')
file.write('      resolution_velocity:          %s  # m/s   :DW内サンプルする速度の刻み幅（小さくすれば、滑らかに動けるようになるはず）\n' % read_params[10])
file.write('      resolution_angular_velocity: 10.0   # deg/s :DW内サンプルする角速度の刻み幅（小さくすれば、滑らかに動けるようになるはず）、未使用\n')
file.write('      simulate_time:                %s   # sec   :simulate_time: 軌道を予測する時間。現状、制御器の時定数が1.2sなので、その付近に設定すべき\n' % read_params[7])
file.write('      weight :\n')
file.write('        heading:  %s   # ゴールに向く重み(time と独立ではないので、0にすべき）\n' % read_params[4])
file.write('        distance: %s   # 障害物からの距離の重み\n' % read_params[5])
file.write('        time:     %s  # 時間を守る重み\n' % read_params[6])
file.write('      map_frame_id : "map"\n')
file.write('      odom_frame_id : "odom"\n')
file.write('      base_frame_id : "cog" # change.20180410 "base"\n')
file.write('      calc_cost_step_on_traj : 0.1 # meter :軌道上のコスト計算をする際の刻み幅. 軌道の終点からこの設定値の刻み幅ごとの軌道上の点のコストを計算する.\n')
file.write('      pre_vel_weight : %s\n'  % read_params[11])
file.write('      pre_vel_sigma : [%s,0.0,0.0,%s]\n' % (read_params[12],read_params[12]))
file.write('      pre_vel_value : %s\n' % read_params[13])
file.write('      min_vel_value : %s\n' % read_params[14])
file.write('fnav_gridmap_path_planner:\n')
file.write('  distance_to_go_map_expansion_overload_amount: 5.0  # m\n')
file.write('\n')
file.write('fnav_localmap_path_planner:\n')
file.write('  distance_to_go_map_expansion_overload_amount: 5.0  # m\n')
file.write('  create_tpp_costmap : false # trajectory path planner用コストマップの生成\n')
file.write('  create_mp_costmap : true # motion_planner用コストマップの生成\n')
file.write('\n')
file.write('fnav_fx_trajectory_planner:\n')
file.write('  common:\n')
file.write('    num_time_ordered_samples: 5000  # int: This value should be less than or equal to max_num_vertices. Including the root state.\n')
file.write('    max_time_horizon: 10.0  # s, double\n')
file.write('    max_velocity: 1.0  # m/s, double\n')
file.write('    max_edge_time_length: 1.0  # s, double\n')
file.write('    goal_radius: 0.5  # m, double\n')
file.write('    cost_eval_time_resolution: 0.1  # s, double\n')
file.write('    middle_goal_distance: 8.0 # 6.0 # 4.0 # 6.0  # m, double\n')
file.write('    evaluation_distance_to_go_factor: 2.0  # double: cost(v) = cost_to_come(v) + THIS * distance_to_go(v)\n')
file.write('    progressive_replanning:\n')
file.write('      enabled: true  # bool\n')
file.write('      trajectory_expansion_scale: 0.5  # double: Edges longer than this * max_edge_time_length will be divided\n')
file.write('    nearest_neighbor_search:\n')
file.write('      num_neighbors_for_extension: 10  # int\n')
file.write('      search_radius_for_rrtstar_rewiring: 0.5  # m, double\n')
file.write('      kdtree_rebuild_threshold: 2  # int\n')
file.write('      kdtree_num_parallel_trees: 1  # int\n')
file.write('      kdtree_num_tree_checks: 32  # int\n')
file.write('\n')
file.write('  engine: "rrt_xyt"  # "rrt_xyt"\n')
file.write('  engine_params:\n')
file.write('    rrt_xyt:\n')
file.write('      rrt_algorithm: "rrtstar"  # "rrt", "rrtstar"\n')
file.write('      max_tree_generation_time: 10.0 # 2.0  # s, double\n')
file.write('      max_num_vertices: 5000  # int\n')
file.write('      max_num_child_vertices: 100  # int\n')
file.write('      enable_path_pruning: true  # bool\n')
file.write('      debug:\n')
file.write('        export_tree:\n')
file.write('          enabled: false # true\n')
file.write('          path: "~/ISP_ws/fx_rrtxyt_tree-%09d.vtk" # "/tmp/fnav/fx_rrtxyt_tree-%09d.vtk"\n')
file.write('\n')
file.write('fnav_ompl_trajectory_planner:\n')
file.write('  common:\n')
file.write('    max_time_horizon: 10.0  # s, double\n')
file.write('    max_space_horizon: 10.0  # s, double\n')
file.write('    mid_goal_distance: 6.0  # m, double\n')
file.write('    max_edge_time_length: 1.0  # s, double\n')
file.write('    max_velocity: 1.0  # m/s, double\n')
file.write('    goal_radius: 0.5  # m, double\n')
file.write('    cost_time_resolution: 0.5  # s, double\n')
file.write('\n')
file.write('  algorithm: "rrt"  # "rrt", "rrtstar"\n')
file.write('  algorithm_params:\n')
file.write('    # Note that these parameters must be specified in text strings.\n')
file.write('    # (This is due to the design of OMPL parameter interface.)\n')
file.write('    rrt:\n')
file.write('      range: "1.0"  # "double", "0.:1.:10000."\n')
file.write('      goal_bias: "0.05"  # "double", "0.:.05:1."\n')
file.write('    rrtstar:\n')
file.write('      range: "1.0"  # "double", "0.:1.:10000."\n')
file.write('      tree_pruning: "1"  # "bool", "0,1"\n')
