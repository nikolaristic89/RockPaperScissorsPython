# game.py

from players import HumanPlayer, ComputerPlayer
from userinterface import get_user_input

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    #Ask user if they want to start a game
    def ask_to_start_game():
        user_choice = get_user_input("Are you ready to begin? \nPlease enter (Yes or No): ", ["Yes", "No"])
        if user_choice == "Yes":
            return True
        if user_choice == "No":
            return False

    #Run a new game and ask at the end if a new game should be started
    def run_game():
        while True:
            new_game = Game.ask_game_mode()
            result = new_game.play_round()

            play_again = get_user_input("Do you want to play another round? \nPlease enter (Yes or No)", ["Yes", "No"])
            if play_again == "No":
                print("Thank you for playing!\n")
                break

    #Ask user which game mode they want to play
    def ask_game_mode():
        print("\nPlease select the game mode:")
        print("1: Human vs Computer - Test your skills against the computer!")
        print("2: Computer vs Computer - Watch two robots compete!")
        game_mode = get_user_input("\nPlease enter (1 or 2): ", ["1", "2"])
        if game_mode == "1":
            return Game(HumanPlayer("Human"), ComputerPlayer("Computer"))
        elif game_mode == "2":
            return Game(ComputerPlayer("Computer 1"), ComputerPlayer("Computer 2"))

    #Play a new round of rock, paper, scissors
    def play_round(self):
        choice_player1 = self.player1.choose_action()
        choice_player2 = self.player2.choose_action()
        print("\n--- New Round ---")
        print(f"{self.player1.name} chooses {choice_player1}")
        print(f"{self.player2.name} chooses {choice_player2}")

        result = self.determine_winner(choice_player1, choice_player2)
        print(f"--- {result} ---\n")
        return result

    #Determine who is the winner and show it to the user
    def determine_winner(self, choice_player1, choice_player2):
        try:
            if choice_player1 == choice_player2:
                return "It's a tie!"
            elif (choice_player1 == "Rock" and choice_player2 == "Scissors") or \
                 (choice_player1 == "Scissors" and choice_player2 == "Paper") or \
                 (choice_player1 == "Paper" and choice_player2 == "Rock"):
                return f"{self.player1.name} wins!"
            else:
                return f"{self.player2.name} wins!"
        except Exception as error:
            print(f"An error occurred in determining the winner: {error}")
            return "Error in determining winner"
