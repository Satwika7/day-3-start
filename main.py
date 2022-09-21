print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height>=120:
  print("you can ride the rollercoaster")
  age = int(input("what is your age"))
  if(age>18):
    print("ticket amount is $12")
  elif(age>=12):
    print("ticket amount is $7")
  else:
    print("ticket amount is $5")
else:
  print("sorry you cannot ride")