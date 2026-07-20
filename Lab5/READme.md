# Author: Alex Perez

# Date: 07/19/2026


# ENGR 221 Lab 5: Koch Snowflake

## Description

This project draws a Koch snowflake fractal in two different ways:

1. A recursive implementation that uses Python's call stack.
2. A non-recursive implementation that uses a list as an explicit stack.

The program can also compare the runtime and memory usage of the two approaches.

## Files

### `snowflake.py`
Contains the `KochSnowflake` class and all methods needed to:

- Initialize the turtle.
- Draw one Koch curve recursively.
- Draw one Koch curve with an explicit stack.
- Draw all three sides of the snowflake.
- Measure runtime and memory usage.

### `answers.txt`
Contains written answers and pseudocode for Parts 1 through 4 of the assignment.

### `README.md`
Explains the project files and how to run the program.

## Requirements

- Python 3
- Python Turtle
- `memory_profiler`

Install `memory_profiler` with:

```bash
pip install memory-profiler
```

## How to Run

Open a terminal in the Lab5 folder and run:

```bash
python snowflake.py
```

At the bottom of `snowflake.py`, create a snowflake object:

```python
s = KochSnowflake(500, 2)
```

The first argument is the original side length. The second argument is the depth.

Run the recursive version with:

```python
s.draw_snowflake_recursive()
```

Run the stack version with:

```python
s.draw_snowflake_stack()
```

Compare both versions with:

```python
s.compare_snowflake()
```

Only one of these calls should normally be uncommented at a time.

## Important Concept

At depth 0, one side is a single straight line. At every greater depth, each line segment is replaced by four smaller segments. Therefore, one side has `4^depth` segments, and the full snowflake has `3 * 4^depth` segments.