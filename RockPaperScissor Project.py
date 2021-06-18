import random
game_list=['Rock','Paper','Scissor']
computer=0
user=0
c=0
p=0

while(True):
    user=input("Enter Rock, Paper, Scissor or Quit : ")
    computer=random.choice(game_list)
    print()
    print()
    
    if(user=="Quit"):
        break
    
    elif(user==computer):
        print("Tie")
        
    elif(user=='Rock'):
        if(computer=='Paper'):
            c+=1
            print("Computer Won!")
        else:
            p+=1
            print("Player Won!")

        
    elif(user=='Paper'):
        if(computer=='Scissor'):
            c+=1
            print("Computer Won!")
        else:
            p+=1
            print("Player Won!")

            
    elif(user=='Scissor'):
        if(computer=='Rock'):
            c+=1
            print("Computer Won!")
        else:
            p+=1
            print("Player Won!")
    else:
        print("Incorrect Input")

    print()
    print("Player : ",user)
    print("Computer : ",computer)
    print()
    print("Computer : ",c,"Player : ",p)
    print()
    
