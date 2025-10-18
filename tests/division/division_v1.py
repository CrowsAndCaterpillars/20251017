######
# v1: find 1 denominator of 2 randomly generated ones.
######
import random
print("Welcome, Ocean.")
print("You already know your Dad is on your team.")
print("")
while True:
    first_denominator = random.randint(2,10)
    second_denominator = random.randint(2,10)
    product = first_denominator * second_denominator
    print(str(product) + " / " + str(first_denominator) + " = what?")
    user_answer = input("Answer: ")
    if int(user_answer) == second_denominator:
        print("RIGHT RIGHT RIGHT !!!!")
    else:
        print("...oh no dear...")
        print("The right answer was "+str(second_denominator))
    more=input("More? y/n/enter: ")
    if more == "y":
        continue
    elif more=="":
        continue
    else:
        break
print("")
print("Value yourself for not what you do, but because you exist -- and still do as well as you can, too.")
