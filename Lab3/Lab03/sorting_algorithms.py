""" 
Author: Alex Perez Perez
Date: 07/05/26
Description: This program implements three sorting algorithms: selection sort, insertion sort, and bubble sort.
 Each algorithm is implemented as a generator function that yields the indices of the elements being compared or 
 swapped. The program also includes methods to create a new array to sort, get the next step in the sorting process, 
restart the sorting process with a new algorithm, and measure the runtime of the sorting algorithms.
"""

import random
import time

from preferences import Preferences

class SortingAlgorithms: 
    def __init__(self):
        # The algorithm to sort
        self.array = []

        # Any indices to highl
        self.inner_idx = -1
        self.outer_idx = -1 

        # A string representing the current sorting algorithm
        self.current_alg = None

        # Store the method of the sorting algorithm being run
        self.alg_method = None
    
    def create_new_array(self, length=Preferences.NUM_ELEMENTS) -> list:
        """ Create a new array to sort """
        return [random.randint(0, Preferences.MAX_VAL) \
                      for _ in range(length)]
    
    def get_next_step(self) -> None:
        """ Updates the value of self.selected_idx whenever we reach 
            a "yield" statement in any of the below sorting algorithms. """
        
        try:
            # Treats the current sorting algorithm as an iterator
            # and sets self.selected_idx to be the next "element"
            self.outer_idx, self.inner_idx = next(self.alg_method)
        # Clear the selected_idx value when we reach the end of the method
        except StopIteration:
            self.outer_idx, self.inner_idx = -1, -1

    def restart(self, new_alg, length=Preferences.NUM_ELEMENTS) -> None:
        """ Restart the sorting process with the new algorithm. 
            Creates a new array to sort. """
        
        self.current_alg = new_alg
        self.alg_method = {
            "selection" : self.selection_sort,
            "insertion" : self.insertion_sort,
            "bubble" : self.bubble_sort
        }[self.current_alg]()
        self.array = self.create_new_array(length)
        self.outer_idx, self.inner_idx = -1, -1

    def selection_sort(self):
        """ An implementation of the Selection sort algorithm. 
            A generator function which creates an iterator that 
            iterates through each "yielded" value. """
        
        
        # Get the current number of items in the list.
        n = len(self.array)

        #Go through each position in the list from left to right.
        for i in range(n):
            # Highlight the current outer-loop postion.
            yield -1, i
            # Assume the current positon holds the smallest value so far.
            min_idx = i

            # If Search the rest of the unsorted portion for a smaller value.
            for j in range(i + 1, n):
                # Highlight the current candidate comparison.
                yield min_idx, j

                # If a smaller value is found, remember its index.
                if self.array[j] < self.array[min_idx]:
                    min_idx = j 
            
            # Swap the smallest found value into its final sorted position.
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            # Highlight the completed swap so the visuallization can show it.
            yield i, min_idx
                

    def insertion_sort(self):
        """ An implementation of the Insertion sort algorithm. """
        n = len(self.array)
    
        for i in range(1, n):
            # Highlight the current index being inserted into the sorted part.
            yield -1, i

            j = i

            # Move the current item left while it is smaller than the item before it.
            while j > 0 and self.array[j -1] > self.array[j]:
                # Highlight the pair being compared.
                yield j - 1, j

                # Swap the two values to place the current item in the correct spot.
                self.array[j], self.array[j -1] = self.array[j -1], self.array[j]

                # Highlight the completed swap.
                yield j, j - 1
                j -= 1
        

    def bubble_sort(self):
        """ An implementation of the Bubble sort algorithm. 
            A generator function which creates an iterator that
            iterates through eac "yielded" value."""

        n = len(self.array)
    
        for i in range(n - 1):

            # Highlight the current pass through the list.
            yield -1, i

            for j in range(n - 1 - i):
                # Highlight the adjecent pair being compared. 
                yield j, j + 1

                if self.array[j] > self.array[j + 1]:
                    # Swap the two values if they are out of order.
                    self.array[j], self.array[j +1] = self.array[j + 1], self.array[j]

                    # Highlight the completed swap.
                    yield j, j + 1
            

    def get_runtime(self) -> float:
        """ Returns the length of time (in seconds) that it took for 
            the function_to_run to sort a list of length list_length """

        # Get the time before running
        start_time = time.time()
        # Sort the given list
        for _ in self.alg_method:
            pass
        # Get the time after running
        end_time = time.time()
        # Return the difference
        return end_time - start_time

if __name__ == "__main__":
    s = SortingAlgorithms()
    s.restart("selection", 10000)
    print(s.get_runtime())