import random

def makeRandomCardArray():      
    cardArr=[i for i in range(1,12) for _ in range(4)]
    for _ in range(8):
        cardArr.append(11)

    for i in range(len(cardArr)-1,-1,-1):
        randnum=random.randint(0,i)
        cardArr[i],cardArr[randnum]=cardArr[randnum],cardArr[i]

    return cardArr

def getMoreCard():
    while True:
        print('카드를 더 받겠습니까? (Y/N)',end=' ')
        order = input()
        if order == 'Y' or order == 'y':
            return True
        elif order =='N' or order =='n':
            return False
        else: 
            print('잘못 입력하셨습니다.')

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


def printSum(Hand):
    sumCards=0
    for elem in Hand:
        sumCards+=elem
    print(f"총합: {sumCards}")
    return sumCards

def bettingMoney(money):
    while True:
        print("얼마를 거시겠습니까?",end=' ')
        betMoney=int(input())
        if betMoney>money or betMoney==0 or betMoney%100!=0:
            print("잘못 입력하셨습니다.")
        else:
            return betMoney

def playerTurn(deck,playerHand):
    playerHand.append(deck.pop())
    print("플레이어: ",end='')
    for elem in playerHand:
        print(f'[{elem:2}]',end='')
    print()

def dealerTurn(deck):
    sumCards=0
    dealerHand=[]
# 딜러는 16 이하이면 무조건 카드를 받고, 17 이상이면 카드를 받지 않는다.
    while sumCards<17:        
        card=deck.pop()
        sumCards+=card
        dealerHand.append(card)
    print("딜러: ",end='')
    for elem in dealerHand:
        print(f'[{elem:2}]',end='')
    print()
    print(f"딜러의 카드 합계는 {sumCards}입니다.")
    return sumCards


def findWinner(sumCards,dealerSum):
    if dealerSum>21:
        if sumCards==21:
            return "B"
        # 딜러의 카드가 22 이상이어도 플레이어의 승리이다.
        return "P"
    if dealerSum<sumCards:
        if sumCards==21:
            return "B"
        # 플레이어의 카드 합이 딜러보다 크다면 플레이어의 승리이다.
        return "P"
    if dealerSum>sumCards: 
        # 딜러의 카드합이 더 큰 값이라면 딜러의 승리이다.
        return "D"
    # 같은 값이라면 서로 비기게 된다. 단 딜러가 21을 뽑을 경우도 딜러가 승리한다.
    if dealerSum==sumCards:
        if dealerSum==21:
            return "D"
        else:
            return "draw"

def playGame(deck):
    playerHand=[]
    while True:
        playerTurn(deck,playerHand)
        sumCards=printSum(playerHand)
        if sumCards>21:
            # 플레이어가 받은 카드의 합이 22 이상이면 무조건 플레이어의 패배이다. 이 때 딜러는 카드를 받지 않는다.
            return "D"
        if not getMoreCard():
            # 플레이어가 카드를 더 이상 안 받기로 결정한 시점에서 딜러도 카드를 받는다.
            dealerSum=dealerTurn(deck)
            winner=findWinner(sumCards,dealerSum)
            return winner
            
def gameResult(winner,money,betMoney):
    if winner=="P"or winner=="B":
        print("당신의 승리입니다.")
        if winner=="B":
            money+=betMoney
        money+=betMoney
    elif winner=="D":
        print("당신의 패배입니다.")
        money-=betMoney
    else:
        print("비겼습니다.")
    print("현재 남은 자산:",money)
    return money

def main():
    money=1000
    turn=0
    deck=makeRandomCardArray()
    print("간단 카드게임을 시작합니다.")
    print("현재 재산:",money)

    while True:
        if len(deck)<=10:
            deck=makeRandomCardArray()
        betMoney=bettingMoney(money)
        print()
        turn+=1
        print("Game",turn)
        winner=playGame(deck)
        money=gameResult(winner,money,betMoney)
        
        # 한 게임이 종료되면 플레이어는 다시 게임을 할지 여부를 결정할 수 있다.
        if money == 0: 
            break
        if not isPlayingAgain():
            break


    
#     myCards=[]
#     dealerCards=[]
#     print('간단 카드게임을 시작합니다.')
#     while True:
#         turn +=1
#         print()
#         print(f'Game {turn}')
#         myCards.append(getRandomCard())
#         dealerCards.append(getRandomCard())
#         printPlayerDealerCards(myCards,dealerCards)

#         if myCards[-1]>dealerCards[-1]:
#             win+=1
#             print('당신이 이겼습니다.')
#         elif myCards[-1]==dealerCards[-1]:
#             draw+=1
#             print('비겼습니다.')
#         else:
#             lose+=1
#             print('딜러가 이겼습니다.')
#         printRecord(win,draw,lose)

#         if not isPlayingAgain():
#             print('게임을 종료합니다.\n플레이해주셔서 감사합니다.')
#             break

if __name__=='__main__':
    main()