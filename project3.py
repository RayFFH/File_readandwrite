import random


List_1 = ["What is your age?\n",
"When were you born?\n",
"What is your mothers name?\n",
"What is your favourite sport?\n",
"What is your favourite colour?\n"]

file = open("Questions.txt","w")
file.writelines(List_1)
file.close()

with open("Questions.txt") as my_file:
    array = my_file.readlines()

random.shuffle(array)
count = 0
array2 = []
for line in array:
    ans = input("Question{}: {}".format(count, line.strip()))
    array2.append(ans)
    count = count + 1

count = 0
for line in array2:
    print("Answer{} : {}".format(count, line.strip()))
    count = count + 1
