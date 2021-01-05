# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Combines two names
combined_names = name1.lower() + name2.lower()

#Set up score and count for word true love

t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("e")
e = combined_names.count("e")

true = t + r + u + e

l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")

love = l + o + v + e

love_score = true + love

# Conditions and output

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score == 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.") 
else:
  print(f"Your score is {love_score}.")