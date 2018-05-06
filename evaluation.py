#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import numpy as np
import shutil
import time

argvs = sys.argv
if len(argvs) != 3:
    print "usage python %s <target dir> <result.csv>" % argvs[0]
    exit()

def readCsv(filename):
    data = np.loadtxt(filename, delimiter=',', dtype = str)
    return data[:,1].astype(np.float)

def save_result(filename, data):
    f = open(filename, 'w')
    for key, value in data:
        print key, ":", value
        f.write(key+ "," + str(value) + "\n")
    f.close()
    print "Save Result"


if __name__ == "__main__":

    #結果保存用辞書{"パラメータ番号":world毎の最小値}
    result = {}
    #.worldのディレクトリごとに
    for param_key in os.listdir(argvs[1]):
        #パラメータの結果ごとに
        param_path = argvs[1] + "/" + param_key
        for world_dir in os.listdir(param_path):
            world_path = param_path + "/" + world_dir
            file_path = world_path + "/" + "result.csv"
            data = readCsv(file_path)

            #評価値として人に最も近づいた時の距離を使う
            score1 = np.array(np.min(data))

            #result辞書に格納
            if param_key in result:
                tmp_scores = np.append(result[param_key],score1)
                result.update({param_key:tmp_scores})
            else:
                result.update({param_key:score1})

    #パラメータ毎に、全ワールドでの実行結果から最も近づいた距離を求める
    for key,value in result.items():
        result.update({key:np.min(value)})

    #降順で並び替える
    sorted_result = sorted(result.items(), key=lambda x: -x[1])
    #結果をファイル出力
    save_result(argvs[2], sorted_result)
