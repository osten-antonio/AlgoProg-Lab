import random

Playing = True

score = 0
highscore=0
maxhp=100
player = {
    "HP" : 100,
    "ATK" : 10,
    "DEF" : 0,
    "INV" : [["Stone sword","Health potion"],[1,3]],
    "Equipped_item": "Stone sword"
}

swords=["Stone sword","Iron sword","Golden sword","Diamond sword"]

item_data = {
"Stone sword" : 10,
"Iron sword" : 20,
"Golden sword" : 30,
"Diamond sword" : 40,
"Health potion":25,
"Bigger health potion":50
}

monsters = {
"monster" : {
    "HP":50,
    "ATK":20,
    "Moves":["Attack"],
    "escape":60,
    "value":1,
    "drop":1
  },
"Bigger": {
    "HP":100,
    "ATK": 30,
    "Moves":["Attack","Heal"],
    "escape":50,
    "value":5,
    "drop":3
  },
"Even Bigger": {
    "HP":200,
    "ATK": 40,
    "Moves":["Attack","Heal","Buff"],
    "escape":40,
    "value":10,
    "drop":6
  },
}
def inventory():
    print(
        '''
=================
    Inventory
=================
        '''
    )
    for i in range(len(player["INV"][0])):
        print(f"{i}. {player['INV'][1][i]} x {player['INV'][0][i]}")
    print(
'''
===============
    Actions
===============
1) Use item
Enter any key to leave
'''
    )
    invaction=input("Input ")
    if invaction == "1":
        selitem = int(input("Which item?"))
        if player['INV'][0][selitem] in swords:
            player["Equipped_item"]= player['INV'][0][selitem]
        else:
            player["HP"]+=item_data[player['INV'][0][selitem]]
            player["INV"][1][selitem]-=1
            if player["HP"]>maxhp:player["HP"]=maxhp
def fight(monsterr):
    global score
    print()
    escape=False
    if monsterr=="monster":monsters[monsterr]["HP"]=50
    if monsterr == "Bigger": monsters[monsterr]["HP"] = 100
    if monsterr == "Even Bigger": monsters[monsterr]["HP"] = 200
    name_dict={"monster":"Small monster","Bigger":"Bigger monster","Even Bigger":"Even bigger monster"}
    while player["HP"] > 0 and monsters[monsterr]["HP"] > 0 and escape==False:
        print(
            '''
            ===============
                Actions
            ===============
            1. Attack
            2. Inventory
            3. Run
            '''
        )
        print(f"Your HP: {player['HP']}          |          {name_dict[monsterr]} HP: {monsters[monsterr]['HP']}")
        fight_input = input()
        if fight_input == "1":
            monsters[monsterr]["HP"] -= (item_data[player["Equipped_item"]] + (player["ATK"] / 2))
        elif fight_input == "2":
            inventory()
        elif fight_input== "3":
            chancerun=random.randint(0,99)
            if chancerun < monsters[monsterr]["escape"]:
                print("Successfuly escaped!")
                escape=True

        if monsters[monsterr]["HP"] > 0:
            match monsterr:
                case "monster":
                    print("Goblin attacked")
                    player["HP"] -= (monsters[monsterr]["ATK"]+int(player["DEF"]/1000))
                case "Bigger":
                    ataks=random.randint(0,99)
                    if ataks < 70:
                        print("Bigger monster attacks")
                        player["HP"] -= (monsters[monsterr]["ATK"] + int(player["DEF"] / 1000))
                    elif ataks < 99:
                        print("Bigger monster buffs")
                        monsters[monsterr]["ATK"] += 5
                case "Even Bigger":
                    ataks = random.randint(0, 99)
                    if ataks < 60:
                        print("Even bigger monster attacks")
                        player["HP"] -= (monsters[monsterr]["ATK"] + int(player["DEF"] / 1000))
                    elif ataks < 20:
                        print("Even bigger monster buffs")
                        monsters[monsterr]["ATK"] += 10
                    else:
                        print("Bigger monster heals")
                        monsters[monsterr]["HP"] += 30
        else:
            print(f"{name_dict[monsterr]} died")
            print(f"Added {monsters[monsterr]['value']} score\n")
            score += monsters[monsterr]["value"]
            for i in range(monsters[monsterr]["drop"]):
                get_item()
        if monsterr == "Goblin": monsters[monsterr]["HP"] = 50
        if monsterr == "Bigger": monsters[monsterr]["HP"] = 100
        if monsterr == "Even Bigger": monsters[monsterr]["HP"] = 200
def receives(item):
    global maxhp
    match item:
        case "ATK":
            player["ATK"] += 10
            print("You got an ATK upgrade!")
            return "ATK"
        case "HP":
            player["HP"] += 20
            maxhp+=20
            print("You got a HP upgrade!")
            return "HP"
        case "DEF":
            player["DEF"] += 5
            print("You got a DEF upgrade!")
            return ("DEF")
        case _:
            print(f"You got {item}!")
            return item
def get_item():
    chance = random.randint(0, 99)
    if chance < 8:
        received = receives("ATK")
    elif chance < 16:
        received = receives("HP")
    elif chance < 50:
        received = receives("Health potion")
    elif chance < 70:
        received = receives("Bigger health potion")
    elif chance < 90:
        received = receives("Golden sword")
    elif chance < 95:
        received = receives("Diamond sword")
    elif chance < 100:
        received = receives("DEF")
    print(player["INV"][0])
    if received in player["INV"][0]:
        player["INV"][1][player["INV"][0].index(received)] += 1
    elif not (received in ("ATK", "HP", "DEF")):
        player["INV"][0].append(received)
        player["INV"][1].append(1)
        print(player["INV"][0])
        print(player["INV"][1])
while Playing == True:
    print(f'''
===============
    Actions
===============
1) Explore
2) Inventory
3) See stats
4) Save
5) Load
6) Quit
    
Current score: {score}
High score: {highscore}
    ''')
    action = input("Input ")
    match action:
        case '1':
            chance=random.randint(0,99)
            if chance < 30:
                get_item()
            elif chance<70:
                chance = random.randint(0, 99)
                if chance < 50:
                    print(f"You encountered a smol monster")
                    fight("monster")
                    if player["HP"] <= 0:
                        print("You died")
                        player = {
                            "HP": 100,
                            "ATK": 10,
                            "DEF": 10,
                            "INV": [["Stone sword", "Health potion"],[1, 3]],
                            "Equipped_item": "Stone sword"
                        }
                        print(f"Your score: {score}")
                        score=0
                        if score>highscore:
                            print("New highscore!")
                            highscore=score

                elif chance < 80:
                    print(f"You encountered a bigger monster")
                    fight("Bigger")
                    if player["HP"] <= 0:
                        print("You died")
                        player = {
                            "HP": 100,
                            "ATK": 10,
                            "DEF": 10,
                            "INV": [["Stone sword", "Health potion"],[1, 3]],
                            "Equipped_item": "Stone sword"
                        }
                        print(f"Your score: {score}")
                        score = 0
                        if score>highscore:
                            print("New highscore!")
                            highscore=score
                elif chance < 100:
                    print(f"You encountered an even bigger monster")
                    fight("Even Bigger")
                    if player["HP"] <= 0:
                        print("You died")
                        player = {
                            "HP": 100,
                            "ATK": 10,
                            "DEF": 10,
                            "INV": [["Stone sword", "Health potion"], [1, 3]],
                            "Equipped_item": "Stone sword"
                        }
                        print(f"Your score: {score}")
                        score = 0
                        if score>highscore:
                            print("New highscore!")
                            highscore=score
            else:
                print("\nYou found nothing")
        case '2': inventory()
        case '3':
            print(f"\nHP: {player['HP']}\nATK: {player['ATK']}\nDEF: {player['DEF']}\nEquipped item: {player['Equipped_item']}")
        case '4':
            data1 = f"{player['HP']} {player['ATK']} {player['DEF']} {player['Equipped_item']} {highscore} {score} {maxhp}"
            data2=""
            data3=""
            for i in range(len(player['INV'][0])):
                data2+=player['INV'][0][i]+"|"
                data3 +=str(player['INV'][1][i]) + "|"
            with open("savefile.txt", "w") as file:
                file.write(data1)
                file.close()
            with open("savefile.txt", "a") as file:
                file.write("\n")
                file.write(data2)
                file.write("\n")
                file.write(data3)
                file.close()
            print("Saved successfully!")
        case '5':
            with open("savefile.txt","r") as file:
                data=file.readlines()
                file.close()
            count = 0
            for i in data:
                temp=i
                if count == 0:
                    temp=temp.split()
                    player['HP'],player['ATK'],player['DEF'],player['Equipped_item'],highscore,score,maxhp=int(temp[0]),int(temp[1]),int(temp[2]),temp[3],int(temp[4]),int(temp[5]),int(temp[6])
                elif count== 1:
                    temp = i.split("|")
                    player['INV'][0]=temp
                else:
                    temp = i[0:len(i)-1].split("|")
                    player['INV'][1] = temp
                count+=1
            print(player['INV'][1])
            for i in range(len(player['INV'][1])):
                player['INV'][1][i]=int(player['INV'][1][i])
        case '6':
            Playing=False
        case _:
            print("Invalid input")