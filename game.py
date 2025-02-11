from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def home():
    user_input=input('Please choose s for scissor, r for rock and p for paper\n')
    result,computer_choose="",""
        # List of numbers
    numbers = [1, 2, 3]
        # Select one random number
    random_number = random.choice(numbers)
    if random_number==1:
            computer_choose='s'
    elif random_number==2:
            computer_choose='r'
    else:
            computer_choose='p'
    validate_data(user_input,computer_choose)
    return "Game is over!!!"
def validate_data(user_type,computer_type):
    if user_type in ('s','r','p'):
         start_the_game(user_type,computer_type)
    else:
        print("Wrong input!!! Please choose s,r or p\n")

def start_the_game(user_type,computer_type):
    result=""
    if user_type == computer_type:
        print(f"Game will start again as you choose same option!!!")
        user_input = input('Please choose s for scissor, r for rock and p for paper\n')
        validate_data(user_input,computer_type)
    else:
        if user_type=='r' and computer_type=='s':
            result = "Congrats!!!you won as you choose Rock and computer choosen scissor"
        elif user_type=='p' and computer_type=='r':
            result = "Congrats!!!you won as you choose paper and computer choosen rock"
        elif user_type=='s' and computer_type=='p':
            result = "Congrats!!!you won as you choose scissor  and computer choosen paper"
        else:
            result = f"You lose  the game as you choosen {user_type} and computer choosen {computer_type}"
    print(result)
if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5000)
