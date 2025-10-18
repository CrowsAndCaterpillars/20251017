import csv
import random
import espeakng
import subprocess
import os

try:
    text_to_speak = "Hello, my big bao baby boy. Let's start..."
    subprocess.run(["espeak-ng", text_to_speak], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    print("espeak-ng command executed silently (using DEVNULL).")
except FileNotFoundError:
    print("espeak-ng command not found. Please ensure it's installed and in your PATH.")
except subprocess.CalledProcessError as e:
    print(f"Error executing espeak-ng: {e}")
with open('/home/kevin/tester/answers/vocab_grade_3.csv', 'r', newline='') as file:
    filereader=csv.reader(file)
    word_list=[]    
    wordlist_index=int(0)
    for row in filereader:
        first_item=row[0]
        if isinstance(first_item, str):
            wordlist_index=wordlist_index+1
            word_list.append(first_item)
    correctindex=int(0)
    wrongindex=int(0)
    askedindex=int(0)
    for ii in range(wordlist_index):
        current_question_index=random.randint(0,wordlist_index)
        askedindex=askedindex+1

        saythis="Spell the word "+word_list[current_question_index]
        subprocess.run(["espeak-ng","-v","en-us","-s",str(100),saythis], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)  
        subprocess.run(["espeak-ng","-v","en-us","-s",str(85),word_list[current_question_index]], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

        print("")
        user_answer=input("Answer: ")
        if word_list[current_question_index].lower()==user_answer.lower():
            correctindex=correctindex+1
            print("++++++++++++++++++++++")
            print("RIGHT! RIGHT! RIGHT!!!")
            print("")
        else:
            wrongindex=wrongindex+1
            print("... oh no dear...")
            print("The answer was: "+word_list[current_question_index])
            print("")
        if input("More? y/n: ").lower()=="y":
            continue
        else:
            break

print("")
print("Results:")
print("--------")
print(str(correctindex) + " correct out of " + str(askedindex) + " asked. " + str(wrongindex) + " wrong.")
print("Total word list length if all words were asked: " + str(wordlist_index))
    

