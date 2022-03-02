# python program to build a text-based adventure game in python

yes_answer=["yes","Y","y","Yes"]
no_answer=["no","No","N","n"]

print(''' WELCOME TO THE GAME
 You are standing outside your house and a man comes to you screaming and running.You need to decide whether you want to 
 help the man.
''')

ans1=input("Enter Whether you want to help the man:")

if ans1 in yes_answer:
    print("You have decided to help the man and have hid him!")
    print("After some time police comes to you and say that the man was a theif and they were catching the theif and asked you whether you have seen a man running.")
    ans2=input("Enter your answer!")
    if ans2 in yes_answer:
        print("Congratulations you have won.You have helped police to catch a theif")
    elif ans2 in no_answer:
        print("You just helped an absconding theif and now you have to go to jail")
    else:
        print("Enter a valid response")
elif ans1 in no_answer:
    print("Congratulations.you have won !")

else:
    print("Please enter a valid response")

