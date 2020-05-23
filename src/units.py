"""
Module designed to handle game units: people, robots, critters, etc.
"""


class BaseUnit:
    pass


class HumanUnit(BaseUnit):

    def __init__(self, parameters: dict):
        """
            Parameters:
                {
                    race: str,
                    hp: int,
                    age: float,
                    strengh: int,
                    intelligence: int,
                    stamina: int,
                    disease: str,
                    combat_exp: int,
                    weapon: dict,
                    shield: dict,
                    craft: dict,
                }
        """

    def move(self):
        """Perform move on global map."""
        pass

    def attack(self):
        """Perform attack on enemy's unit."""
        pass

    def receive_damage(self):
        """Receive damage from enemy's unit."""
        pass

    def work(self):
        """Perform current job."""
        pass

    def train(self):
        """Train unit during specific actions."""
        pass

    def disease(self):
        """Set disease if any."""
        pass

    def apply_effects(self):
        """Apply different effects, cause by diseases, environment, etc."""
        pass

    def action(self):
        """Perform one of possible actions.

        Action list:
            move,
            attack,
            work,
            train
        """
        pass
