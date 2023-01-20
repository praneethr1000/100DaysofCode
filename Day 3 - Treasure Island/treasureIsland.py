print("Welcome to Treasure Island. \nYour mission is to find the treasure. ")
roadDirection = input('You are at a cross road. Where do you want to go? Type "left" or "right"')
if roadDirection == 'left':
    desicion = input('You came to a lake. There is an island in the middle of the lake. Type "wait" to wait for the boat. Type "swim" to swim across.')
    if desicion == 'wait':
        color = input('You arrived at the Island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?')
        if color == 'yellow':
            print("You Win!")
        else:
            print("You entered a room of beasts. Game Over")
    else:
        print("Game Over.")
else:
    print("Game Over.")