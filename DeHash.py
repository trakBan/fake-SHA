import json

# de hashing fake hash

def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

non_numbered_letters = ["rg", "fw", "rj", "ko", "jk", "eu", "ko", "wi"]

dir = "DeHashOptions.json" # Your directory to the json file here
with open(dir, "r") as read_file:
    code = json.load(read_file)

phrase = input("Put your fake hash: ")
phrase = phrase.lower()

# Converting to a list for easier removing irrelevant numbers and letters
phrase_list = Convert(phrase)
first_two = phrase[0] + phrase[1]

while True:
    # Removing first two letters if they were generated.#
    if first_two in non_numbered_letters:

        phrase_list.pop(0)
        phrase_list.pop(0)
        first_two = phrase[2] + phrase[3]

    else:
        first_two = phrase[0] + phrase[1]

    # Removing 2 numbers if they were found in DeHashOptions under "num"
    try:
        json_check = code["num"][first_two]
        phrase_list.pop(0)
        phrase_list.pop(0)
        break

    except KeyError:
        break

phrase = "".join(phrase_list)

one_set = ""
dehashed_string = ""

for x in phrase:
    one_set = one_set + x

    if one_set == "0":
        break

    if len(one_set) == 2:
        
        dehashed_string = dehashed_string + code["main"][one_set]
        one_set = ""

print(dehashed_string)