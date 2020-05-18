"""
Module designed to handle races.
"""


class BaseRace:
    birth_chance_percentage = 10
    maturity_age = 16
    elder_age = 60
    aging_percentage = 10
    death_chance_percentage = 1
    hp = 100
    strength = 10
    training = 10
    intelligence = 20
    combat_skill = 10
    work_skill = 20
    scientific_breakout_chance_percentage = 3
    environment_effects = {}
    immune_list = ()


class RaceYians(BaseRace):
    pass


class RaceBrutfals(BaseRace):
    strength = int(BaseRace.strength * 1.4)
    training = int(BaseRace.training * 1.5)
    aging_percentage = int(BaseRace.aging_percentage * 0.9)
    intelligence = int(BaseRace.intelligence * 0.5)


class RaceMinpows(BaseRace):
    intelligence = int(BaseRace.intelligence * 1.5)
    work_skill = int(BaseRace.work_skill * 1.25)
    strength = int(BaseRace.strength * 0.8)
    aging_percentage = int(BaseRace.aging_percentage * 1.1)
    combat_skill = int(BaseRace.combat_skill * 0.7)


class RaceIndelvs(BaseRace):
    birth_chance_percentage = int(BaseRace.birth_chance_percentage * 1.4)
    environment_effects = {env: value * 0.5
                           for env, value in BaseRace.environment_effects.items()}
    intelligence = int(BaseRace.intelligence * 0.8)
    work_skill = int(BaseRace.work_skill * 0.8)
    combat_skill = int(BaseRace.combat_skill * 0.8)


class RaceTmechs(BaseRace):
    environment_effects = {}
    intelligence = int(BaseRace.intelligence * 1.2)
    work_skill = int(BaseRace.work_skill * 1.5)
    birth_chance_percentage = int(BaseRace.birth_chance_percentage * 0.7)
    strength = int(BaseRace.strength * 0.7)
    combat_skill = int(BaseRace.combat_skill * 0.8)


class RaceWarjas(BaseRace):
    combat_skill = int(BaseRace.combat_skill * 1.5)
    strength = int(BaseRace.strength * 1.1)
    aging_percentage = int(BaseRace.aging_percentage * 1.2)
    intelligence = int(BaseRace.intelligence * 0.8)
    work_skill = int(BaseRace.work_skill * 0.8)
