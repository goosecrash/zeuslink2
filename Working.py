import random

# Declare variables and functions outside of the while loop to avoid
# recreating them every iteration
numbers1 = [1, 2, 3, 4,5,6]
numbers2 = [1, 2, 3, 4,5,6]
balance = 0

def main():
    # Choose X and Y outside of the if statement to avoid
    # selecting new random numbers unnecessarily
    X = random.choice(numbers1)
    Y = random.choice(numbers2)
    Z = X + Y
    Quest1 = 'what does'
    Quest2 = 'equal to:'
    Space1 = " "
    mid = str(X) + "+" + str(Y)
    if MainMenu == '1':
        print(Quest1  + Space1 + mid + Space1 + Quest2)
        Answer = int(input())  # convert user input to integer
        if Answer == Z:  # compare Answer to Z directly
            print("Mined a block")
            global balance
            balance += 5
            print(f'Your balance is: ${balance:.0f}')
        else:
            print("error")

# Print welcome message outside of the loop
print("Welcome to zeuslink")

while True:
    MainMenu = input('Press 1 to login:')
    main()
