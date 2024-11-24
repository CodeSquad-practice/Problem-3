import random

def makeRandomCardArray():      
    cardArr=[i for i in range(1,12) for _ in range(4)]
    for _ in range(8):
        cardArr.append(11)

    for i in range(len(cardArr)-1,-1,-1):
        randnum=random.randint(0,i)
        cardArr[i],cardArr[randnum]=cardArr[randnum],cardArr[i]

    return cardArr

# def printRecord(win,draw,lose):
#     if draw==0:
#         print(f'현재전적 : {win}승 {lose}패')
#     else:
#         print(f'현재전적 : {win}승 {draw}무 {lose}패')

# def isPlayingAgain():
#     while True:
#         print('한 게임 더 하시겠습니까? (Y/N)',end=' ')
#         order = input()
#         if order == 'Y' or order == 'y':
#             return True
#         elif order =='N' or order =='n':
#             return False
#         else: 
#             print('잘못 입력하셨습니다.')
    
# def printPlayerDealerCards(playerCards,dealerCards):
#     print('YOU   : ',end='')
#     for card in playerCards:
#         print(f'[{card:2}]',end=' ')
#     print()
#     print('Dealer: ',end='')
#     for card in dealerCards:
#         print(f'[{card:2}]',end=' ')
#     print()

def bettingMoney(money):
    while True:
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

def main():
    money=1000
    # betMoney=bettingMoney(money)
    deck=makeRandomCardArray()
    playerHand=[]
    playerTurn(deck,playerHand)


#     turn,win,lose,draw=0,0,0,0
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