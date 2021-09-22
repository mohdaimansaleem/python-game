import random

Random_number=random.randint(1,100)
guess=None
count=0
#rint(Random_number)

high_score=open("high_score.txt","r")
score=high_score.read()
sol=int(score)
high_score.close()

winner=open("winner_name.txt","r")
w_name=winner.read()
winner.close()

print(f"HIGH SCORE BY {w_name}  ")
print(f"HIGH SCORE : {sol}  ")


while (guess!=Random_number):
       
       
  guess=int(input("\n\tGUESS A NUMBER IN BETWEEN 1-100 :"))
  count=count+1
       
  if(guess==Random_number):

   print("YOU WON BUDDY!!")
   print(f"NUMBER OF ATTEMPTS : {count} ")
  elif(guess>Random_number):

   print("\tENTER A SMALLER NUMBER..")
  elif(guess<Random_number):
    print("\tENTER A GREATER NUMBER..")

if(sol>=count):
   print("NEW RECORD!!")
   name=input("ENTER NAME :")

   name=name.upper()
   high_score=open("high_score.txt","w")
   count=str(count)
   high_score.write(count)
   high_score.close()
   winner_name=open("winner_name.txt","w")
   winner_name.write(name)
   winner_name.close