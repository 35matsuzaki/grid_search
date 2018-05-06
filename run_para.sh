#!/bin/bash

PROGNAME=$(basename $0)

usage() {
    echo "Usage :$PROGNAME [-sim][-ssd][-dm][-pause][-rec][-debug_dwa][-h] (world name)"
    echo "Default:"
    echo "(world name)=default.world"
    echo
    echo "Options:"
    echo "  -sim        :use object_detector and decision maker on this machine."
    echo "  -ssd        :use object_detector "
    echo "  -dm         :use decision maker"
    echo "  -pause      :gazebo simulation pause when start"
    echo "  -rec        :learning mode.(not use object_detector and decision maker)"
    echo "  -dwa_debug  :use dwa_debug_tool"
    echo "  -h:help"
    echo "  (world name):Gazebo world file."
    echo
    exit 1
}
declare -i argc=0
declare -a argv=()

world_name="default.world"

rec_param_name="record_learning_data.yaml"
use_ssd=false
use_decision_maker=false
pause_start=false
use_record=false
use_dwa_debug=false

while (( $# > 0 ))
do
    case "$1" in
        -*)
            if [[ "$1" =~ 'h' ]]; then
                usage
            fi
            if [[ "$1" =~ 'ssd' ]]; then
                use_ssd=true
            fi
            if [[ "$1" =~ 'dm' ]]; then
                use_decision_maker=true
            fi
            if [[ "$1" =~ 'sim' ]]; then
                use_ssd=true
                use_decision_maker=true
            fi
            if [[ "$1" =~ 'rec' ]]; then
                use_record=true
                use_ssd=false
                use_decision_maker=false
            fi
            if [[ "$1" =~ 'pause' ]]; then
                pause_start=true
            fi
            if [[ "$1" =~ 'dwa_debug' ]]; then
                use_dwa_debug=true
            fi
            shift
            ;;
        *.csv)
        csv_name="$1"
        shift
        ;;

        *)
            ((++argc))
	    world_name="$1"
	    rec_param_name="$1.yaml"
            shift
            ;;
    esac

    if [ $argc -gt 1 ]; then
	usage
	exit
    fi
done

echo "=====node====="
if $use_ssd;then
    echo "Use object_detector_node"
fi
if $use_decision_maker;then
    echo "Use decision_maker_node"
fi
if $pause_start;then
    echo "GAZEBO start and simulation pause."
else
    echo "GAZEBO start and simulation auto start."
fi
if $use_record;then
    echo "Record learning data and Use auto waypoint publish."
fi
if $use_dwa_debug;then
    echo "Use DWA debug tool."
fi

echo
echo "=====parameter====="
if $use_record;then
    echo "Use record_learning_node param=$rec_param_name"
fi
echo "Use GAZEBO world = ${world_name}"
echo "=================="
echo

# array of process ID
pids=()

source ./devel/setup.bash

echo "------>start roscore"
{
  roscore
} &
pids[$!]=$!

sleep 5
echo "------>started roscore"

#######roscore sim_time=trueセット########
rosparam set /use_sim_time true

echo "------>start gazebo"
{
  echo $world_name
  roslaunch ballbot_env gazebo_case.launch paused:=${pause_start} case:=$world_name
} &
pids[$!]=$!
echo "------>started gazebo"

sleep 5

echo "------>start gazebo controller"
{
  rosrun hgx_bip_gazebo bip_gazebo_controller
} &
pids[$!]=$!
echo "------>started gazebo controller"

echo "------>start movebase"
{
  roslaunch ballbot_env movebase_ballbot.launch
} &
pids[$!]=$!
echo "------>started movebase"

echo "------>start amcl"
{
  roslaunch ballbot_env amcl_ballbot.launch
} &
pids[$!]=$!
echo "------>started amcl"

echo "------>start rviz"
{
  rviz
} &
pids[$!]=$!

echo "------>started rviz"


if $use_dwa_debug; then
    echo "------>start dwa_debug_tool"
    {
	python ./src/fnav_stack/dwa_debug_tools/scripts/dwa_debug.py
    } &
    pids[$!]=$!
    echo "------>started dwa_debug_tool"
fi

if $use_record; then
    echo "------>start record_learning_data node"
    {
	roslaunch ballbot_env record_learning_data.launch param:=$rec_param_name
    } &
    pids[$!]=$!
    echo "------>started record_learning_data node"
fi

if $use_ssd; then
    echo "------>start object_detector node"
    {
	roslaunch ballbot_env object_detect.launch
    } &
    pids[$!]=$!
    echo "------>started object_detector node"
fi

if $use_decision_maker; then
    echo "------>start decision_maker node"
    {
	roslaunch ballbot_env decision_maker.launch
    } &
    pids[$!]=$!
    echo "------>started decision_maker node"
fi

echo "------>start trajectory sender"
{
  roslaunch trajectory_sender trajectory_sender.launch
} &
pids[$!]=$!
echo "------>started trajectory sender"

sleep 5
echo "------>unpause"
rosservice call gazebo/unpause_physics

echo "------>start gazebo collision checker"
{
  rosrun gazebo_collision_check gazebo_collision_check.py $csv_name
} &
pids[$!]=$!
echo "------>started trajectory sender"



#################################################################
# echo "process list:"
# echo ${pids[@]}
#
# echo "Please push 'Enter' if want to end process."
# read key
#
# for pid in ${pids[@]}
# do
#   echo "kill ${pid}"
#   kill -9 ${pid}
# done
#
# killall roscore
# killall roslaunch
#
# ./killProc.sh
