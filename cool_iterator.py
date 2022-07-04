
import gol
import blessed
import time


# Just a cool iterator!
def cool_iterator(steps, starting_array, wait=1, show_step=True):
    """Game of Life iterator. Prints step by step.

    Args:
        steps (int): How many steps should have taken?
        starting_array (list): 2-dimensional list.
        wait (number, optional): How many seconds it waits between each step? Defaults to 1.
        step (bool, optional): Print the step number? Defaults to True.
    """

    # Some tests...
    if type(steps) != int:
        raise ValueError('Steps should be a natural number.')
    if type(starting_array) != list:
        raise ValueError('Array is not a 2D-list.')
    try:
        if type(starting_array[0]) != list:
            raise ValueError('Array is not a 2D-list.')
    except (IndexError,TypeError):
        raise ValueError('Array is not a 2D-list.')
    
    term = blessed.Terminal()
    game = gol.GameOfLife(starting_array)
    
    # Printing the game of life.
    with term.fullscreen():
        
        for step in range(steps+1):
            game.tick(0, True)
            if show_step:
                print(step)
            time.sleep(wait)
            
            game.tick(1)
            print(term.clear, end='')
            