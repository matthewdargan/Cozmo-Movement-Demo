#In this sample code, you will learn how to program Cozmo to
#move forward, turn 90 degrees left or right, spin in a circle
#talk, and perform an animation


#import the cozmo and image libraries
import cozmo

#import libraries for movement 
from cozmo.util import degrees, distance_mm

#we shouldn't need anything for asynchronous behavior
#import asyncio

#import libraries for light colors.  If this library has not been
#acquired, comment out all actions involving colors
from colors import Colors
from woc import WOC

#we shouldn't need these for this demonstration
#import _thread
#import time

def moveInCircle(robot, speed, seconds):

	robot.say_text("I will spin in a circle").wait_for_completed()
	robot.set_all_backpack_lights(Colors.BLUE)
	#the first value is the speed for one of the treads, and the second value
	#is the speed for the other tread (left? right?).  They can both be
	#the same sign, or have opposite signs.  the last value is the duration of the
	#movement (measured in seconds?)
	robot.drive_wheels(speed, -1 * speed, None, None, seconds)
	robot.set_all_backpack_lights(Colors.GREEN)
	return

def turnRight(robot):
	robot.say_text("I will turn right").wait_for_completed()
	robot.set_all_backpack_lights(Colors.RED)
	robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
	robot.set_all_backpack_lights(Colors.GREEN)
	return

def turnLeft(robot):
	robot.say_text("I will turn left").wait_for_completed()
	robot.set_all_backpack_lights(Colors.BLUE)
	robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
	robot.set_all_backpack_lights(Colors.GREEN)
	return

def cozmo_program(robot: cozmo.robot.Robot):
	
	# Move lift down and tilt the head up
	robot.move_lift(-3)
	robot.set_head_angle(degrees(0)).wait_for_completed()
    
	#make an announcment and drive forward
	robot.say_text("I will drive forward").wait_for_completed()
	robot.drive_straight(cozmo.util.distance_mm(400), cozmo.util.speed_mmps(150)).wait_for_completed()
	
	#Cozmo should turn left (counter-clockwise)
	turnLeft(robot)    
	
	#make an announcment and drive forward
	robot.say_text("I will drive forward again").wait_for_completed()
	robot.drive_straight(cozmo.util.distance_mm(400), cozmo.util.speed_mmps(150)).wait_for_completed()

	#Cozmo should turn right (clockwise)
	turnRight(robot)
	
	#make an announcment and drive forward
	robot.say_text("I will drive forward one more time").wait_for_completed()
	robot.drive_straight(cozmo.util.distance_mm(400), cozmo.util.speed_mmps(150)).wait_for_completed()
	
	#make an announcment and act like a dog
	robot.say_text("I will act like a dog").wait_for_completed()
	robot.play_anim(name="anim_petdetection_dog_03").wait_for_completed()
	
	#moveInCircle(robot, speed, seconds)
	moveInCircle(robot, 200, 6)
	
	return

cozmo.run_program(cozmo_program, use_viewer=False, force_viewer_on_top=False)