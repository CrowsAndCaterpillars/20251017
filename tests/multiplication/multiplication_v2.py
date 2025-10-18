###
# v2 shows the user's progress at filling up a 10x10 multipication table as they get answers right.
### todo: don't ask the same question twice if they got it right

import random

print("Welcome, Ocean.")
print("You already know your Dad is on your team.")
print("")

max_rows = 10
max_cols = 10
big_chart_divider = "@"
little_chart_divider = "~"

row_location = 0
col_location = 1
answer_location = 2

matrix = []
for rowindex in range(1,max_rows+1):
    for colindex in range(1,max_cols+1):
        smalllist = [rowindex, colindex, "???"]
        matrix.append(smalllist)


# from this we learned pos 99 is 10x10, so in position, tens digit plus one is x and ones digit plus one is y
''' make this a matrix view not a list
print("your answer matrix so far")
print("column header")
print(big_chart_divider * ( max_rows * 3 ) )
uamindex=0
for rowindex in range(1,max_rows+1):
    if matrix[ uamindex ][row_location] == rowindex:
        print(matrix[ uamindex])
    print(uamindex)
    uamindex+=1
    print(uamindex)
'''
'''
print(str(rowindex)+big_chart_divider)
for colindex in range(1,max_cols+1):
    print(str(matrix[rowindex-1,colindex-1,answer_location])+little_chart_divider)
'''
while True:
    first_operand = random.randint(1,max_rows)
    second_operand = random.randint(1,max_cols)
    actual_answer = first_operand * second_operand
    position = ((first_operand-1)*10) + ((second_operand-1)*1) 
    matrix_answer = matrix[position][answer_location]
    if str(matrix_answer) == "???":
        pass
    else:
        # start back at the top. a brute force way of getting only unanswered questions posed.
        continue
       
    #user_answer = input(str(first_operand)+" x "+str(second_operand)+" = ")
    user_answer = input(str(first_operand)+" x "+str(second_operand)+" = ")

    if user_answer == "":
        # this prevents the program erroring out if user accidently hits enter with nothing at all
        continue
    elif int(user_answer) == actual_answer:
        print("RIGHT RIGHT RIGHT !!!!")
        position = ((first_operand-1)*10) + ((second_operand-1)*1) 
        #print("position = "+str(position))
        matrix[position][answer_location] = user_answer 
    else:
        print("...oh no dear...")
        print("The right answer was "+str(actual_answer))

    myinput = input("See your progress in the multiplication table, and do another? type y Want to have no more? Type n: ")
    if myinput == "":
        # this prevents the program erroring out if user accidently hits enter with nothing at all
        continue
    elif myinput == "y":
        for pos in range(0,max_rows*max_cols):
            printpos = False
            print( ("pos: "+str(pos) if printpos else "") + " matrix: "+ str(matrix[pos][row_location])+" x "+str(matrix[pos][col_location])+" = "+str(matrix[pos][answer_location]))
    # from this we learned pos 99 is 10x10, so in position, tens digit plus one is x and ones digit plus one is y
    else:
        break

print("")
print("Value yourself not for what you do, but just because you are. And still do as well as you can, too.")
