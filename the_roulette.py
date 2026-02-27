import random

money = 100
## Reach 3193894 to win, goodluck
while money < 3193894:
 ask = input("black or red:")

 print(f"you have $:{money}")
 try:
  bet = int(input("how much to bet:"))
  if bet > money:
    continue
 except ValueError:
    print("trying to break the game huh?")
    continue


 roll = random.randint(0, 1)

 if roll == 0:
       roll = "black"

 else:
     roll = "red"

 if ask == roll:

     money = money + bet
     print(f"win +${bet} total:$:{money}") 
 else: 
     
     money = money - bet
     print(f"lose -${bet} total:$:{money}")

