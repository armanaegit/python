#1
"""
username = input("What is your name?")

userage = input("How old are you?")

repeatnum = int(input("How many times to repeat?"))

userage = int(userage)
for x in range(repeatnum):
    print("Hey " + username + ", You'll become 100 years old in " + str(100 - userage) + " years.")"""
    
   
#2   
"""
usernumber = int(input("Please enter an integer:"))

usernumber2 = int(input("Please enter another integer to check the division of the first number by it:"))

if usernumber % usernumber2 == 0:
    print(str(usernumber) + " is evenly divided by " + str(usernumber2) + ".")

else:
    print(str(usernumber) + " is not evenly divided by " + str(usernumber2) + ".")"""
    
   
#3   
"""
import random
my_list = []
sec_list = []
user_num = int(input("Enter a number less than 10: "))
for x in range(100):
    my_list.append(random.randrange(10))
    if my_list[x] < user_num:
        sec_list.append(my_list[x])

print(sec_list)"""



#4
"""user_num = int(input("Please enter a number: "))
divisors = []
for x in range(1, int(user_num/2)):
    if user_num % x == 0:
        divisors.append(x)
       
message = "The divisors of {0} are the following:\n {1}"
print(message.format(user_num, divisors))"""


#5
"""import random

list_1 = []
for x in range(random.randrange(803, 5009)):
    list_1.append(random.randrange(1741))

print("The first list: \n {}\n".format(list_1))

list_2 = []
for x in range(random.randrange(803, 5009)):
    list_2.append(random.randrange(1741))

print("The second list: \n {}\n".format(list_2))

common_elements = []

for x in list_1:
        if x in common_elements:
            break
        for y in list_2:
            if x == y:
                common_elements.append(x)
                break
                
print("Common_elements of the above lists:\n{}\n".format(common_elements))"""


#6-1
"""user_word = input("Enter a word: ")

is_palindrom = True

for x in range(len(user_word)):
    if user_word[x] != user_word[len(user_word) - x - 1]:
        is_palindrom = False
    
if is_palindrom:
    print(user_word + " is a palindrome!\n")
else:
    print(user_word + " is not a palindrome!\n")"""


#6-2
"""user_word = input("Enter a word: ")

if user_word == user_word[len(user_word)-1::-1]:
    print(user_word + " is a palindrome!\n")
else:
    print(user_word + " is not a palindrome!\n")
   """


#7 List comprehension
"""a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [x for x in a if x % 2 == 0]
print(b)"""



#8 Rock-Paper-Scissors
"""print("Welcome to Rock-Paper-Schissors game!\nIn order to quit the game, enter the command 'quit'.")
while True:
    player1_play = input("Player1! Please enter your move (rock, paper, scissors):")
    if player1_play == "quit":
        break
    player2_play = input("Player2! Please enter your move (rock, paper, scissors):")
    if player2_play == "quit":
        break
    if player1_play == player2_play:
        print("It's a DRAW :)\n")
    elif player1_play == 'rock':
        if player2_play == 'paper':
            print("Player2 WINS :)\n")
        else:
            print("Player1 WINS :)\n")
    elif player1_play == 'paper':
        if player2_play == 'rock':
            print("Player1 WINS :)\n")
        else:
            print("Player2 WINS :)\n")
    elif player1_play == 'scissors':
        if player2_play == 'rock':
            print("Player2 WINS :)\n")
        else:
            print("Player1 WINS :)\n")
    else:
        print("Wrong input! Only 'rock', 'papers' and 'scissors' are accepted.")

print("GoOdByE :)")"""



#9 Guess the number
import random
print("Hello, to exit the program type 'exit' and press Enter.\n")

alltries = trueguesses = 0

while True:
    randnum = random.randint(1, 9)
    usernum = input("Guess a number between 0 and 10: ")
    if usernum == 'exit':
        break
    elif int(usernum) == randnum:
        print("You guessed correctly!\n")
        trueguesses += 1
    else:
        print("You were wrong! The correct number was {}.\n".format(randnum))
    alltries += 1


print("You tried for {} times and you were correct in {} of them!".format(alltries, trueguesses))
