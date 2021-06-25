Heroes = {"AAA" : "Starlord",
"AAB" : "Drax",
"ABA" : "Black Panther",
"ABB" : "Doctor Strange",
"BAA" : "Winter Soldier",
"BAB" : "Rocket Raccoon",
"BBA" : "Captain America",
"BBB" : "Iron Man",
"CAA" : "Groot",
"CAB" : "Hulk",
"CBA" : "Spiderman",
"CBB" : "Mantis",
"DAA" : "Thanos",
"DAB" : "Thor",
"DBA" : "Hawkeye",
"DBB" : "Black Widow"}

name = input ("Hello, what is your name? ")
answer = input ("Hello " + name + "! Ready to play? YES or No ")
print()
if answer.upper() == "YES":
  question1 = input ("What color would you chose? (Chose A, or B)\na) Blue \nB) Red\n") 
  question2 = input ("What game would you play (ChooseA, or B)\nA) Minecraft \nB Fortnite\n")
  question3 = input ("What sport would you prefer? (Choose A, or B)\nA) Tennis \nB) Basketball\n")
  choise = question1 + question2 + question3
  wait = input ("Do you want to know your favorite marvel hero? YES or No: ")
  if wait.upper() == "YES":
    print("This is you Marvel Charectar: " + Heroes[choise.upper()])
  else:
    print("ok")

else:print("Okay, Bye bye!")