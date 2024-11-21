import random

def get_random_card():
    card=random.randint(1,12)
    return card

def main():
    turn=0
    win=0
    lose=0
    print('간단 카드게임을 시작합니다.')
    print()
    while True:
        turn +=1
        print(f'Game {turn}')
        myCard=get_random_card()
        dealerCard=get_random_card()
        print(f'YOU   : [{myCard:2}]')
        print(f'DEALER: [{dealerCard:2}]')
        break

if __name__=='__main__':
    main()