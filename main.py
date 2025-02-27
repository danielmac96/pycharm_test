def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Dan')

print('wow a successful commit')

print("my efmfe")

print("another commit")

def print_my_text(text, repeat=1):
    for _ in range(repeat):
        print(text)

print_my_text('Hello, world!', 6)

#function to give me a random number between 1 and 6 called dice_roll
import random

def dice_roll():
    return random.randint(1, 6)

print(dice_roll())