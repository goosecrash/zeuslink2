import random

numbers1 = [1, 2, 3, 4,5,6]
numbers2 = [1, 2, 3, 4,5,6]
X = random.choice(numbers1)
Y = random.choice(numbers2)
Z = X + Y
Balance = 0
# note to self use int rather than str
# print(Z)
print("Welcome to zeuslink")

MainMenu = input('Press 1 to login:')

running = True

def main():
    numbers1 = [1, 2, 3, 4, 5, 6]
    numbers2 = [1, 2, 3, 4, 5, 6]
    X = random.choice(numbers1)
    Y = random.choice(numbers2)
    Z = X + Y
    Balance = 0
    Quest1 = 'what does'
    Quest2 = 'equal to:'
    Space1 = " "
    mid = str(X) + "+" + str(Y)
    if MainMenu == '1':
        print(Quest1  + Space1 + mid + Space1 + Quest2)
        Answer = int(input())  # convert user input to integer
        if Answer == Z:  # compare Answer to Z directly
            print("Mined a block")
            print(f'Your balance is: ${Balance + 1:.0f}')
        else:
            print("error")

while running == True:
    main()
