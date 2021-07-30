from base_class.player import Player
# Human class
# Human class extends Player class
class Human(Player):
    def __init__(self, pid, pname):
        super().__init__(pid, pname, "human")