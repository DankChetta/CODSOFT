import random
rock='''
     _______
---'    ____)
        (____)
        (____)
        (____)
---.____(___)
'''

paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---._______)
'''

scissors='''
    _______
---'   ____)____
          ______)
       _________)
        (____)
---.___(___)
'''
images=[rock, paper, scissors]
u_score=0
c_score=0
while True:
    u=int(input("Enter your choice: 0 for rock, 1 for paper, 2 for scissors, 3 for exit: "))
    if u==3:
        print("Exiting the game!")
        print(f"Final score - You: {u_score}, Computer: {c_score}")
        break
    elif u>=4 or u<0:
        print("Invalid input, you lose!")
    else:
        print("You chose:", u)
        print(images[u])
        c=random.randint(0,2)
        print("Computer chose:", c)
        print(images[c])
        if c==u:
            print("It's a draw!")
        elif (u==0 and c==2) or (u==1 and c==0) or (u==2 and c==1):
            print("You win!")
            u_score += 1
        else:
            print("You lose!")
            c_score += 1
    print(f"Your score: {u_score}, Computer's score: {c_score}")