""" TODO
Author: Alex Perez Perez 
Date: June 28, 2026 last updated
Description: Stores the game data for Antartic Survival, including the board, player movement, food, enemies,
score, and game-over state.
"""

import random

from cell import Cell
from preferences import Preferences

class GameData:
    def __init__(self):
        # The current state of the board
        self.board = [[Cell(row, col) for col in range(Preferences.NUM_COLS)] 
                                      for row in range(Preferences.NUM_ROWS)]
        
        # Whether or not the game is over
        self.gameover = False

        # The current cell containing the player
        self.player = self.board[0][0]    # Start at the top left
        self.player.become_player()

        # The number of empty cells on the board, accounting for the player cell
        self.num_empty_cells = Preferences.NUM_CELLS - 1

        # A list of cells containing food
        self.food = []
        # Number of food eaten
        self.score = 0

        # A list of cells containing enemies
        self.enemies = []


    #######################
    # Game Limits Methods #
    #######################

    def at_max_food(self) -> bool:
        """ Check whether we can add more food """
        return len(self.food) / self.num_empty_cells > Preferences.MAX_FOOD
    
    def at_max_enemies(self) -> bool:
        """ Check whether we can add more enemies """
        return len(self.enemies) / self.num_empty_cells > Preferences.MAX_ENEMIES

    def set_game_over(self) -> None:
        """ Turn on the game over flag """
        self.gameover = True


    ##############################
    # Neighbor Retrieval Methods #
    ##############################

    def get_west_neighbor(self, cell: Cell) -> Cell:
        """ Returns the cell immediately to the left of the given cell. 
            If we are at the  edge of the map, return None. """
        if cell.get_col() == 0:  # If we are at the left edge of the board, return None
            return None 
        else:
            return self.board[cell.get_row()][cell.get_col() - 1]  # Return the cell to the left of the given cell
        
        
    def get_east_neighbor(self, cell: Cell) -> Cell:
        """ Returns the cell immediately to the right of the given cell.
            If we are at the edge of the map, return None. """
        if cell.get_col() == Preferences.NUM_COLS - 1:  # If we are at the right edge of the board, return None
            return None
        else:
            return self.board[cell.get_row()][cell.get_col() + 1]  # Return the cell to the right of the given cell
        
        
    def get_north_neighbor(self, cell: Cell) -> Cell:
        """ Returns the cell immediately above the given cell.
            If we are at the edge of the map, return None. """
        if cell.get_row() == 0:  # If we are at the top edge of the board, return None
            return None
        else:
            return self.board[cell.get_row() - 1][cell.get_col()]  # Return the cell above the given cell
        
        
    def get_south_neighbor(self, cell: Cell) -> Cell:
        """ Returns the cell immediately below the given cell.
            If we are at the edge of the map, return None. """
        if cell.get_row() == Preferences.NUM_ROWS - 1:  # If we are at the bottom edge of the board, return None
            return None
        else:
            return self.board[cell.get_row() + 1][cell.get_col()]  # Return the cell below the given cell
        


    ###########################
    # Player Movement Methods #
    ###########################
        
    def move_player_right(self) -> None:
        """ Move the player one cell to the right if it is empty """
        cell = self.get_east_neighbor(self.player) # Get the cell to the right of the player
        if cell is not None: # If the cell is not None, move the player to that cell
            self.move_player_to_cell(cell) # Move the player to the new cell

    def move_player_left(self) -> None:
        """ Move the player one cell to the left if it is empty """
        cell = self.get_west_neighbor(self.player) # Get the cell to the left of the player
        if cell is not None: # If the cell is not None, move the player to that cell
            self.move_player_to_cell(cell) # Move the player to the new cell

    def move_player_up(self) -> None:
        """ Move the player one cell up if it is empty """
        cell = self.get_north_neighbor(self.player) # Get the cell above the player
        if cell is not None: # If the cell is not None, move the player to that cell
            self.move_player_to_cell(cell) # Move the player to the new cell

    def move_player_down(self) -> None:
        """ Move the player one cell down if it is empty """
        cell = self.get_south_neighbor(self.player) # Get the cell below the player
        if cell is not None: # If the cell is not None, move player to that cell
            self.move_player_to_cell(cell) # Move the player to the new cell

    def move_player_to_cell(self, cell: Cell) -> None:
        """ Move the player to the given cell """


        # If there is food in this cell, eat it
        if cell.is_food():
            self.eat_food(cell)
            self.update_player_cell(cell)
        # If there is an enemy in this cell, game over!
        elif cell.is_enemy():
            self.player.become_empty()
            self.set_game_over()
        # Otherwise, update the player location
        else:
            self.update_player_cell(cell)

    def update_player_cell(self, new_cell: Cell) -> None:
        """ Move the player to the new cell """
    
        # Empty the cell the player just moved away from
        self.player.become_empty()
        # Update the player to the new cell
        self.player = new_cell
        # Change the new cell to be the player type
        self.player.become_player()


    ########################
    # Food Related Methods #
    ########################

    def add_food(self) -> None:
        """ Adds food to a random open spot on the board """

        # Find a row on the board
        row = random.randrange(0, Preferences.NUM_ROWS)
        # Find a col on the board
        col = random.randrange(0, Preferences.NUM_COLS)

        cell = self.board[row][col] # Get the rando cell on the board

        if cell.is_empty() and not self.at_max_food():
            cell.become_food()          # Change the empty cell into food 
            self.food.append(cell)      # Save this food cell in the food list
            self.num_empty_cells -= 1   # One less empty cell is available


    def eat_food(self, cell: Cell) -> None:
        """ Behavior for when the player eats food """
        self.food.remove(cell)          # Remove the eaten food from the food list
        self.score += 1                 # Increase the players's score
        self.num_empty_cells += 1       # Food is gone, so there is one more empty cell
        


    ##########################
    # Enemy Movement Methods #
    ##########################

    def add_enemy(self) -> None:
        """ Adds an enemy to the bottom right corner of the board """
        # Get the bottom-right cell of the board
        cell = self.board[Preferences.NUM_ROWS -1][Preferences.NUM_COLS -1]

        # If the player is in that cell, the enemy cathces the player
        if cell.is_player():
            self.set_game_over()

        #If the food is in that cell, replace the food with an enemy 
        elif cell.is_food():
            self.food.remove(cell)
            cell.become_enemy()
            self.enemies.append(cell)

        # If the cell is empty and there is room for more enemies, add enemy 
        elif cell.is_empty() and not self.at_max_enemies():
            cell.become_enemy()
            self.enemies.append(cell)
            self.num_empty_cells -= 1
        

    def move_enemy_to_cell(self, enemy_cell: Cell, 
                           cell: Cell, idx: int) -> None:
        """ Moves the enemy cell to a new location.
            idx refpresents the index of that enemy in
             the enemies list. """
        
        # If there is no cell in that direction, do not move the enemy
        if cell is None:
            return
        
        # If the enemy moves onto the player, the game is over
        if cell.is_player():
            enemy_cell.become_empty()
            cell.become_enemy()
            self.enemies[idx] = cell
            self.set_game_over() 

        # If the destination is empty, move the enemy there
        elif cell.is_empty():
            enemy_cell.become_empty()
            cell.become_enemy()
            self.enemies[idx] = cell

        # If the destination has food, remove the food and move the enemy there
        elif cell.is_food():
            self.food.remove(cell)
            enemy_cell.become_empty()
            cell.become_enemy()
            self.enemies[idx] = cell
            self.num_empty_cells += 1
        

    def move_enemy_left(self, idx: int) -> None:
        """ Move the enemy at index idx left one cell """

        enemy = self.enemies[idx]                   # Get the enemy from the enemies list
        cell = self.get_west_neighbor(enemy)        # Find the cell to the left of the enemy
        self.move_enemy_to_cell(enemy, cell, idx)   # Move the enemy if possibble
       

    def move_enemy_right(self, idx: int) -> None:
        """ Move the enemy at index idx right one cell """

        enemy = self.enemies[idx]
        cell = self.get_east_neighbor(enemy)
        self.move_enemy_to_cell(enemy, cell, idx)
        

    def move_enemy_up(self, idx: int) -> None:
        """ Move the enemy at index idx up one cell """
        enemy = self.enemies[idx]
        cell = self.get_north_neighbor(enemy)
        self.move_enemy_to_cell(enemy, cell, idx)


    def move_enemy_down(self, idx: int) -> None:
        """ Move the enemy at index idx down one cell """
        enemy = self.enemies[idx]
        cell = self.get_south_neighbor(enemy)
        self.move_enemy_to_cell(enemy, cell, idx)
        


if __name__ == "__main__":
    gd = GameData()
    # You can modify the line below for testing!
    print(gd.get_west_neighbor(gd.player))