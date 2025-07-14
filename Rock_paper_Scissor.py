import random
while True:
    try:
            print("Choose: 1 for Rock, 2 for paper, 3 for Scissors")
            user = int(input("Enter a number: "))
            comp = random.randint(1,3)
            rock = 1
            paper = 2 
            scissor = 3

            choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
            print(f"You chose: {choices[user]}")
            print(f"Computer chose: {choices[comp]}")


            if user == comp:
                print("Tie")

            elif user == 1 and comp == 3 or user == 2 and comp == 1 or user == 3 and comp == 2:
                print("User wins",choices[user])
            else:
                print("Computer Wins",choices[comp])
            playagain = input("Enter yes if you want to playagain and No to exit:").lower()
            if playagain not in ["yes","y"]:
                 print("Thanks for playing")
                 break

    except ValueError:
        print("Write number btw 1-3")
    except:
        print("Choose number btw 1-3")