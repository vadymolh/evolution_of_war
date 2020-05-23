"""
Module designed to handle research tree.
"""


class ResearchTree:

    """ This class should handle all researches per player.

    Each player will have his own research tree.
    """

    pass


class Research:

    """ Class handles separate particular research. """

    def __init__(self, research_name, dependencies, unlock_techs):
        self.name = research_name
        self.dependencies = dependencies
        self.techs = unlock_techs


class Tech:

    """ Class handles separate particular technology.

    Technologies can be unlocked with researches.
    For example: research in iron craft can unlock iron instruments, swords, etc.

    Properties of tech is what tech improves, e.g. +10 damage, +20% of production
    """

    def __init__(self, tech_name, properties):
        self.name = tech_name
        self.properties = properties
