def gameengineandlives():
    """Return lives left and run game engine."""
    global attempt
    a = random.randint(0, randintend)
    for i in range(attempt + 1):
        try:
            user_input = int(input("Enter Number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if user_input == a:
            print('You won')
            break
        else:
            print(f'Try again! {attempt} attempts left.')
            attempt -= 1
