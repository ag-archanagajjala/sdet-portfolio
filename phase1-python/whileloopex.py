while True:
    name = input("Who are you? > ")
    if name != 'Joe':
        continue
    print("Hello, Joe. What is password? (It is a fish.)")
    password = input()
    if password == "swordfish":
        break
print("Access granted.")    



# --------------------------------------

# while True:
#     name = input("Please type your name > ")
#     if name == "your name":
#         break
# print('Thank you!')

# --------------------------------------

# print("Start")
# name = ""
# while (name != 'your name'):
#     name = input("Please type your name > ")
# print('Thank you!')
# print("End")

