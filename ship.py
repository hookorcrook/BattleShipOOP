class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.hits = 0

    def hit(self):
        """Increases the hit count and checks if the ship is sunk."""
        self.hits += 1
        if self.is_sunk():
            print(f"SHIP SUNK! {self.name} has sunk!")  # Notify when the ship sinks
        return self.is_sunk()

    def is_sunk(self):
        """Returns True if the ship is sunk (i.e., hit count equals ship size)."""
        return self.hits == self.size
