from CozmoClassMovement import turnLeft, turnRight
import cozmo
from cozmo.util import degrees, distance_mm

# Used for testing the cozmo_navigator function
def cozmo_program(robot: cozmo.robot.Robot):
    cozmo_navigator(robot, instructions=[580, "left", 600, "right", 1080, "left", 600])
    return

def cozmo_navigator(robot: cozmo.robot.Robot, instructions):
    """Move cozmo through a maze by using a list to tell it how far or which direction to turn in.
    One unit in any given direction is defined as one centimeter.

	Keyword arguments:
	robot -- the cozmo robot object
	instructions -- a list of distances or turns that should be made
                    to navigate the maze
	"""

    # iterate through the instructions passed in to navigate the maze
    for instruction in instructions:

        # check if the instruction is an integer/distance to move
        if isinstance(instruction, int):
            robot.say_text("I will drive forward").wait_for_completed()
            robot.drive_straight(cozmo.util.distance_mm(instruction), cozmo.util.speed_mmps(300)).wait_for_completed()

        # otherwise we should turn either left or right
        else:
            if instruction == "left":
                turnLeft(robot)
            else:
                turnRight(robot)

if __name__ == '__main__':
	cozmo.run_program(cozmo_program, use_viewer=False, force_viewer_on_top=False)
