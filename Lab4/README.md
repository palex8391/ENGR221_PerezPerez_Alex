# Author: Alex Perez

# Date: 07/12/26

# Lab 4: Searching Algorithms

This lab implements a Snake-style game called Duck Collector. The player moves around the board collecting ducks while avoiding running off the board or into its own body.

## Files

### cell.py
Represents one cell on the board. A cell can be empty, player, body, or food.

### controller.py
Controls the game loop. It handles key presses, updates the player, adds food, and refreshes the display.

### display.py
Handles the graphics. It draws the board, player, body, food, score, and game-over message.

### preferences.py
Stores constant values used by the game, such as board size, colors, images, font sizes, and timing.

### search_structure.py
Contains the custom Queue and Stack classes used for BFS and DFS.

### game_data.py
Stores the game state, including the board, player body, food, score, movement mode, and AI search logic.

## Modified Files

I modified:

- search_structure.py
- game_data.py
- README.md
- answers.txt

## How to Run

Run:

```bash
python controller.py