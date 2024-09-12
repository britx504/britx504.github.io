import random

if __name__ == '__main__':
    low = 1
    high = 100
    num = random.randint(low, high)
    response = None

    print('Please think of a number between 1-100 and I will guess your number')

    while response != "yes":
        response = input(f'Is your number {num}? (higher, lower, yes)')

        if response == "lower":
            high = num
        elif response == "higher":
            low = num
        elif response != "yes":
            print(f'{response} is not a valid response')

        num = (high + low) // 2
