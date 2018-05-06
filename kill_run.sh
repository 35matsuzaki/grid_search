#!/bin/bash

pgrep -f gazebo_collision_check |xargs kill
pgrep -f bip_gazebo_controller |xargs kill -9
pgrep -f rviz |xargs kill -9
pgrep -f ros |xargs kill -9
