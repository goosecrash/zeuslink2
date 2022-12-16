import random

numbers1 = [1, 2, 3, 4,5,6]
numbers2 = [1, 2, 3, 4,5,6]
X = random.choice(numbers1)
Y = random.choice(numbers2)
Z = X + Y
balance = 0  # fix variable name
# note to self use int rather than str
# print(Z)
print("Welcome to zeuslink")

main_menu = input('Press 1 to login:')  # fix variable name

running = True

def main():
    numbers1 = [1, 2, 3, 4, 5, 6]
    numbers2 = [1, 2, 3, 4, 5, 6]
    X = random.choice(numbers1)
    Y = random.choice(numbers2)
    Z = X + Y
    Quest1 = 'what does'
    Quest2 = 'equal to:'
    Space1 = " "
    mid = str(X) + "+" + str(Y)
    if main_menu == '1':  # fix variable name
        print(Quest1  + Space1 + mid + Space1 + Quest2)
        Answer = int(input())  # convert user input to integer
        if Answer == Z:  # compare Answer to Z directly
            print("Mined a block")
            balance += 1  # update balance
            print(f'Your balance is: ${balance:.0f}')  # print balance with correct formatting
        else:
            print("error")

while running == True:
    main()
