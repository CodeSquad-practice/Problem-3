import random

def get_random_card():
    card=random.randint(1,12)
    return card

def main():
    card=get_random_card()
    print(card)

if __name__=='__main__':
    main()