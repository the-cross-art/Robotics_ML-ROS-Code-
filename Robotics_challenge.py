#!/usr/bin/env python
# Popular Robotics Wheeled Robot Motion Control Challenge Program Template for Use with Simulation
# Last edited by Sotirios Stasinopoulos on Jan.16,2020

"""
# Copyright
#   All rights reserved. No part of this script may be reproduced, distributed, or transmitted in any
#   form or by any means, including photocopying, recording, or other electronic or mechanical methods,
#   without prior written permission from Popular Robotics, except in the case of brief quotations embodied
#   in critical reviews and certain other noncommercial uses permitted by copyright law.
#   For permission requests, contact Popular Robotics directly.
"""

# The below commands imports other python files (modules) to be used in this script.
import simulation as sim
import time
import sys
import cv2
import rospy
import numpy
import rospkg
import os

# ----- example functions below -----

def test_wheel_motors():
    # test to see if wheel motors function properly
    sim.go_forward(50, 0.5)  # arguments: speed (between 0 and 100), duration (seconds)
    sim.stop_moving_for(.2)  # argument: duration (seconds)
    sim.go_backward(50, 0.3)
    sim.stop_moving_for(.2)
    sim.spin_left(50, 1)
    sim.stop_moving_for(.2)
    sim.spin_right(50, 1)
    sim.stop_moving_for(0)

# ----- example functions above -----


# ***** student edits start *****
# students define their own functions here.

def student_function():
    sim.initialize_simulation()
    test_wheel_motors()
    # Replace 'pass' with your own code to get the robot moving ;)
    sim.go_forward(50,0.06)
    sim.stop_moving_for(0.2)
    sim.spin_left(50,1)
    sim.go_forward(50,0.02)
    sim.stop_moving_for(0.2)
    sim.spin_right(50,2)
    sim.go_forward(50,0.06)
    sim.stop_moving_for(0.2)
    sim.spin_left(50,2)
    sim.go_forward(50,0.06)
    sim.stop_moving_for(0.2)
    sim.spin_right(50,2)
    sim.go_forward(50,0.06)
    sim.stop_moving_for(0.2)
    sim.spin_left(50,2)
    sim.go_forward(50,0.06)
    sim.stop_moving_for(0.2)
    sim.spin_right(50,2)

    
# ***** student edits end *****


# ----- main function below -----

if __name__ == "__main__":
    if not rospy.is_shutdown():
        student_function()

# ----- main function above -----
