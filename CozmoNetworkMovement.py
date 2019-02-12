#!/usr/bin/env python3

# Copyright (c) 2016 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''Hello World
Make Cozmo communicate with other Cozmo robots
'''

import cozmo
import socket
import errno
from socket import error as socket_error

# need to get movement info
from cozmo.util import degrees, distance_mm, speed_mmps


def cozmo_program(robot: cozmo.robot.Robot):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket_error as msg:
        robot.say_text("socket failed" + msg).wait_for_completed()

    ip = "10.0.1.10"
    port = 5000
    
    try:
        s.connect((ip, port))
    except socket_error as msg:
        robot.say_text("socket failed to bind").wait_for_completed()

    cont = True
    robot.say_text("ready").wait_for_completed()    
    
    # SET COZMO's NAME
    myName = 'CozmoName'
    while cont:
        bytedata = s.recv(4048)
        #data = str(bytedata)
        data = bytedata.decode('utf-8')

        if not data:
            cont = False
            s.close()
            quit()
        else:
            #---------------------------------------------------------
            #This is where you need to adjust the program
            #---------------------------------------------------------
            print(data)
            instructions = data.split(';')

            # check the name:
            if instructions[0] == myName:
                if len(instructions) == 5:
                    # we know that this is a message involving movement
                    instructions[3] = int(instructions[3])
                    instructions[4] = int(instructions[4])

                    # next, we will want to move forward or backward, if the x distance is not 0
                    # first, just move if 'F' and turn 180 degrees for 'B'
                    # then, we will want to turn left or right, if the y distance is not 0
                    print(instructions)

                    if instructions[3] is not 0:
                        # just move forward
                        if instructions[1] == 'F':
                            robot.drive_straight(cozmo.util.distance_mm(instructions[3]), cozmo.util.speed_mmps(150)).wait_for_completed()

                            if instructions[4] is not 0:
                                # now handle left or right distance
                                if instructions[2] == 'L':
                                    robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                                    robot.drive_straight(cozmo.util.distance_mm(instructions[4]), cozmo.util.speed_mmps(150)).wait_for_completed()
                                else:
                                    robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                                    robot.drive_straight(cozmo.util.distance_mm(instructions[4]), cozmo.util.speed_mmps(150)).wait_for_completed()

                        # reverse and then move forward
                        else:
                            robot.turn_in_place(cozmo.util.degrees(180)).wait_for_completed()
                            robot.drive_straight(cozmo.util.distance_mm(instructions[3]), cozmo.util.speed_mmps(150)).wait_for_completed()

                            if instructions[4] is not 0:
                                # now handle left or right distance
                                if instructions[2] == 'L':
                                    robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
                                    robot.drive_straight(cozmo.util.distance_mm(instructions[4]), cozmo.util.speed_mmps(150)).wait_for_completed()
                                else:
                                    robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
                                    robot.drive_straight(cozmo.util.distance_mm(instructions[4]), cozmo.util.speed_mmps(150)).wait_for_completed()

                    robot.say_text(instructions[0]).wait_for_completed()
                elif len(instructions) == 3:
                    # this is where we move the tractor or the head
                    # if the first value is greater than 0, move the head
                    # if the second value is greater than 0, move the tractor arm
                    instructions[1] = int(instructions[1])
                    instructions[2] = int(instructions[2])
                    print(instructions)

                    # change head angle
                    if instructions[1] > 0:
                        robot.set_head_angle(instructions[1])

                    # change tractor arm angle
                    if instructions[2] > 0:
                        robot.set_lift_height(instructions[2])
                
                s.sendall(b"Done")
                s.close()
                quit()

cozmo.run_program(cozmo_program)