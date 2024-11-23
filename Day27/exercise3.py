#Use list data types
#Display the final amount after the game

winAmount = 0
cName = str(input("Hello it's Amar(Devloper of this Program) Welcomes You\nEnter Your First Name Only: "))
print("Hello", cName.capitalize(), "It is a QuizGame Which is Inspired From A T.V Program Called KBC")
print("***********So Let's Start The Quiz***********")

quesList = [
    "Who was the first Prime Minister of India?",
    "What is the capital city of India?",
    "Which state is also known as the “Fruit Bowl” of India?",
    "Who is Sachin Tendulkar?",
    "Who discovered India?",
    "Who is popularly known as the “Iron Man” of India?",
    "Which is the national sport of India?",
    "Who is the current President of India?",
    "Which place in India is also known as the “Land of Rising Sun”?",
    "Where is Taj Mahal located in India?"
]
ansOptions = [
    "\nOptions Are : \n(a)Indira Gandhi\n(b)Narendra Modi\n(c)Jawaharlal Nehru\n(d)Rajiv Gandhi\nChoose the correct option: ",
    "\nOptions Are : \n(a)Kolkata\n(b)Ahemdabad\n(c)Pune\n(d)Delhi\nChoose the correct option: ",
    "\nOptions Are : \n(a)Rajasthan\n(b)Kashmir\n(c)Pune\n(d)Mumbai\nChoose the correct option: ",
    "\nOptions Are : \n(a)Tennis Player\n(b)Crickter\n(c)Badminton Player\n(d)Swimmer\nChoose the correct option: ",
    "\nOptions Are : \n(a)Vasco da Gama\n(b)Narendra Modi\n(c)Captain Hook\n(d)Iron Man\nChoose the correct option: ",
    "\nOptions Are : \n(a)Indira Gandhi\n(b)Narendra Modi\n(c)Jawaharlal Nehru\n(d)Sardar Vallabh Bhai Patel\nChoose the correct option: ",
    "\nOptions Are : \n(a)Cricket\n(b)Hockey\n(c)Swimming\n(d)Badminton\nChoose the correct option: ",
    "\nOptions Are : \n(a)Indira Gandhi\n(b)Draupadi Murmu\n(c)Jawaharlal Nehru\n(d)Rajiv Gandhi\nChoose the correct option: ",
    "\nOptions Are : \n(a)Gujrat\n(b)Arunachal Pradesh\n(c)Hyedrabad\n(d)Odisha\nChoose the correct option: ",
    "\nOptions Are : \n(a)Gujrat\n(b)Agra\n(c)Hyedrabad\n(d)Odisha\nChoose the correct option: "
]

print(quesList[0], ansOptions[0], "\n")
ques1 = str(input("Your answer: "))

if ques1 == 'c':
    print("You won 1,000 Rs !!")
    winAmount = winAmount + 1000
else:
    print("You lost !!, better luck next time", cName)
    exit()

print(quesList[1], ansOptions[1], "\n")
ques2 = str(input("Your answer: "))

if ques2 == 'd':
    print("You won 1,000 Rs !!")
    winAmount = winAmount + 1000
else:
    print("You lost !!, better luck next time", cName)
    exit()
print(quesList[2], ansOptions[2], "\n")
ques2 = str(input("Your answer: "))

if ques2 == 'b':
    print("You won 2,000 Rs !!")
    winAmount = winAmount + 2000
else:
    print("You lost !!, better luck next time", cName)
    exit()
print(quesList[3], ansOptions[3], "\n")
ques2 = str(input("Your answer: "))

if ques2 == 'b':
    print("You won 4,000 Rs !!")
    winAmount = winAmount + 4000
else:
    print("You lost !!, better luck next time", cName)
    exit()
print(quesList[4], ansOptions[4], "\n")
ques2 = str(input("Your answer: "))

if ques2 == 'a':
    print("You won 12,000 Rs !!")
    winAmount = winAmount + 12000
else:
    print("You lost !!, better luck next time", cName)
    exit()

print(quesList[5], ansOptions[5], "\n")
ques2 = str(input("Your answer: "))

if ques2 == 'd':
    print("You won 20,000 Rs !!")
    winAmount = winAmount + 20000
else:
    print("You lost !!, better luck next time", cName)
    exit()

print(quesList[6], ansOptions[6], "\n")
ques2 = str(input("Your answer: "))

if ques2 == 'b':
    print("You won 40,000 Rs !!")
    winAmount = winAmount + 40000
else:
    print("You lost !!, better luck next time", cName)
    exit()

print(quesList[7], ansOptions[7], "\n")
ques2 = str(input("Your answer: "))

if ques2 == 'b':
    print("You won 12,00,00 Rs !!")
    winAmount = winAmount + 120000
else:
    print("You lost !!, better luck next time", cName)
    exit()

print(quesList[8], ansOptions[8], "\n")
ques2 = str(input("Your answer: "))

if ques2 == 'b':
    print("You won 2,00,000 Rs !!")
    winAmount = winAmount + 200000
else:
    print("You lost !!, better luck next time", cName)
    exit()
print(quesList[9], ansOptions[9], "\n")
ques2 = str(input("Your answer: "))

if ques2 == 'b':
    print("You won 10,00,000 Rs !!")
    winAmount = winAmount + 1000000
else:
    print("You lost !!, better luck next time", cName)
    exit()

print ("If you attempted all question correcty then only you are seeing this, congrats for this. You win amount is: ", winAmount, 'Rs')
exit()
    


    
