# Problem-3
## 랜덤으로 카드 뽑기 
단순히 randint 함수로 쉽게 구현할 수 있었다.  
카드를 뽑아도 확률이 달라지지 않기 때문에 플레이어도, 딜러도 이 함수로 카드를 뽑는다.

## 카드 뽑고 배열에 추가하기
```python
myCards.append(getRandomCard())
dealerCards.append(getRandomCard())
printPlayerDealerCards(myCards,dealerCards)
```
위처럼 getRandomCard라는 랜덤으로 카드를 뽑는 함수로, 카드를 뽑아 자신과 딜러의 리스트에 추가하도록 했다.  
그리고 printPlayerDealerCards 메서드는 리스트의 모든 카드들을 출력하는 함수이다. 

## 카드비교하기
```python
if myCards[-1]>dealerCards[-1]:
    win+=1
    print('당신이 이겼습니다.')
elif myCards[-1]==dealerCards[-1]:
    draw+=1
    print('비겼습니다.')
else:
    lose+=1
    print('딜러가 이겼습니다.')
```
리스트의 마지막 카드로 서로 카드를 비교한다.

## 결과 출력하기
```python
def printRecord(win,draw,lose):
    if draw==0:
        print(f'현재전적 : {win}승 {lose}패')
    else:
        print(f'현재전적 : {win}승 {draw}무 {lose}패')
```
draw가 0일 때는 무승부를 출력하지 않고, draw가 1 이상이 될 때 출력한다.

## 한판 더할지 말지 결정하기
```python
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
```
한판을 할 때마다 입력을 받아 y가 나오면 한판 더 실행하고, n이 나오면 끝낸다.  
잘못 입력할 경우 계속해서 다시 입력받는다.

## 실행결과
```
Game 1
YOU   : [ 7]
Dealer: [ 6]
당신이 이겼습니다.
현재전적 : 1승 0패
한 게임 더 하시겠습니까? (Y/N) y

Game 2
YOU   : [ 7] [ 2]
Dealer: [ 6] [ 3]
딜러가 이겼습니다.
현재전적 : 1승 1패
한 게임 더 하시겠습니까? (Y/N) y

Game 3
YOU   : [ 7] [ 2] [ 6] 
Dealer: [ 6] [ 3] [ 7] 
딜러가 이겼습니다.     
현재전적 : 1승 2패     
한 게임 더 하시겠습니까? (Y/N) y

Game 4
YOU   : [ 7] [ 2] [ 6] [10]
Dealer: [ 6] [ 3] [ 7] [ 3]
당신이 이겼습니다.
현재전적 : 2승 2패
한 게임 더 하시겠습니까? (Y/N) n
게임을 종료합니다.
플레이해주셔서 감사합니다.
```

# Problem-3 2단계

## 랜덤 덱 만들기
```python
def makeRandomCardArray():      
    cardArr=[i for i in range(1,12) for _ in range(4)]
    for _ in range(8):
        cardArr.append(11)

    for i in range(len(cardArr)-1,-1,-1):
        randnum=random.randint(0,i)
        cardArr[i],cardArr[randnum]=cardArr[randnum],cardArr[i]

    return cardArr
```
우선 덱을 만드는 함수는 Fisher-Yates 알고리즘을 이용하여 만들었다.   
카드덱에 있는 모든 숫자들을 순서대로 넣고, 위 알고리즘을 이용하여 섞어주었다. 

## 돈 베팅하기
```python
def bettingMoney(money,deck):
    while True:
        print("얼마를 거시겠습니까?",end=' ')
        betMoney=input()
        if betMoney=="codesquad":
            cheat(deck)
            continue
        if not betMoney.isdigit():
            print('잘못 입력하셨습니다.')
            continue
        betMoney=int(betMoney)
        if betMoney>money or betMoney==0 or betMoney%100!=0:
            print("잘못 입력하셨습니다.")
        else:
            return betMoney
```
100원 단위로 돈을 입력받는 함수이다. 추후 설명할 치트도 추가했다.  
치트 코드를 입력받으면 치트 함수를 실행한다.

## 메인함수
```python
def main():
    money=1000
    turn=0
    deck=makeRandomCardArray()
    print("간단 카드게임을 시작합니다.")
    print("현재 재산:",money)

    while True:
        if len(deck)<=10:
            deck=makeRandomCardArray()
        betMoney=bettingMoney(money,deck)
        print()
        turn+=1
        print("Game",turn)
        winner=playGame(deck)
        money=gameResult(winner,money,betMoney)
        
        # 한 게임이 종료되면 플레이어는 다시 게임을 할지 여부를 결정할 수 있다.
        if money == 0: 
            break
        if not isPlayingAgain(deck):
            break
```
메인 함수는 다음과 같다.
덱의 장수가 10장 미만이면 다시 덱을 만들도록 하여 기타 규칙을 만족했다.  
플레이어가 게임을 종료할 때 까지 playGame 함수를 실행하여 게임을 계속 진행한다.

## 게임 시작 
```python
def playGame(deck):
    playerHand=[]
    while True:
        playerTurn(deck,playerHand)
        sumCards=printSum(playerHand)
        if sumCards>21:
            # 플레이어가 받은 카드의 합이 22 이상이면 무조건 플레이어의 패배이다. 이 때 딜러는 카드를 받지 않는다.
            return "D"
        if not getMoreCard(deck):
            # 플레이어가 카드를 더 이상 안 받기로 결정한 시점에서 딜러도 카드를 받는다.
            dealerSum=dealerTurn(deck)
            winner=findWinner(sumCards,dealerSum)
            return winner
```
게임은 플레이어 턴과 딜러턴으로 나뉜다.   
각각의 턴을 실행한 후, 서로의 결과를 비교해 승자를 return 하게된다.
여기서 승자가 어떻게 표현되는지는 findWinner 함수에서 자세히 나온다.
```python
def getMoreCard(deck):
    while True:
        print('카드를 더 받겠습니까? (Y/N)',end=' ')
        order = input()
        if order=="codesquad":
            cheat(deck)
            continue
        if order == 'Y' or order == 'y':
            return True
        elif order =='N' or order =='n':
            return False
        else: 
            print('잘못 입력하셨습니다.')
```
getMoreCards 함수는 y혹은 n을 받아서 카드를 더 받을지 결정하는 함수이다.
카드를 더 받지 않기로 결정하면 딜러턴이 진행된다. 

## 플레이어 턴
```python
#플레이어 턴
def playerTurn(deck,playerHand):
    playerHand.append(deck.pop())
    print("플레이어: ",end='')
    for elem in playerHand:
        print(f'[{elem:2}]',end='')
    print()
```
deck을 인자로 받아 제일 마지막 요소를 pop해주며 player핸드에 추가한다.   
그리고는 핸드를 print 한다.

## 딜러턴
```python 
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
```
딜러턴도 플레이어턴과 비슷하게 진행되지만, 직접 카드를 더 받을지 선택하는 것이 아니라, 카드의 합이 17이상이 될 때 까지 받는다.

## 승자 찾기
```python
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
```
플레이어 카드의 합과 딜러 카드의 합을 비교해 누가 승자인지 계산하는 함수이다.   
draw 조건이 있고, 플레이어가 21로 이기면 돈을 두배로 받기 때문에 블랙잭(21)으로 이겼다는 것을 알려주는 "B"도 있다. 

``` python
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
```
그래서 winner를 받고, 그에 따라 money를 더하거나 빼준다.

## 한판 더 할지 결정
```python
def isPlayingAgain(deck):
    while True:
        print('한 게임 더 하시겠습니까? (Y/N)',end=' ')
        order = input()
        if order == "codesquad":
            cheat(deck)
            continue
        if order == 'Y' or order == 'y':
            return True
        elif order =='N' or order =='n':
            return False
        else: 
            print('잘못 입력하셨습니다.')
```
게임이 끝난 후 한판 더 할지 결정한다.

## 치트
```python
def cheat(deck):
    print("덱의 카드 ", end='')
    cnt=0
    for i in range(len(deck)-1,-1,-1):
        cnt+=1
        print(f'[{deck[i]:2}]',end='')
        if cnt==6:
            break
    print()
```
입력을 받는 모든 함수는 codesquad라는 문자열이 들어오면 치트 함수를 실행한다.
치트함수는 덱의 가장 위 6장을 보여준다.   
혹시나 덱의 장수가 6장이 되지 않을 가능성도 있는데, 그 가능성을 생각하여 단순히 리스트 인덱싱으로 처리하지 않고, for문을 통해 처리했다.
