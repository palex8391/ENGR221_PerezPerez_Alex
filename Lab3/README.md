## Author
Alex Perez Perez

## Date
Last Updated: June 2026

# Lab 3 - Sorting Algorithm Visualizer

## Description
This project implements and visualizes three sorting algorithms using Python and Pygame. The program displays each step of the sorting process so the user can see how Selection Sort, Insertion Sort, and Bubble Sort organize a list of randomly generated values. Users can step through each algorithm one operation at a time or run it continuously.

## Files

- **sorting_algorithms.py** – Implements the Selection Sort, Insertion Sort, and Bubble Sort algorithms and measures their runtime. *(Modified)*
- **controller.py** – Controls the program flow, handles keyboard input, and updates the visualization.
- **display.py** – Draws the sorting visualization and displays the array on the screen.
- **preferences.py** – Stores constants such as colors, window size, timing, and other program settings.


## How to Run
1. Open a terminal in the project folder.
2. Run:
python controller.py


## Controls
- **S** – Start Selection Sort
- **I** – Start Insertion Sort
- **B** – Start Bubble Sort
- **R** – Reset the current algorithm
- **Right Arrow** – Advance one step
- **Space** – Run continuously
