
# What is this?
# Look at https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for more information.

# How it works? Actually it's not that complex.
# 1. Think the array as a coordinate system and locate alive coordinates on it. That is self.__alive.
# 2. Alive coordinates are going to affect coordinates around them, so locate them too. 
#    And put them all together in another list. Lets call it self.__important.
# 3. Now iterate over those important coordinates and find out how many of their neighbors are alive,
#    then apply the rules to decide whether they are alive or not. Save all the alive coordinates in a
#    temprorary list. Then update self.__alive and self.__important with it.
# 4. Now we returned back to start. Keep iterating 2-5 if you want, or continue, to return the result list.
# 5. Remember that I said to think the array as a coordinate system? Now think the result as a rectangle
#    on that coordinate system. Max and min alive coordinates are making up the corners, and the rest is inside it.
#    Now move one of the corners to the origin, in a way so every coordinate, except the origin, are positive.
#    Now every alive coordinates are moved to this positive area.
# 6. It is now actually like rows and columns of the starting list. Show alive coordinates as ones and dead 
#    coordinates as zeroes. Finally, return the final product and that's it. A game of life algorithm.


from multiprocessing.sharedctypes import Value


class GameOfLife(object):
    """A class for the game of life algorithm.

    Args:
        object (class): Sub-class of object.
    """
    def __init__(self, array):
        """Initialize a GameOfLife instance.

        Args:
            array (list): Assumes array is a 2-dimensional list of zeroes and ones.
        """
        if type(array) != list:
            raise ValueError
        
        self.__alive = []
        
        y_len = len(array)
        x_len = len(array[0])

        # Think it as a coordinate system and locate the alive coords.
        # Actually, this is a bottom-up coordinates system, but this is not an important detail.
        # After all, coordinates are coordinates and the steps are also same. It's just a funny fact.
        for y in range(y_len):    
            for x in range(x_len):
                if array[y][x] == 1:
                    self.__alive.append((x, y))
                elif array[y][x] == 0:
                    continue
                else:
                    raise ValueError
                            
        # Locating and saving the important coordinates.
        self.__important = []
        self.__important_coords()
    
    
    # Returns neighborhood coordinates of a coordinate. 
    def __look_around(self, coord):
        x, y = coord
        
        return ((x+1, y), (x-1, y), (x, y+1), (x, y-1), 
                (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1))
    
    
    # Function for locating and saving important coordinates.
    # And also for updating them.
    def __important_coords(self):
        self.__important = []
        self.__important.extend(self.__alive)
        
        for alive_coord in self.__alive:
            neighborhood = self.__look_around(alive_coord)
            
            for any_coord in neighborhood:
                if any_coord not in self.__important:
                    self.__important.append(any_coord)
    
    
    # Iterates the game one time. Iterate over the important coords
    # And apply to rules on them. Then save the alive ones.         
    def __single_tick(self):
        new_alive = []
               
        for impo_coord in self.__important:
            neighborhood = self.__look_around(impo_coord)

            alive_count = 0
            for any_coord in neighborhood:
                if any_coord in self.__alive:
                    alive_count += 1
            
            if impo_coord in self.__alive:
                if alive_count == 2 or alive_count == 3:
                    new_alive.append(impo_coord)
            
            else:
                if alive_count == 3:
                    new_alive.append(impo_coord)
        
        self.__alive = new_alive.copy()
        self.__important_coords()
                

    # The only method that the user will see. Run __single_tick() n times.
    # And then create the result list. Set n=0 to return the current state.
    def tick(self, n, prt=False):
        """Returns the n-th iteration of game of life as a list, similar to
        the list that the class is instanced. Keep in mind that n

        Args:
            n (int): Number of iterations. 0 to return the current state.
            prt (bool, optional): If True, prints the resulting list in a nice way. Skips if all 
            are dead. Defaults to False.

        Returns:
            list: Returns the result as a 2-dimensional list. If no alive 
            coordinates left, returns an empty 2-dimensional list.
        """
        
        # Some tests...
        if type(n) != type(int):
            raise ValueError
        if n < 0:
            raise ValueError
        
        for _ in range(n):
            self.__single_tick()
        
        # If all is dead, return this sad, empty list.
        if self.__alive == []:
            return [[]]
        
        # Maximum and miniman x and y values.
        x_max = max(self.__alive)[0]
        x_min = min(self.__alive)[0]
        y_max = max(self.__alive, key=lambda x: x[1])[1]
        y_min = min(self.__alive, key=lambda x: x[1])[1]
        
        # This difference is the length and height of the final 2D list.
        x = x_max - x_min
        y = y_max - y_min
        
        # And that is how much each coordinate should be moved at x and y axis
        # to come to their final positions. Think of it that way: 
        # Only x_max length is positive, but it should be x positive, so we are moving
        # it x - x_max coordinates.
        x_dif = x - x_max
        y_dif = y - y_max
        
        # Copying each row manually to prevent mutations.
        row = [0 for _ in range(x+1)]
        res = [row.copy() for _ in range(y+1)]
        
        # Currently, result is only consisted of zeroes. 
        # Adding ones for alive coordinates.
        for alive_coord in self.__alive:
            alive_x, alive_y = alive_coord
            
            new_x = alive_x + x_dif
            new_y = alive_y + y_dif
            
            res[new_y][new_x] = 1
        
        # First print, then return.
        if prt == True:
            for row in res: 
                for cell in row:
                    if cell:
                        print('▓▓', end='')
                    else:
                        print('░░', end='')
                print()
    
        return res

