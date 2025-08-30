import random

def toss_coin():
    result = random.choice(['Heads', 'Tails'])
    print(f"The coin landed on: {result}")

# Run the simulator
toss_coin()
