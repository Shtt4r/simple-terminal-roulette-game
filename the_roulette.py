import random

import winsound

money = 100
print("-----------------------------------------")
print("simple terminal roulette game (strgv1.2)")
print("-----------------------------------------")
print("type red/black to bet on a colour")
print("-----------------------------------------")

valid = ["red", "black"]
while money > 0:
 print("--------------------")
 ask = input("black or red:").lower()
 print("--------------------")
 if ask not in valid:
    print("-----------------------")
    print("! not inside red/black")
    print("-----------------------")
    winsound.PlaySound("sound//invalid.wav", winsound.SND_FILENAME)
    continue
 print("--------------------")
 print(f"you have $:{money}")
 print("--------------------")
 try:
  bet = int(input("how much to bet:"))
  print("--------------------")
  if bet > money:
    print("! Thats... too much")
    winsound.PlaySound("sound//invalid.wav", winsound.SND_FILENAME)
    continue
 except ValueError:
    print("--------------------")
    print("! trying to break the game huh?")
    winsound.PlaySound("sound//invalid.wav", winsound.SND_FILENAME)
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

     if money == 0:
        print("----")
        print("debt")
        print("----")
        winsound.PlaySound("sound//invalid.wav", winsound.SND_FILENAME)
        break
