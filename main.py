"""
Name(s): Taj Chhabra, Mark
Name of Project: Hangman

We did this in another file, then copy and pasted

"""
import random
import turtle
from turtle import *

turtle.ht()     #Hides cursor

xPos = -100
yPos = -115

head_radius = 35
body_length = 65

neck_length = 20
arm_length = 45
arm_angle = 60
leg_length = 40
leg_angle = 30

mouth_radius = 15
sadness = 100

mouth_to_eye = 20
eye_distance = 10
eye_size = 10

Screen().setup(width = 450, height = 300)      #Screen size
Screen().colormode(255)       #Color scheme

turtle.penup()
turtle.goto(xPos, yPos)       #Starting coordinated
turtle.pendown()

turtle.left(90)       
turtle.forward(200)
turtle.right(45)
turtle.forward(50)
turtle.right(45)
turtle.forward(75)
turtle.right(90)
turtle.forward(25)        #Making Gallows ^^^


#----------------------------------------------------------
words = ["python", "jumble", "easy", "difficult", "answer",  "xylophone", "schizophrenia","programmer", "cheng", "mannix", "europe", "antarctica", "north", "south", "america", "asia", "australia", "anything", "superman", "africa", "bulgaria", "china", "property", "tooth", "signature", "argument", "food", "employee", "policy", "insect", "diamond", "cabinet", "photo", "situation", "army", "stranger", "safety", "office", "garbage", "excitement", "community", "tongue", "speaker", "bath", "conclusion", "procedure", "reputation", "passion", "hair", "writer", "university", "poem", "investment", "resolution", "dirt", "painting", "industry", "election", "nation", "resource", "village", "entry", "skill", "connection", "coma", "sunday", "drum", "model", "architect", "division", "basketball", "officer", "word", "activity", "island", "nail", "president", "gallery", "restrict", "ticket", "art", "cemetery", "random", "concert", "resource", "orchestra", "culture", "vacuum", "worker", "save", "betray", "delicate", "virtue", "corn", "recommend", "patent", "sculpture", "flexible", "list", "privacy", "structure", "apple", "worker", "personality", "moment", "teaching", "excitement", "community", "celebration", "management", "potato", "argument", "income", "property", "virus", "world", "control", "freedom", "winner", "library", "selection", "woman", "procedure", "newspaper", "fortune", "heart", "thanks", "wealth", "video", "entertainment", "accident", "skill", "homework", "speaker", "chocolate", "currency", "departure", "department", "assistant", "championship", "delivery", "orange", "explanation"]

chosen = random.choice(words)
chosen = chosen.lower()

all_letters = list(chosen)

cur_found = []
for i in range(len(all_letters)):
  cur_found.append("_")
print(*cur_found)
print()                          #Budget \n

mistakes_left = 8


#---------------------------------------------------------

def hangman(life):
  
  if life == 6:       #Fault 1
    turtle.right(90)
    turtle.circle(head_radius)        #Head ^^^
    turtle.left(90)
    turtle.penup()
    turtle.forward(head_radius * 2)
    turtle.pendown()
    turtle.forward(body_length)        #Body ^^^
  
  if life == 4:       #Fault 2
    xPos = turtle.xcor()
    yPos = turtle.ycor()
    turtle.left(leg_angle)
    turtle.forward(leg_length)
    turtle.goto(xPos, yPos)
    turtle.right(leg_angle * 2)
    turtle.forward(leg_length)        #Legs ^^^

    turtle.penup()
    turtle.goto(xPos, yPos)
    turtle.setheading(90)
    turtle.forward(body_length - neck_length)
    xPos = turtle.xcor()
    yPos = turtle.ycor()
    turtle.pendown()
    turtle.right(arm_angle)
    turtle.forward(arm_length)
    turtle.goto(xPos, yPos)
    turtle.left(arm_angle * 2)
    turtle.forward(arm_length)
    turtle.goto(xPos, yPos)       #Arms ^^^

  if life == 2:
    turtle.setheading(90)
    turtle.penup()
    turtle.forward(neck_length + 25)
    turtle.pendown()
    xPos = turtle.xcor()
    yPos = turtle.ycor()
    turtle.setheading(180)
    turtle.circle(mouth_radius, extent = sadness)
    turtle.penup()
    turtle.goto(xPos, yPos)
    turtle.pendown()
    turtle.setheading(180)
    turtle.circle(mouth_radius, extent = -sadness)        #Mouth ^^^
    turtle.penup()
    turtle.goto(xPos, yPos)

  if life == 0:
    turtle.pencolor(240, 30, 0)
    turtle.width(3)
    turtle.setheading(90)
    turtle.forward(mouth_to_eye)
    xPos = turtle.xcor()
    yPos = turtle.ycor()
    
    turtle.setheading(0)
    turtle.forward(eye_distance)
    turtle.right(45)
    turtle.pendown()
    turtle.forward(eye_size)
    turtle.penup()
    turtle.backward(eye_size / 2)
    turtle.right(90)
    turtle.forward(eye_size/2)
    turtle.pendown()
    turtle.backward(eye_size)

    turtle.penup()
    turtle.goto(xPos, yPos)
    turtle.setheading(180)
    turtle.forward(eye_distance)
    turtle.left(45)
    turtle.pendown()
    turtle.forward(eye_size)
    turtle.penup()
    turtle.backward(eye_size / 2)
    turtle.right(90)
    turtle.forward(eye_size/2)
    turtle.pendown()
    turtle.backward(eye_size)       #Eyes ^^^
  
  if life > 0:
    guess_option(life)
  else:
    print("You lose!")
    print("The chosen word was \"" + chosen + "\"")





def guess_letter(fault):
  guess = input("Enter a letter guess: ")[0] #Will choose first letter of guess
  guess = guess.lower()
  if guess in all_letters:
    for counter in range (0, len(all_letters)):
      if guess == all_letters[counter]:
        cur_found[counter] = guess
    print(*cur_found)      
    print()                   #Budget \n
    guess_option(fault)

  else:
    print()
    print("\"" + guess + "\" is not in the chosen word")
    fault = fault - 1
    print("Tries left: " + str(fault))
    print(*cur_found)
    print()
    hangman(fault)




def guess_word(fault):
  guess = input("Enter the word: ")
  guess = guess.lower().strip()
  if guess == "".join(all_letters):
    print("You win!")
  else:
    print()
    print("\"" + guess + "\" is not the word")
    fault = fault - 1
    print("Tries left: " + str(fault) + "\n")
    hangman(fault)



def guess_option(mistakes_left):
  option = input("Would you like to guess a letter (1) or guess the word (2): ")
  if option == "1":
    guess_letter(mistakes_left)

  elif option == "2":
    guess_word(mistakes_left)
  
  else:
    print("That is not a valid response \n")
    guess_option(mistakes_left)





guess_option(mistakes_left)
