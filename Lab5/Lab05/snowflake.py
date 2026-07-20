"""
Author: Alex Perez Perez
Last updated: July 19, 2026
Description: Draws a Koch snowflake with either recursion or an explicit
stack, and compares the runtime and memory usage of both approaches. 
"""

import turtle
import time 
from memory_profiler import memory_usage

class KochSnowflake:
    def __init__(self, init_length=500, init_depth=3):
        # Initialize the turtle
        self.t = None  

        # Length of one edge at 0 depth
        self.init_length = init_length  
        # Number of "layers" to draw
        self.init_depth = init_depth    
    

    def init_turtle(self):
        """ Initialize the turtle and move it to the 
            appropriate location on the screen """
        
        t = turtle.Turtle() # Initialize the turtle
        t.speed(8) # Increase the turtle's speed
        # Move the turtle to the upper left corner
        t.teleport(-200, -200)
        self.t = t


    ######################
    # Draw curve methods #
    ######################

    def draw_curve_recursive(self):
        """ The 'entry point' into the recursive curve method
            Draw one side of the Koch snowflake recursively. """
        self.draw_curve_recursive_helper(self.init_length, self.init_depth)


    def draw_curve_recursive_helper(self, length, depth):
        """ Recursively draw one Koch curve of the given length and depth. """

        # Raise an error if depth is negative
        if depth < 0:
            # Raise a value error with a message indicating that depth cannot be negative
            raise ValueError ("Depth cannot be negative")

                
        # Base case: at depth 0, draw one straight segment.
        elif depth == 0:
            # Draw a straigh line segment of the given length
            self.t.forward(length)
            return

        # Recursive case: replace one segment with four smaller segments.
        else:
            # Calculate the length of the smaller segments and the next depth
            smaller_length = length / 3
            next_depth = depth - 1

            # Draw the four smaller segments, turning the turtle appropriately between each segment
            self.draw_curve_recursive_helper(smaller_length, next_depth)
            self.t.right(60)

            self.draw_curve_recursive_helper(smaller_length, next_depth)
            self.t.left(120)

            self.draw_curve_recursive_helper(smaller_length, next_depth)
            self.t.right(60)

            self.draw_curve_recursive_helper(smaller_length, next_depth)


    def draw_curve_stack(self):
        """ Draw one side of the Koch snowflake using an explicit stack. """
        if self.init_depth < 0:
            # Raise a value error with a message indicating that depth cannot be negative
            raise ValueError("Depth cannot be negative")
        # initialize the stack with the initial command to draw the curve
        commands = [("add_curve", self.init_length, self.init_depth)]

        while commands:
            # pop the last command from the stack
            command = commands.pop()
            # unpack the command type and its arguments
            command_type = command[0]

            if command_type == "turn_left":
                # Turn the turtle left by the specified angle
                self.t.left(command[1])

            elif command_type == "turn_right":
                # Turn the turtle right by the specified angle
                self.t.right(command[1])

            elif command_type == "add_curve":
                # Unpack the length and deepth from the command tuple
                length = command[1]
                depth = command[2]

                if depth == 0:
                    # Base Case: at depth 0, draw one straight segment.
                    self.t.forward(length)
                else:
                    # Calculate the lengthf of the smalller segments and the next depth
                    smaller_length = length / 3
                    next_depth = depth - 1

                    # Push in reverse execution order because the stack is LIFO.
                    commands.append(("add_curve", smaller_length, next_depth))
                    commands.append(("turn_right", 60))
                    commands.append(("add_curve", smaller_length, next_depth))
                    commands.append(("turn_left", 120))
                    commands.append(("add_curve", smaller_length, next_depth))
                    commands.append(("turn_right", 60))
                    commands.append(("add_curve", smaller_length, next_depth))

            else:
                # Raise an error if the command type is unknown 
                raise ValueError(f"Unknown command: {command_type}")



    ##########################
    # Draw snowflake methods #
    ##########################

    def draw_snowflake_recursive(self):
        """ Draw the three edges of the Koch snowflake using the 
            recursive curve method """
        # Initialize the turtle and move it to the appropriate location on the screen
        self.init_turtle()
        # Draw the three edges of the Koch snowfalke
        for _ in range(3):
            self.draw_curve_recursive()
            self.t.left(120)
            
        turtle.clearscreen()


    def draw_snowflake_stack(self):
        """ Draw the three edges of the Koch snowflake using the 
            non-recursive curve method """

        self.init_turtle()
        # Draw the three edges of the Koch snowflake
        for _ in range(3):
            self.draw_curve_stack()
            self.t.left(120)

        turtle.clearscreen()


    #########################@#
    # Compare the approaches! #
    ##########################@

    def compare_snowflake(self):
        """ Compare how much time and memory the recursive and non-recursive 
            implementations of drawing the Koch Snowflake used """
        
        rec_time, rec_mem = self.get_time_and_mem(self.draw_snowflake_recursive)
        nonrec_time, nonrec_mem = self.get_time_and_mem(self.draw_snowflake_stack)

        print(f"Recursive memory usage: {rec_mem} MB")
        print(f"Non-recursive memory usage: {nonrec_mem} MB")
        print()
        print(f"Recursive time taken: {rec_time:.5f} s")
        print(f"Non-recursive time taken: {nonrec_time:.5f} s")
        

    def get_time_and_mem(self, func):
        """ Find the time and memory used by the given function """

        # Start the timer
        time_start = time.perf_counter()
        # Run the function and find the memory used
        mem_usage = memory_usage((func, ), include_children=True, multiprocess=True)
        # End the timer
        time_end = time.perf_counter()

        # Find the total time taken
        time_taken = time_end - time_start 
        # Find the total memory used
        mem_used = max(mem_usage) - min(mem_usage)

        return time_taken, mem_used


if __name__ == "__main__":
     # Change the second value to 0, 1, 2, 3, and so on to test depths.
    s = KochSnowflake(500, 0)
    # Run one of these at a time:
    s.draw_snowflake_stack()
    # s.draw_snowflake_stack()
    # s.compare_snowflake()

