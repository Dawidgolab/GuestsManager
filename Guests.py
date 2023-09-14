import Manager
from enum import IntEnum

print("Welcome in the Guest Manager!!!")

#Using the IntEnum library
Menu = IntEnum('Menu',"Add, Delete, Search, All, Save, Exit")
guest_list = []

guest_list = Manager.load_guest_list()

#Menu
while True:

    choice = int(input('''
1 - Add guest
2 - Remove guest
3 - Search the list 
4 - Show all guests
5 - Save in file guests.txt
6 - Exit program 
Select option: \n'''))

    if choice == Menu.Add:
        name = input("Give the name:")
        guest_list.append(name)
        print("Added correctly!\n")

    elif choice == Menu.Delete:
        print("Specify the name and surname you wish to remove")
        name = input("Give the name:")
        Manager.Remove(name,guest_list)

    elif choice == Menu.Search:
        print("Check if the guest is on the list")
        name = input("Give the name:")
        if name in guest_list:
            print(name,"is on the list!\n")
        else:
            print(name," is not on the list!!!\n")

    elif choice == Menu.All:
        if guest_list:
            for i, name in enumerate(guest_list):
                print(i+1,"-",name)
        else:
            print("The list is empty!!")

# saving in the guests.txt file
    elif choice == Menu.Save:
        Manager.save_guest_list(guest_list)

    elif choice == Menu.Exit:
        print("Good bye!!!\n")
        break
    else:
        print("You selected the wrong option!!!\n")