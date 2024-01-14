# userinterface.py

#Get the user input and validate if it is correct
def get_user_input(text, valid_options):
    while True:
        try:
            user_input = input(text).strip().title()
            if user_input in valid_options:
                return user_input
            else:
                print(f"Invalid input. Please choose from {valid_options}")
        except Exception as error:
            print(f"An error occurred: {error}. Please try again.")
