'''
1 = Stone 
2 = Paper
3 = Scissors
'''
while True:

    def opt(user,comp):
        if  (user == comp):
            print("\n \tIt's a Tie")
        elif(user == 1 and comp == 2):
            print("\n \tYou Lose")
        elif(user == 1 and comp == 3):
            print("\n \tCongrats! You Win 🎉")
        elif(user == 2 and comp == 3):
            print("\n \tYou Lose")
        elif(user == 2 and comp == 1):
            print("\n \tCongrats! You Win 🎉")
        elif(user == 3 and comp == 1):
            print("\n \tYou Lose")
        elif(user == 3 and comp == 2):
            print("\n \tCongrats! You Win 🎉")

    def wor(user):
        if(1>user or user>3):
            return(wor(int(input("Invalid choice\nEnter a valid option 1 , 2 , or 3 : "))))
        return user


    import random

    computer = random.randint(1,3)

    print("\nYou are playing against a bot \nPlease enter your choise")
    print("\nPress 1 for Stone\nPress 2 for Paper\nPress 3 for Scissors\n")

    user = int(input("Enter your choise : "))

    user = (wor(user))

    guess = { 1:"Stone ✊",2:"Paper ✋",3:"Scissors ✌️"}

    choise_1 = guess[user]

    choise_2 = guess[computer]

    (opt(user,computer))

    print(f"\nYou chouse {choise_1} and the computer chouse {choise_2}")

    option_to_play = input("\nDo you want to play again ? (Yes/No) ").lower()

    if(option_to_play == "no"):
        print("OK")
        
        break

