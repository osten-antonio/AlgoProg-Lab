import random
sel_num=random.randint(1,101)
while True:
    user_input=int(input())
    if(user_input<sel_num):print("Higher")
    elif(user_input>sel_num):print("Lower")
    else:
        print("Correct")
        break