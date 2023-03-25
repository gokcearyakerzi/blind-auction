logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

from replit import clear
#HINT: You can call clear() to clear the output in the console.

names_bides = {}

name = input("What is your name?:")
bid = input("What's your bid?:")
names_bides[name] = bid
ask = input("Are there any other bidders? Type 'yes' or 'no'")

def function():
  name = input("What is your name?:")
  bid = input("What's your bid?:")
  names_bides[name] = bid
  

while ask == "yes":
  clear()
  function()
  ask = input("Are there any other bidders? Type 'yes' or 'no'")
else:
  clear()
  max = max(names_bides)
  print(f"The winner is {max} with a bid of {names_bides[max]}")