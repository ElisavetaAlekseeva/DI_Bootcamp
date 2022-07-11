# # # Exercise 3 : Outputs
# # # Instructions
# # # Predict the output of the following code snippets:
# # 3 <= 3 < 9 #true
# # 3 == 3 == 3 #true
# # bool(0) #false
# # bool(5 == "5") #false
# # bool(4 == 4) == bool("4" == "4") #true
# # bool(bool(None)) #false
# # x = (1 == True) #true
# # y = (1 == False) #false
# # a = True + 4 #5
# # b = False + 10 #10

# # print("x is", x) #x is true
# # print("y is", y) #y is false
# # print("a:", a) #a: 5
# # print("b:", b) #b: 10



# # Exercise 4 : How Many Characters In A Sentence ?
# # Instructions
# # Use python to find out how many characters are in the following text, use a single line of code (beyond the establishment of your my_text variable).
# my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
# print(len(my_text))



# Exercise 5: Longest Word Without A Specific Character
# Instructions
# Keep asking the user to input the longest sentence they can without the character “A”.
# Each time a user successfully sets a new longest sentence, print a congratulations message.
lengthUser = 0
while(True):
    user = input('enter the longest sentence you can without the character “A”: ')
    longestStr = len(user)
    if(longestStr > lengthUser and not ('a' in user)):
        lengthUser = longestStr
        print('congratulation message')
    else:
        print('do not suit')
