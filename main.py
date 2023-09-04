#!python3

class tile:
    '''
    A class modelling a single Palazzo tile.

    Attributes:
        self._level (int): Palace level of the tile
        self._windows (int): Number of windows on the tile
        self._material (string): Material of the tile
    
    Methods:
        self.__init__(tile, int, int, string): Initialize level, windows, and material.
        self.level(): Getter for self._level
        self.windows(): Getter for self._windows
        self.material(): Getter for self._material
    '''

    def __init__(self, level, windows, material):
        '''
        Initializes the tile with the given level, windows, and material.

        Args:
            level (int): The level value of the tile
            windows (int): The number of windows on the tile
            material (string): The material the tile is made of
        '''
        self._level = level
        self._windows = windows
        self._material = material
    
    def level(self):
        '''Getter for self._level.'''
        return self._level
    
    def windows(self):
        '''Getter for self._windows.'''
        return self._windows
    
    def material(self):
        '''Getter for self._material.'''
        return self._material

class palace:
    '''
    A class modelling a single Palazzo palace.
    
    Attributes:
        self._tiles (list_of tile): The tiles of the palace, in order, from bottom to top.
        self._score (int): The score of the palace at any given time.
    
    Methods:
        self.__init__(palace, tile): Initializes the palace with the given tile as the first and a score of -5.
        self.add_tile (palace,tile): Adds a tile to the top of the palace.
        self.remove_tile (palace, int): Removes a tile from the palace at the given tile number.
        self.insert_tile (palace, tile, int): Inserts a tile into the palace at the given tile number.
        self.tile_count (palace): Returns the number of tiles in the palace.
        self.windows_count (palace): Returns the number of windows on the palace.
        self.is_pure (palace): Returns 1 if the palace is of a single material, 0 if not.
        self.score (palace): Getter for self._score.
    '''
    def __init__(self, foundation):
        '''
        Initializes palace with the first block placed and assigns the single-tile score of -5.
        
        Args:
            self (palace): The palace being initialized.
            foundation (tile): The first level in the palace.
        '''
        self._tiles = [foundation]
        self._score = -5
    
    def add_tile(self, tile):
        '''
        Adds a tile to the top of the palace and updates the score of the palace. Intended for use when addings tiles after purchase.
        
        Args:
            self (palace): The palace being added to.
            tile (tile): The tile being added to the palace.
        
        Returns:
            None
        '''
        if self._tiles[-1].level() < tile.level():
            self._tiles.append(tile)
            self._score = evaluate_palace(self)
        else:
            print("Invalid tile level.")
    
    def remove_tile(self, tile_number):
        '''
        Removes the tile at the given number from the palace, returning it as a tile object. Updates the score of the palace.
        
        Args:
            self (palace): The palace being removed from.
            tile_number (int): The tile number of the tile being removed.
        
        Returns:
            removed_tile (tile): The tile that was removed.
        '''
        if 0 < tile_number and tile_number <= len(self._tiles):
            removed_tile = self._tiles[tile_number-1]
            self._tiles = self._tiles[0:tile_number-1] + self._tiles[tile_number:len(self.tiles)]
            self._score = evaluate_palace(self)
            return removed_tile
        else:
            print("Invalid tile number.")
    
    def insert_tile(self, tile, tile_number):
        '''
        Inserts a tile at the given number from the palace, pushing all other tiles up. Updates the score of the palace.
        
        Args:
            self (palace): The palace being inserted into.
            tile (tile): The tile being inserted.
            tile_number (int): The tile number at which the tile will be inserted.
        
        Returns:
            None
        '''
        if tile_number == 1 and tile.level() <= self._tiles[0].level():
            self._tiles.insert(tile,0)
            self._score = evaluate_palace(self)
        elif tile_number == len(self._tiles)+1 and self._tiles[-1].level() < tile.level():
            self._tiles.append(tile)
            self._score = evaluate_palace(self)
        elif 1 < tile_number and tile_number <= len(self._tiles):
            if self._tiles[tile_number-2].level() < tile.level() and tile.level() < self._tiles[tile_number-1].level():
                self._tiles.insert(tile,tile_number-1)
                self._score = evaluate_palace(self)
        else:
            print("Invalid tile number.")
    
    def tile_count(self):
        '''Returns the number of tiles in the palace.'''
        return len(self._tiles)
    
    def window_count(self):
        '''Returns the number of windows on the palace.'''
        count = 0
        for tile in self._tiles:
            count += tile.windows()
        return count

    def is_pure(self):
        '''Returns a 1 if the palace is pure in material, 0 otherwise.'''
        pure = True
        material = self._tiles[0].material()

        for tile in self._tiles:
            if tile.material() != material:
                pure = False
                break
        
        return pure
    
    def score(self):
        return self._score

def evaluate_palace(palace):
    '''Calculates the score of a palace according to Palazzo rules and returns it.'''
    height = palace.tile_count()
    windows = palace.window_count()
    pure = palace.is_pure()

    if height == 1:
        return -5
    elif height == 2:
        return 0
    elif height == 3:
        return windows + 0 + pure * 3
    elif height == 4:
        return windows + 3 + pure * 3
    elif height == 5:
        return windows + 6 + pure * 6
    else:
        raise Exception("Invalid height.")

### Testing ### Sourced from [https://www.ultraboardgames.com/palazzo/game-rules.php] ### There are 5 * 3 * 3 = 45 Unique tiles in the game.

palace_one = palace(tile(3,3,"S"))
assert palace_one.score() == -5

palace_two = palace(tile(2,3,"B"))
palace_two.add_tile(tile(4,2,"B"))
assert palace_two.score() == 0

palace_three = palace(tile(1,3,"B"))
palace_three.add_tile(tile(2,1,"S"))
palace_three.add_tile(tile(5,2,"B"))
assert palace_three.score() == 6

palace_four = palace(tile(2,2,"S"))
palace_four.add_tile(tile(3,2,"S"))
palace_four.add_tile(tile(4,2,"S"))
palace_four.add_tile(tile(5,1,"S"))
assert palace_four.score() == 13

palace_five = palace(tile(1,3,"M"))
palace_five.add_tile(tile(2,1,"M"))
palace_five.add_tile(tile(3,2,"M"))
palace_five.add_tile(tile(4,3,"S"))
palace_five.add_tile(tile(5,2,"M"))
assert palace_five.score() == 17

palace_six = palace(tile(1,1,"B"))
palace_six.add_tile(tile(2,2,"B"))
palace_six.add_tile(tile(3,3,"B"))
palace_six.add_tile(tile(4,1,"B"))
palace_six.add_tile(tile(5,1,"B"))
assert palace_six.score() == 20

palace_seven = palace(tile(2,2,"M"))
palace_seven.add_tile(tile(3,1,"M"))
palace_seven.add_tile(tile(4,2,"M"))
assert palace_seven.score() == 8