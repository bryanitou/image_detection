# Screen username
uname="detection_action-$1"
mission_log="/home/pi/mission_log_${uname}.log"

# Launch python command
python3 detection_action_test.py | tee "${mission_log}"