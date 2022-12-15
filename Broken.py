import random

numbers1 = [1,2,3,4]
numbers2 = [1,2,3,5]
X = numbers1 = random.choice(numbers1)
Y = numbers2 = random.choice(numbers2)
Z = int(numbers1) + int(numbers2)

# note to self use int rather than str
#print(Z)
print("Welcome to zeuslink")

MainMenu = input('Press 1 to login:')

Quest1 = 'what does'
Quest2 = 'equal to:'
Space1 = " "
mid = str(X) + "+" + str(Y)
if MainMenu == '1':
    print(Quest1  + Space1 + Space1 + mid  + Quest2)
    Answer = input()
    if Answer == int(Z):
        print("Mined a block")
    else:
        print("error")


