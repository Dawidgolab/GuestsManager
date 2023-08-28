import Manager
from enum import IntEnum

print("Welcome in the Guest Manager!!!")

Menu = IntEnum('Menu',"Add, Delete, Search, All, Exit")
list = []


while True:

    choice = int(input('''
1 - Add guest
2 - Remove guest
3 - Search the list 
4 - Show all guests
5 - Exit program 
Select option: \n'''))

    if choice == Menu.Add:
        name = input("Give the name:")
        list.append(name)
        print("Added correctly!\n")

    elif choice == Menu.Delete:
        print("Specify the name and surname you wish to remove")
        name = input("Give the name:")
        Manager.Remove(name,list)

    elif choice == Menu.Search:
        print("Check if the guest is on the list")
        name = input("Give the name:")
        if name in list:
            print(name,"is on the list!\n")
        else:
            print(name," is not on the list!!!\n")

    elif choice == Menu.All:
        for i, name in enumerate(list):
            print(i+1,"-",name)

    elif choice == Menu.Exit:
        print("Good bye!!!\n")
        break
    else:
        print("You selected the wrong option!!!\n")