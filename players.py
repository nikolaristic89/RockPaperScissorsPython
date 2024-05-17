# players.py

import random
from userinterface import get_user_input
#nlkndfjndkjfn
class Player:
    def __init__(self, name):
        self.name = name

    def choose_action(self):
        pass

class HumanPlayer(Player):
    def choose_action(self):
        return get_user_input("\nPlease enter your choice (Rock, Paper, or Scissors): ", ["Rock", "Paper", "Scissors"])

class ComputerPlayer(Player):
    def choose_action(self):
        return random.choice(["Rock", "Paper", "Scissors"])
