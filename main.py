# Main project file

class Character:
    """Class for a character"""

    def __init__(self, attack, hp):
        self.attack
        self.hp

    def attacked(self, attack):
        self.hp = self.hp - attack
        if self.hp < 0:
            self.hp = 0

moe = Character(50,5)
joe = Character(65,14)

moe.attacked()



