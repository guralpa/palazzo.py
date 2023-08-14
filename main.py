#!python3

class tower:
    def __init__(self, foundation):
        self._floors = [foundation]
        self._score = -5
    
    def add_floor(self, floor):
        if self._floors[-1].level < floor.level():
            self._floors.append(floor)
            self._score = evaluate_tower(self)
        else:
            print("Invalid floor level.")
    
    def remove_floor(self, floor_number):
        if 0 < floor_number and floor_number <= len(self._floors):
            self._floors = self._floors[0:floor_number-1] + self._floors[floor_number:len(self.floors)]
            self._score = evaluate_tower(self)
        else:
            print("Invalid floor number.")
    
    def insert_floor(self, floor, floor_number):
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
    return -5