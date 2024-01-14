# main.py

from game import Game

def main():
    try:
        print("\n\n--- Welcome to the ultimate Rock, Paper, Scissors experience! ---\n") 
        
        if Game.ask_to_start_game():
            Game.run_game()
        else:
            print("Maybe next time! Goodbye!\n")

    except Exception as error:
        print(f"An unexpected error occurred: {error}")

if __name__ == "__main__":
    main()