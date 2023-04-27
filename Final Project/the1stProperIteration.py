import random
a = random.randint(0,20)
print("Welcome to the random number guessing game. This is a game where you guess a number betwen the value of 0 and 20.")
attempt = 4
for i in range(5):
    user_input = int(input("Enter Number: "))

    if user_input == (a):
        print('You won!')
        break
    else:
        print(f'Try again! {attempt} attempts left.')
        attempt -= 1
        continue