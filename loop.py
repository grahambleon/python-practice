
print("You're in a recursive loop! Enter 'e' to exit. Enter anything else to loop again!")

def loop(count):
    print(f"You've looped {count} times!\nEnter 'e' to exit. Enter anything else to loop again!")
    user_input = input()
    if user_input == 'e':
        print("Goodbye!")
    else:
        loop(count + 1)

loop(0)
