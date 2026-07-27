# ENGR 221 - Homework 6

# Author

Alex Perez Perez

ENGR 221

Homework 6 – Hash Maps & Trees
## Hash Maps & Trees

### Overview
This assignment introduces the use of **trees** and **hash maps (dictionaries)** in Python. The project builds an Engineering Faculty Roster that organizes professors into a tree based on their engineering program while also allowing efficient faculty lookup using a dictionary.

The program displays a visual representation of the School of Engineering using Pygame and allows the user to search for professors by their last name.

---

## Files

### engr_faculty.py
- Main program for the Engineering Faculty Roster.
- Imports professor information from an Excel spreadsheet.
- Creates Professor objects.
- Stores professors in a dictionary for fast lookup.
- Builds the engineering tree structure.
- Starts the graphical visualization.

---

### tree_node.py
- Defines the TreeNode class.
- Represents each node in the engineering tree.
- Implements tree operations including:
  - add_child()
  - remove_child()
  - is_leaf()
  - depth()
  - height()
  - find()
- Maintains parent-child relationships.

---

### faculty_visualizer.py
- Displays the engineering tree using Pygame.
- Draws nodes and edges.
- Displays professor headshots.
- Handles keyboard input.
- Searches for professors using the faculty dictionary.
- Displays professor information when a valid last name is entered.

---

### professor.py
- Defines the Professor class.
- Stores information for each professor including:
  - First name
  - Last name
  - Rank
  - Program
  - Office
- Stores the path to each professor's headshot image.

---

### preferences.py
- Stores constant values used throughout the project.
- Includes:
  - Screen size
  - Fonts
  - Colors
  - Image sizes
  - File locations
  - Timing settings

---

### answers.txt
Contains written responses for:
- Part 2
- Part 3
- Part 4

---

## Data Structures Used

### Dictionary (Hash Map)
- Stores all professors.
- Key = Professor's last name.
- Value = Professor object.
- Allows fast O(1) average lookup.

### Tree
Represents the engineering department hierarchy.

Example:

School of Engineering
- Electrical
- Computer
- Civil
- Mechanical

Each program contains its faculty members.

---

## How to Run

1. Open the project folder in VS Code.
2. Install the required libraries:

```bash
pip install pandas openpyxl pygame-ce
```

3. Run the program:

```bash
py engr_faculty.py
```

---

## Testing

Run the TreeNode tests:

```bash
pytest -v tests/tree_node_tests.py
```

All tests should pass before submitting.

---

## Concepts Learned

- Trees
- Parent and child nodes
- Leaf nodes
- Tree traversal
- Tree height and depth
- Dictionaries (Hash Maps)
- Object-Oriented Programming
- Pygame graphics
- Reading Excel files with pandas
- Searching data efficiently

---

