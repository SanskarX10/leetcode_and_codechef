"""

On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle. """


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x_dir, y_dir = 0, 1
        x, y = 0, 0

        for i in instructions:
            if i == 'G':
                x += x_dir
                y += y_dir
            elif i == 'L':
                x_dir, y_dir = -1* y_dir, x_dir
            else:
                x_dir, y_dir = y_dir, -1*x_dir

        return (x, y) == (0, 0) or (x_dir, y_dir) != (0, 1)
        
