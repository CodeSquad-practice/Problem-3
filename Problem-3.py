import random

def getRandomCard():
    card=random.randint(1,12)
    return card

def printRecord(win,draw,lose):
    if draw==0:
        print(f'현재전적 : {win}승 {lose}패')
    else:
        print(f'현재전적 : {win}승 {draw}무 {lose}패')

def isPlayingAgain():
    while True:
        print('한 게임 더 하시겠습니까? (Y/N)',end=' ')
        order = input()
        if order == 'Y' or order == 'y':
            return True
        elif order =='N' or order =='n':
            return False
        else: 
            print('잘못 입력하셨습니다.')
    

def main():
    turn=0
    win=0
    lose=0
    draw=0
    print('간단 카드게임을 시작합니다.')
    print()
    while True:
        turn +=1
        print(f'Game {turn}')
        myCard=getRandomCard()
        dealerCard=getRandomCard()
        print(f'YOU   : [{myCard:2}]')
        print(f'DEALER: [{dealerCard:2}]')

        if myCard>dealerCard:
            win+=1
            print('당신이 이겼습니다.')
        elif myCard==dealerCard:
            draw+=1
            print('비겼습니다.')
        else:
            lose+=1
            print('딜러가 이겼습니다.')
        printRecord(win,draw,lose)

        isPlayingAgain()
        break

if __name__=='__main__':
    main()