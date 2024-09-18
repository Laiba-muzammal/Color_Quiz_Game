# Multi-question Game: A dummy KBGKC (Kaun Banega Game Ka Crorepati) style game
# Rules:
# 1. The player will be asked a series of multiple-choice questions.
# 2. For every correct answer, the player's money increases by 10,000.
# 3. If the player answers incorrectly, the game ends, and the player's current money is their final amount.
# 4. The questions will be presented in a random order every time the game starts.
# 5. The game exits immediately upon a wrong answer.


import random

print("WELCOME TO THE GAME!\n")

question=[{"Q":"What is the color of the sky? \n1.blue\n2.green\n3.yellow\n4.black","correct":"1"},
          {"Q":"What is the color of the grass? \n1.blue\n2.green\n3.yellow\n4.black","correct":"2"},
          {"Q":"What is the color of the mango? \n1.blue\n2.green\n3.yellow\n4.black","correct":"3"},
          {"Q":"What is the color of the sun? \n1.blue\n2.green\n3.yellow\n4.black","correct":"3"},
          {"Q":"What is the color of the water? \n1.blue\n2.green\n3.yellow\n4.black","correct":"1"},
          {"Q":"What is the color of the leaves? \n1.blue\n2.green\n3.yellow\n4.black","correct":"2"},
          {"Q":"What is the color of the night? \n1.blue\n2.green\n3.yellow\n4.black","correct":"4"}]
random.shuffle(question)
score=0
for i,q in enumerate (question):
    print(f"Question#0{i+1}: {q['Q']}")
    get=input()
    if(get==(q['correct'])):
        score=score+10000
        print("\nWoppie!!\nCorrect Answer!!")
        print(f"Your money is: {score}\n")
    else:
        print("\nOops!!\nWrong Answer....Better luck next time!!")
        print(f"Your total money is: {score}")
        exit()
        
    
    
    
    