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
        
    
    
    
    
