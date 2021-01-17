class travel():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

def add_passenger(self, name):
  if not self.space_left():
      return False 
  self.passengers.append(name)
    return True

def space_left(self):
    return self.capacity - len(self.passengers)

travel = Travel(capacity = 3)

people = ["Leom", "Dammy", "Revelation", "Kemi"]
for person in people:
    if travel.add_passenger(person):
        print(f"{person} added successfully")
    else:
        print(f"{person} has no available seat")