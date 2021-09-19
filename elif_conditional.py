userReply = input("Would you like to buy stamps, an envelope, or make copies? (Type stamps or envelope or copy)")
if(userReply == "stamps"):
    print("We have plenty of stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Type a number)")
    print("Here are {} copies".format(copies))
else:
    print("Thank you, please come again.")