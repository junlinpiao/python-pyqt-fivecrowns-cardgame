from base_class.player import Player

# class for computer player.
# Computer class extends Player class
class Computer(Player):
    def __init__(self, pid, pname):
        super().__init__(pid, pname, "computer")
