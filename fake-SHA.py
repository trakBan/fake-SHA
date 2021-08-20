import json
import random

# fake hashing

non_numbered_letters = ["rg", "fw", "rj", "ko", "jk", "eu", "ko", "wi"]
sha_like = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def RNG(num1, num2):
    return round(random.uniform(num1, num2))

dir = "HashOptions.json" # Your directory to the json file here
with open(dir, "r") as read_file:
    code = json.load(read_file)

phrase = input("Puy your phrase here!: ")
phrase = phrase.lower()

if len(phrase) > 28:
    print("You cannot have more than 28 characters")

# there is 65% chance that first two letters of fake hash will have 2 numbers from non_numbered_letters 
if(RNG(0, 100) >= 65):
    try:
        numbered_string = code["num"][phrase[0]]
    except KeyError:
        print("You entered the unsopported key!")
else:
    numbered_string = non_numbered_letters[RNG(0, 7)] + code["num"][phrase[0]]
counter = 0

for i in phrase:
    counter=+ 1
    numbered_string = numbered_string + str(code["main"][i])

lenght_needed_numbered_string = (64 - len(numbered_string))
numbered_string = numbered_string + "0"

# Generating the rest of hash to make it up to 64 chars
for x in range(lenght_needed_numbered_string - 1):
    numbered_string = numbered_string + sha_like[RNG(0, 35)]

print(numbered_string)