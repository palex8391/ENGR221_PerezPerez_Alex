""" 
Author: Alex Perez Perez
Last updated: July 26, 2026
Description: Imports engineering faculty information, stores it in a hash map, 
builds the School of Engineering tree, and starts the visualizer. """

import pandas as pd

from professor import Professor
from faculty_visualizer import FacultyVisualizer
from tree_node import TreeNode
from preferences import Preferences

class ENGR_Faculty:
    # Create the faculty database, build the tree structure, and prepare the visualizer.
    def __init__(self):

        # Store all faculty members in a dictionary keyed by last name.
        # Each value is a Professor object containing the person's details.
        self.faculty_dict = self.import_faculty()

        # Build the school-program-faculty tree from the imported data.
        self.program_structure = self.build_structure()

        # Create the visualizer so the tree can be displayed on screen.
        self.visualizer = FacultyVisualizer(
            self.program_structure, self.faculty_dict)

        
    def import_faculty(self):
        """Read the Excel file, create Professor objects, and store them in a dictionary."""

        # Create an empty dictionary to hold all faculty members.
        faculty_dict = {}

        # Read the spreadsheet into a table so each row can be processed.
        df = pd.read_excel(Preferences.FACULTY_FILE)

        # Process each row of the spreadsheet and add the professor to the dictionary.
        df.apply((lambda x: self.add_prof(x, faculty_dict)), axis=1)

        return faculty_dict


    def add_prof(self, prof, faculty_dict) -> None:
        """Create a Professor object from one spreadsheet row and store it in the dictionary."""
        professor = Professor(
            prof["FirstName"],  # First name from the spreadsheet.
            prof["LastName"],   # Last name from the spreadsheet.
            prof["Rank"],        # Academic rank from the spreadsheet.
            prof["Program"],     # Program affiliation from the spreadsheet.
            prof["Office"],      # Office location from the spreadsheet.
        )

        # Use the professor's last name as the dictionary key.
        faculty_dict[professor.last_name] = professor


    def build_structure(self) -> TreeNode:
        """Build and return the school-program-faculty tree."""

        # Create the root node for the School of Engineering.
        root = TreeNode("School of Engineering", TreeNode.NodeType.SCHOOL)

        # Keep a mapping from each program enum value to its tree node.
        program_nodes = {}

        # Create one child node for every program in the engineering school.
        for program in Professor.Program:
            program_node = TreeNode(
                program.value,  # The visible name of the program.
                TreeNode.NodeType.PROGAM,
            )
            root.add_child(program_node)  # Attach the program node under the school root.
            program_nodes[program] = program_node  # Save it for later use.

        # Add each professor as a child of their matching program node.
        for professor in self.faculty_dict.values():
            faculty_node = TreeNode(
                professor.last_name,  # Show the professor's last name in the tree.
                TreeNode.NodeType.FACULTY,
                professor,  # Store the Professor object as node data.
            )
            program_nodes[professor.program].add_child(faculty_node)

        return root


    def visualize_faculty(self):
        """Run the visualizer to display the faculty tree."""
        self.visualizer.run()


if __name__ == '__main__':
    # Create the faculty manager and display the faculty tree.
    f = ENGR_Faculty()
    f.visualize_faculty()