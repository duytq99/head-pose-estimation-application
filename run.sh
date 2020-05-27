#! /bin/bash
clear
echo "Hello!"
echo "We are TEAM ELECTRIC"
echo "This is Evaluation System of Student's Concentration"
echo "Wait 10s to initalize our system"
sleep 2

python3 data_gen.py &
python3 test_plot_animate.py &