"""
@author: TEKIN Abdurrahim Burak
@date: 2016-11-27
-- Simple game with threads! --
"""

class game_model:
    """
    Model class for the game
    """
    def __init__(self):
        """
        Constructor for game_model
        """
        self.übrig = 15
        self.korrekt = 0
        self.falsch = 0
        self.spiele = 1
        self.letztes = 1