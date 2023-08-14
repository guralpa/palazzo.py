#!python3

class tower:
    '''
    A class modelling a single Palazzo tower.
    
    Attributes:
        self._floors (list_of floor): The floors of the tower, in order, from bottom to top.
        self._score (int): The score of the tower at any given time.
    
    Methods:
        self.__init__(tower, floor): Initializes the tower with the given floor as the first and a score of -5.
        self.add_floor (tower,floor): Adds a floor to the top of the tower.
        self.remove_floor (tower, int): Removes a floor from the tower at the given floor number.
        self.insert_floor (tower, floor, int): Inserts a floor into the tower at the given floor number.
    
    '''
    def __init__(self, foundation):
        '''
        Initializes tower with the first block placed and assigns the single-floor score of -5.
        
        Args:
            self (tower): The tower being initialized.
            foundation (level): The first level in the tower.
        '''
        self._floors = [foundation]
        self._score = -5
    
    def add_floor(self, floor):
        '''
        Adds a floor to the top of the tower and updates the score of the tower. Intended for use when addings floors after purchase.
        
        Args:
            self (tower): The tower being added to.
            floor (floor): The floor being added to the tower.
        
        Returns:
            None
        '''
        if self._floors[-1].level < floor.level():
            self._floors.append(floor)
            self._score = evaluate_tower(self)
        else:
            print("Invalid floor level.")
    
    def remove_floor(self, floor_number):
        '''
        Removes the floor at the given number from the tower, returning it as a floor object. Updates the score of the tower.
        
        Args:
            self (tower): The tower being removed from.
            floor_number (int): The floor number of the floor being removed.
        
        Returns:
            removed_floor (floor): The floor that was removed.
        '''
        if 0 < floor_number and floor_number <= len(self._floors):
            removed_floor = self._floors[floor_number-1]
            self._floors = self._floors[0:floor_number-1] + self._floors[floor_number:len(self.floors)]
            self._score = evaluate_tower(self)
            return removed_floor
        else:
            print("Invalid floor number.")
    
    def insert_floor(self, floor, floor_number):
        '''
        Inserts a floor at the given number from the tower, pushing all other floors up. Updates the score of the tower.
        
        Args:
            self (tower): The tower being inserted into.
            floor (floor): The floor being inserted.
            floor_number (int): The floor number at which the floor will be inserted.
        
        Returns:
            None
        '''
        if floor_number == 1 and floor.level() <= self._floors[0].level():
            self._floors.insert(floor,0)
            self._score = evaluate_tower(self)
        elif floor_number == len(self._floors)+1 and self._floors[-1].level() < floor.level():
            self._floors.append(floor)
            self._score = evaluate_tower(self)
        elif 1 < floor_number and floor_number <= len(self._floors):
            if self._floors[floor_number-2].level() < floor.level() and floor.level() < self._floors[floor_number-1].level():
                self._floors.insert(floor,floor_number-1)
                self._score = evaluate_tower(self)
        else:
            print("Invalid floor number.")

def evaluate_tower(tower):
    '''Calculates the score of a tower according to Palazzo rules and returns it.'''
    return -5