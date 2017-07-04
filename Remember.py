#Trying to create a program in which your name will be remembered even after the program is closed.

#Doing this by storing the name on a text I/O file.

# Adding pauses because I find it personally more entertaining and lifelike.
from time import sleep

#Opening file and setting variable "Name" to that file
My_File = open('name.txt', 'r')
Name = My_File.read()
My_File.close()



# If the computer doesn't have anything stored in the file...
if(Name == ''):
    #The Computer will greet you try to find out your name
    print("Hey there!")
    sleep(1)
    print("My name is...")
    sleep(1)
    print("...")
    sleep(2)
    print("...")
    sleep(3)
    print("Actually, I don't have a real name.")
    sleep(1)

    Name = str(input("What is YOUR name?\n\n>>>"))

    print(Name)
    My_File = open('name.txt','w')
    My_File.write(Name)
    My_File.close()
    sleep(3)
    print("I'll make sure to remember that.")
    sleep(1)
else:
    #But if the computer DOES have something stored in it's database, then it will greet you like an old pal
    print("Heyyyy!")
    sleep(1)
    print("I know you!")
    sleep(0.5)
    print('You are', Name, '!')
    sleep(1)
    # Then it will attempt to make sure that the name is correct, and if it isn't, then it will try to get your name
    ans = str(input("This is you, right? ('Y'/'N')\n\n>>>"))
    if (ans == 'N'):
        print("oops.")
        sleep(1)
        print("...")
        sleep(2)
        Name = str(input("What IS your name? (Remember to use quotation marks outside of your text\n\n>>>"))
        print(Name)
        My_File = open('name.txt','w')
        My_File.write(Name)
        My_File.close()
        print("Ok, got it.")
        sleep(1)
print("Alright then, goodbye!")
