from random import choice
dict={'rock':0,'paper':1, 'scissors':2}
def game():
    computer=choice(list(dict.keys()))
    return computer

def main():
    while True:
        user_input = (input("Rock, paper or scissors? ").lower())
        if user_input=="quit": 
            break   
        computer=game()
        if  user_input not in dict.keys():
            print("Invalid input! Please enter either 'rock', 'paper' or 'scissors'")
            return
        elif user_input=="rock" and computer=="paper":
            print(f"You chose {user_input} while the computer chose {computer}. You lost!")
        elif user_input=="rock" and computer=="scissors":
            print(f"You chose  {user_input} while the computer chose {computer}. You won!")
        
        elif user_input=="paper" and computer=="scissors":
            print(f"You chose {user_input} while the computer chose {computer}. You lost!")
        elif user_input=="paper" and computer=="rock":
            print(f"You chose  {user_input} while the computer chose {computer}. You won!")

        elif user_input=="scissors" and computer=="rock":
            print(f"You chose  {user_input} while the computer chose {computer}. You lost!")
        elif user_input=="scissors" and computer=="paper":
            print(f"You chose  {user_input} while the computer chose  {computer}. You won!")
        
        else:
            print("It's a tie!")
    

main()


