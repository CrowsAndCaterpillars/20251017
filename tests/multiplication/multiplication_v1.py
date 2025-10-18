import random

print("Welcome, Ocean.")
print("You already know your Dad is on your team.")
print("")

while True:
    first_operand = random.randint(1,10)
    second_operand = random.randint(1,10)
    actual_answer = first_operand * second_operand

    user_answer = input(str(first_operand)+" x "+str(second_operand)+" = ")

    if int(user_answer) == actual_answer:
        print("RIGHT RIGHT RIGHT !!!!")
    else:
        print("...oh no dear...")
        print("The right answer was "+str(actual_answer))

    if input("More? y/n: ") == "y":
        continue
    else:
        break

print("")
print("Value yourself for not what you do, but because you exist -- and still do as well as you can, too.")

