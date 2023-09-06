# Task 1
import re

# contain = "Hi what going on 111 bbbsssaaa999dndw ?! "

# patern = "([a-z]|[A-Z]|[0-9]+)"



# matches = re.findall(patern, contain)
# if matches:
#     for match in matches:
#         contain = contain.replace(match, "")
#     print(contain)
# else:
#     print("All fine")

# print(matches)


#Task 2

# # pattern = ".(b+|0?)"

# pattern = "ab*"

# found = re.search(pattern, "hbbbbb0")
# print(found)


# #Task 3

# pattern2 = "ab+"

# print(re.search(pattern2, input("Writt here:")))

#Task 4

# pattern3 = "ab?"

# print(re.search(pattern3, input("Writt here:")))

# #Task 5

# # pattern4 = "abbb"
# pattern4 = "ab{3}"
# print(re.search(pattern4, "abbb"))

# #Task 6

# pattern5 = "ab{2,3}"

# print(re.search(pattern5, "abb b"))

# # Task 7

# pattern6 = "[a-z]+_[a-z]+"

# print(re.search(pattern6, "iiih_iii how are you?"))

# #Task 8

# pattern7 = "[A-Z][a-z]"

# print(re.search(pattern7, "Hi how are you?"))

# # Task 9

# pattern8 = "a.*b"
# print(re.search(pattern8, "Hi how are you?"))

# #Task 10

# pattern9 = "^[A-Za-z]+"
# print(re.search(pattern9, "Hinow how are you?"))

# #Task 11
# pattern10 = "[A-Za-z]+\.?$"
# print(re.search(pattern10, "Hinow how are you luckyone."))

# # Task 12
# pattern11 = "[A-Za-z]*z[A-Za-z]*"
# print(re.search(pattern11, "Hinow zow are you luckzone."))

# #Task 13 
# pattern12 = "[A-Za-z]+z[A-Za-z]+"
# print(re.search(pattern12, "Hinow howz are zou luckzone."))

# #Task 14
# pattern13 = "\w+"
# print(re.search(pattern13, "HinJ4ow234_ howz are zou luckzone."))

# #Task 15

# number = int(input("Enter a number:"))

# text = ("Moin", "Hello", "Hi")

# for string in text:
#     string = str(number) + " " + string
#     print(string)


# pattern14 = "^\d+"
# print(re.findall(pattern14, "string.")) 1. try

# for string in text:   2. try
#     match = re.search(pattern14, string)
#     if match:
#         found_number = match.group()
#         print(f"Found number: {found_number} in '{string}'")
#     else:
#         print(f"No number found in '{string}'")


#Task 16

ipAddress = str(input("Enter here your ip address: "))
pattern15 = r'\b0+(\d+)\b'

remove_ip = re.sub(pattern15, r'\1', ipAddress)

print("Removed 0 from IP adress:", remove_ip)

