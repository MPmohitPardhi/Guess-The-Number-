import random
a=random.randint(1,100)

n = -1
Guessa = 1
while(n != a):
   
   n = int(input("Guess The Number: "))
   if(n > a):
      print("Lower Number pless")
      Guessa += 1
   elif(n < a):
      print("higher Number pless")
      Guessa += 1

print(f"you guess the {n} corrrect Number in {Guessa} attempt")      