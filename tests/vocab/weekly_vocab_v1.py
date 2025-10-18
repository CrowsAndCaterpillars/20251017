import csv
import random

########################
### change this weekly
word_list=["puppy","carry","lady","dry","marry","penny","study","butterfly","bunny","hurry","along","put"]    
#             1          2  3         4  5        6       7        8          9        10     11      12
########################

# get ready
num_words = len(word_list)
correctindex=int(0)
wrongindex=int(0)
askedindex=int(0)
max_correct_words = num_words
correct_list_default_value="not asked"
correct_list=[correct_list_default_value] * num_words
correct_words = 0

# the question user loop
while True:
#for current_question_index in range(num_words):    
    random_index = 0
    while True:
        random_index = random.randint(0,num_words - 1)
        if correct_list[random_index] == "right":
            continue
        else:
            break
    saythis="Index: "+str(random_index) + " Spell the word           "+word_list[random_index]
    print(saythis)
    user_answer=input("Answer: ")
    if word_list[random_index].lower()==user_answer.lower():
        correctindex=correctindex+1
        print("++++++++++++++++++++++")
        print("RIGHT! RIGHT! RIIIIIGHT!!!")
        correct_words+=1
        correct_list[random_index] = "right"
    else:
        wrongindex=wrongindex+1
        print("............... oh no dear...")
        print("The answer was: "+word_list[random_index])
        correct_list[random_index] = "wrong"
    if correct_words < max_correct_words: 
        reply=input("correct_words="+str(correct_words)+"  More? y/n/[enter]: ").lower()
        if reply=="":
            continue
        elif reply=="y":
            continue
        else:
            # user tired of this
            break
    else:
        # user got them all correct
        break

# summary
print("")
print("Results:")
print("--------")
print(str(correctindex) + " correct out of " + str(correctindex + wrongindex) + " asked. " + str(wrongindex) + " wrong.")
print("Total word list length if all words were asked: " + str(num_words))
print(word_list)
print(correct_list)
