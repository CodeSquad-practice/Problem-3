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

