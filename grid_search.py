#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import numpy as np
import shutil
import time

#ballbot_envのパスを指定
ballbot_env_path = "/home/s_matsuzaki/20180412_ISP/path_generation_ballbot-master/src/ballbot_env/param/"
ros_ws_path ="/home/s_matsuzaki/20180412_ISP/path_generation_ballbot-master/"

#パラメータをいじるファイルを指定
fnav_file_name = "fnav_params_ballbot.yaml"
local_file_name = "local_costmap_params_ballbot.yaml"

argvs = sys.argv
if len(argvs) != 2:
    print "usage python %s <output_dir> " % argvs[0]
    exit()

#バッグアップ、結果をまとめるディレクトリを作成
if os.path.exists(argvs[1]):
    print "usage output dir already exits"
    exit()
os.mkdir(argvs[1])

#main ループ
#csvの各列に記載してあるパラメータごとに処理
for i in range(0,80):
    #パラメータごとにバックアップ、結果をまとめるディレクトリ作成
    output_dir = argvs[1]+"/"+str(i)
    os.mkdir(output_dir)

    #パラメータを読み込んで、yamlファイルを作成
    fnav_cmd = "python fnav_params_ballbot_writer.py " + str(i)
    local_cmd = "python local_costmap_params_ballbot_writer.py " + str(i)
    os.system(fnav_cmd)
    os.system(local_cmd)

    #ballbot_envにあるyamlを削除する
    os.remove(ballbot_env_path+fnav_file_name)
    os.remove(ballbot_env_path+local_file_name)
    #ballbot_envとバックアップディレクトリに作成したyamlファイルをコピーする
    shutil.copy2(fnav_file_name, ballbot_env_path)
    shutil.copy2(fnav_file_name, output_dir)
    shutil.copy2(local_file_name, ballbot_env_path)
    shutil.copy2(local_file_name, output_dir)

    #ros環境作る
    source_cmd = "source " + ros_ws_path + "devel/setup.bash"
    os.system(source_cmd)

    #worldごとに./run_para.shを実行
    result_csv =output_dir + "/result.csv"
    world_name = "/case/case0010.world"
    run_cmd = ros_ws_path + "run_para.sh -pause " + result_csv + " " + world_name
    os.system(run_cmd)

    #良きタイミング待つ
    time.sleep(22)

    #終了する
    kill_cmd = ros_ws_path + "kill_run.sh"
    os.system(kill_cmd)
    time.sleep(3)
