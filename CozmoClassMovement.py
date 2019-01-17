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
#from colors import Colors
#from woc import WOC

#import _thread
#import time

def moveInCircle(robot, speed, seconds):

	robot.say_text("I will spin in three circles").wait_for_completed()
	#robot.set_all_backpack_lights(Colors.BLUE)
	#the first value is the speed for one of the treads, and the second value
	#is the speed for the other tread (left? right?).  They can both be
	#the same sign, or have opposite signs.  the last value is the duration of the
	#movement (measured in seconds?)
	robot.drive_wheels(speed, -1 * speed, None, None, seconds)
	#robot.set_all_backpack_lights(Colors.GREEN)
	return

def turnRight(robot):
	robot.say_text("I will turn right").wait_for_completed()
	#robot.set_all_backpack_lights(Colors.RED)
	robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
	#robot.set_all_backpack_lights(Colors.GREEN)
	return

def turnLeft(robot):
	robot.say_text("I will turn left").wait_for_completed()
	#robot.set_all_backpack_lights(Colors.BLUE)
	robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
	#robot.set_all_backpack_lights(Colors.GREEN)
	return

def turnReverse(robot):
	robot.say_text("I will reverse").wait_for_completed()
	robot.turn_in_place(cozmo.util.degrees(180)).wait_for_completed()
	return

def cozmo_program(robot: cozmo.robot.Robot):
	cozmo_movement(robot, a = 0, b = 0, x = -400, y = 400)	
	return

def cozmo_movement(robot: cozmo.robot.Robot,  x, y, a = 0, b = 0, animation = "anim_petdetection_dog_03"):
	x_mag = abs(x - a)
	y_mag = abs(y - b)

	# Just go straight
	if (x-a >= 0):
		robot.say_text("I will drive forward one more time").wait_for_completed()
		robot.drive_straight(cozmo.util.distance_mm(x_mag), cozmo.util.speed_mmps(150)).wait_for_completed()
	
	# Reverse
	else:
		# Turn 180 degrees
		turnReverse(robot)

		# Then move straight
		robot.say_text("I will drive forward one more time").wait_for_completed()
		robot.drive_straight(cozmo.util.distance_mm(x_mag), cozmo.util.speed_mmps(150)).wait_for_completed()

		# turn back to positive x direction
		turnReverse(robot)
	

	if (y-b >= 0):
		# Turn in the positive y-direction
		turnLeft(robot)

		robot.say_text("I will drive forward one more time").wait_for_completed()
		robot.drive_straight(cozmo.util.distance_mm(y_mag), cozmo.util.speed_mmps(150)).wait_for_completed()

		# Turn to face position direction
		turnRight(robot)
	
	else:
		# Turn in the negative y-direction
		turnRight(robot)

		# Then move straight
		robot.say_text("I will drive forward one more time").wait_for_completed()
		robot.drive_straight(cozmo.util.distance_mm(y_mag), cozmo.util.speed_mmps(150)).wait_for_completed()

		# Turn to face position direction
		turnLeft(robot)

	robot.play_anim(name=animation).wait_for_completed()

if __name__ == '__main__':
	cozmo.run_program(cozmo_program, use_viewer=False, force_viewer_on_top=False)
